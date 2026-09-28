---
name: notebook-code-legibility
description: In the Tesis-de-Licenciatura---ITeDA repo, analysis notebooks must be written to be read by the author - named fields and DataFrames over tuples, explicit loops over comprehensions, no inline ternaries in plotting calls
metadata:
    pinned: false
---

In this repository (the user's Licenciatura thesis project at ITeDA), the author reads, runs and
edits the analysis notebooks himself in JupyterLab, and he has asked twice, in consecutive tasks,
for the code to be more legible - first "do it in a code that is EXTREMELY legible, heavily
commented and explain all the changes", then, after being given a working figure notebook,
"the code inside the notebook is still not very legible". Heavy commenting alone did not satisfy
him: the second complaint came about a file that was already densely commented. What he objects to
is the *structure* of the code, not the amount of explanation around it.

The concrete patterns that drew the complaint, all from a plotting notebook that was otherwise
correct and well commented:

- helper functions returning bare tuples (`return A1, A1_err`, or `return (np.nan, np.nan) if ...`),
  which then force nested unpacking at the call site, e.g.
  `pd.DataFrame({etiqueta: valores for etiqueta, (valores, _) in resultados.items()})`;
- configuration held in lists of long positional tuples, unpacked differently in different loops
  (`for etiqueta, tabla, columna, *_ in curvas` in one place and
  `for etiqueta, tabla, columna, color, marker, eje, estilo in curvas` in another);
- several inline conditional expressions inside one matplotlib call (`markersize=8 if ... else 6`,
  `fmt=f"-{marker}" if ... else f"--{marker}"`, and so on);
- list comprehensions that both compute and destructure at once.

The preferred style, which should be the default when writing analysis code for this repo: give
every field a name (a small dataclass or a dict with explicit keys for plot/curve configuration),
have computation functions return a `DataFrame` (or dict) with named columns rather than positional
tuples, use explicit `for` loops with named intermediate variables instead of comprehensions that
do more than one thing, and build a style dictionary in a plain `if/else` before passing it to
matplotlib as `**kwargs` instead of putting conditionals inside the call. One obvious step per
notebook cell. Comments and markdown explanations are still wanted - they are simply not a
substitute for code whose shape is already clear.
