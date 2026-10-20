#!/usr/bin/env bash
# Run the Actor synchronously and print the dataset items as JSON.
# Usage:
#   export APIFY_TOKEN=...
#   ./run_sync.sh [input.json]      (default: ../inputs/eu5_compare.json)
# Note: the sync endpoint times out after 300 seconds; for bigger runs use the
# client libraries in ../python or ../node.
set -euo pipefail

: "${APIFY_TOKEN:?Set the APIFY_TOKEN environment variable first}"
INPUT="${1:-$(dirname "$0")/../inputs/eu5_compare.json}"

curl --fail-with-body -sS -X POST \
  "https://api.apify.com/v2/acts/asia-data-desk~google-trends-sea/run-sync-get-dataset-items" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  --data @"${INPUT}"
