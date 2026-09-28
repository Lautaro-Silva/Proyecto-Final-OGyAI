#!/usr/bin/env bash
# Compila figuras e informe (pdflatex, dos pasadas). Uso: ./build.sh
set -euo pipefail
cd "$(dirname "$0")"
for fig in timeline workflow; do
  (cd ../figures && pdflatex -interaction=nonstopmode -halt-on-error "$fig.tex" >/dev/null)
done
pdflatex -interaction=nonstopmode -halt-on-error informe.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error informe.tex >/dev/null
echo "OK: informe.pdf"
