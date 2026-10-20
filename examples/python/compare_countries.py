"""Compare 1-2 keywords across Southeast Asia on one 0-100 scale per keyword.

Usage:
    export APIFY_TOKEN=...   # your Apify API token
    python compare_countries.py durian "bubble tea"

Prints the average interest per country for each keyword. Running the Actor
is billed by Apify (pay per event); maxItems below caps the run.
"""
import os
import sys

from apify_client import ApifyClient

ACTOR_ID = "asia-data-desk/google-trends-sea"


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set the APIFY_TOKEN environment variable first.")

    keywords = sys.argv[1:3] or ["durian"]
    run_input = {
        "mode": "compare",
        "countryPreset": "SEA",
        "keywords": keywords,
        "timeframe": "today 12-m",
        "maxItems": 20,
    }

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    if run is None:
        sys.exit("The run did not return a Run object.")

    # keyword -> list of (country, average)
    table: dict[str, list[tuple[str, float]]] = {}
    for item in client.dataset(run.default_dataset_id).iterate_items():
        if item.get("record_type") != "interest" or not item.get("has_data"):
            continue
        table.setdefault(item["keyword"], []).append((item["country"], item["average"]))

    for keyword, rows in table.items():
        print(f"\n{keyword} (average interest, 0-100, one scale across countries)")
        print(f"{'country':<8}{'average':>8}")
        for country, average in sorted(rows, key=lambda r: r[1], reverse=True):
            print(f"{country:<8}{average:>8.1f}")


if __name__ == "__main__":
    main()
