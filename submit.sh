#!/usr/bin/env bash
# Send a JSON file to POST /submit.
#
#   ./submit.sh samples/time_management.json
#
# Putting the JSON in a file avoids shell quoting problems with apostrophes.
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: ./submit.sh path/to/file.json" >&2
  exit 1
fi

curl -s -X POST "http://127.0.0.1:5000/submit" \
  -H "Content-Type: application/json" \
  --data-binary "@$1"
echo
