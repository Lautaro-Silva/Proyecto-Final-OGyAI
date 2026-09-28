"""Extract readable per-session text from local Claude Code and Codex transcripts.

Output: one Markdown file per session in notes/_transcripts/ (git-ignored: raw transcripts
may contain internal paths/usernames and must never be committed), plus an index.csv.

Kept in full: user messages and assistant text. Tool calls and tool results are reduced
to one-liners so the files stay readable. Reasoning blocks are encrypted/empty and skipped.

Run:  python3 notes/tools/extract_transcripts.py   (from claude_work/Proyecto_Final_IA/)
"""
import csv
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, '..', '_transcripts')
CLAUDE_GLOB = os.path.expanduser('~/.claude/projects/*ITeDA*/**/*.jsonl')
CODEX_GLOB = os.path.expanduser('~/.codex/sessions/**/*.jsonl')

TEXT_LIMIT = 6000        # max chars kept per user/assistant message
TOOL_INPUT_LIMIT = 250   # max chars of a tool call's input
TOOL_RESULT_LIMIT = 300  # max chars of a tool result


def short(text, limit):
    text = str(text).replace('\n', ' ⏎ ')
    if len(text) > limit:
        return text[:limit] + f' …[+{len(text) - limit} chars]'
    return text


def clip(text, limit):
    if len(text) > limit:
        return text[:limit] + f'\n…[truncated, +{len(text) - limit} chars]'
    return text


def claude_session(path):
    """Return (metadata, lines) for one Claude Code jsonl file."""
    lines = []
    models = set()
    first_ts = None
    last_ts = None
    title = ''
    for raw in open(path, encoding='utf-8', errors='replace'):
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if record.get('type') == 'ai-title':
            title = record.get('aiTitle', title)
        timestamp = record.get('timestamp')
        if timestamp:
            first_ts = first_ts or timestamp
            last_ts = timestamp
        message = record.get('message') or {}
        role = message.get('role')
        if role not in ('user', 'assistant'):
            continue
        model = message.get('model')
        if model:
            models.add(model)
        content = message.get('content')
        stamp = (timestamp or '')[:19]
        if isinstance(content, str):
            lines.append(f'\n### [{stamp}] {role.upper()}\n{clip(content, TEXT_LIMIT)}\n')
            continue
        for block in content or []:
            kind = block.get('type')
            if kind == 'text' and block.get('text', '').strip():
                lines.append(f'\n### [{stamp}] {role.upper()} ({model or ""})\n{clip(block["text"], TEXT_LIMIT)}\n')
            elif kind == 'tool_use':
                lines.append(f'- `[{stamp}] TOOL {block.get("name")}` {short(json.dumps(block.get("input", {}), ensure_ascii=False), TOOL_INPUT_LIMIT)}')
            elif kind == 'tool_result':
                result = block.get('content')
                if isinstance(result, list):
                    result = ' '.join(part.get('text', '') for part in result if isinstance(part, dict))
                lines.append(f'  - result: {short(result, TOOL_RESULT_LIMIT)}')
    meta = {'kind': 'claude', 'title': title, 'models': ';'.join(sorted(models)),
            'start': first_ts, 'end': last_ts}
    return meta, lines


def codex_text(content):
    parts = []
    for part in content or []:
        if isinstance(part, dict) and part.get('text'):
            parts.append(part['text'])
    return '\n'.join(parts)


def codex_session(path):
    lines = []
    models = set()
    first_ts = None
    last_ts = None
    title = ''
    for raw in open(path, encoding='utf-8', errors='replace'):
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        timestamp = record.get('timestamp')
        if timestamp:
            first_ts = first_ts or timestamp
            last_ts = timestamp
        stamp = (timestamp or '')[:19]
        kind = record.get('type')
        payload = record.get('payload') if isinstance(record.get('payload'), dict) else {}
        ptype = payload.get('type')
        if kind == 'event_msg' and ptype == 'thread_settings_applied':
            model = payload.get('thread_settings', {}).get('model')
            if model:
                models.add(model)
                lines.append(f'- `[{stamp}] MODEL SET: {model}`')
        elif kind == 'turn_context' and payload.get('model'):
            models.add(payload['model'])
        elif kind == 'response_item' and ptype == 'message':
            role = payload.get('role')
            text = codex_text(payload.get('content'))
            if role == 'developer' or not text.strip():
                continue
            if role == 'user' and text.startswith('# AGENTS.md instructions'):
                lines.append(f'- `[{stamp}] (AGENTS.md injected)`')
                continue
            lines.append(f'\n### [{stamp}] {role.upper()}\n{clip(text, TEXT_LIMIT)}\n')
        elif kind == 'response_item' and ptype in ('custom_tool_call', 'function_call'):
            call_input = payload.get('input') or payload.get('arguments') or ''
            lines.append(f'- `[{stamp}] TOOL {payload.get("name")}` {short(call_input, TOOL_INPUT_LIMIT)}')
        elif kind == 'response_item' and ptype in ('custom_tool_call_output', 'function_call_output'):
            output = payload.get('output')
            if isinstance(output, list):
                output = codex_text(output)
            lines.append(f'  - result: {short(output, TOOL_RESULT_LIMIT)}')
        elif kind == 'response_item' and ptype == 'agent_message':
            lines.append(f'- `[{stamp}] SUBAGENT MSG {payload.get("author")} -> {payload.get("recipient")}` {short(codex_text(payload.get("content")), TOOL_INPUT_LIMIT)}')
        elif kind == 'event_msg' and ptype == 'task_complete' and payload.get('error'):
            lines.append(f'- `[{stamp}] TASK ERROR` {short(payload["error"].get("message", ""), 200)}')
        elif kind == 'compacted':
            lines.append(f'- `[{stamp}] (context compacted)`')
    meta = {'kind': 'codex', 'title': title, 'models': ';'.join(sorted(models)),
            'start': first_ts, 'end': last_ts}
    return meta, lines


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    index_rows = []
    sources = []
    for path in glob.glob(CLAUDE_GLOB, recursive=True):
        sources.append(('claude', path))
    for path in glob.glob(CODEX_GLOB, recursive=True):
        sources.append(('codex', path))
    for kind, path in sources:
        if kind == 'claude':
            meta, lines = claude_session(path)
        else:
            meta, lines = codex_session(path)
        project = os.path.basename(os.path.dirname(path))
        is_subagent = '/subagents/' in path
        base = os.path.splitext(os.path.basename(path))[0]
        name = f'{kind}__{(meta["start"] or "nodate")[:10]}__{"sub__" if is_subagent else ""}{base[-36:]}.md'
        with open(os.path.join(OUT_DIR, name), 'w', encoding='utf-8') as handle:
            handle.write(f'# {kind} session {base}\n\n')
            handle.write(f'- source project dir: `{project}`\n- subagent: {is_subagent}\n')
            handle.write(f'- title: {meta["title"]}\n- models: {meta["models"]}\n')
            handle.write(f'- start: {meta["start"]}\n- end: {meta["end"]}\n\n')
            handle.write('\n'.join(lines))
        size = os.path.getsize(os.path.join(OUT_DIR, name))
        index_rows.append({'file': name, 'kind': kind, 'subagent': is_subagent, 'project_dir': project,
                           'title': meta['title'], 'models': meta['models'],
                           'start': meta['start'], 'end': meta['end'], 'extracted_bytes': size})
    index_rows.sort(key=lambda row: row['start'] or '')
    with open(os.path.join(OUT_DIR, 'index.csv'), 'w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(index_rows[0].keys()))
        writer.writeheader()
        writer.writerows(index_rows)
    print(f'{len(index_rows)} sessions extracted to {OUT_DIR}')


if __name__ == '__main__':
    main()
