#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 <tool name> <tool location>"
    exit 1
fi

TOOL="$1"
LOCATION="$2"

mkdir -p "syllabuses/$LOCATION/$TOOL"
sed "s/\$TOOL/$TOOL/g" generator/templates/syllabus.md.tmpl > "syllabuses/$LOCATION/$TOOL/syllabus.md"
sed "s/\$TOOL/$TOOL/g" generator/templates/risk-assessment.md.tmpl > "syllabuses/$LOCATION/$TOOL/risk-assessment.md"

echo -e "Added scaffolding for $TOOL in $LOCATION. Now edit:"
echo -e "\tsyllabuses/$LOCATION/$TOOL/syllabus.md"
echo -e "\tsyllabuses/$LOCATION/$TOOL/risk-assessment.md"
