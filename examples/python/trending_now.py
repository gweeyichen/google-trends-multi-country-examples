"""Print today's trending searches for the Southeast Asia preset.

Usage:
    export APIFY_TOKEN=...
    python trending_now.py
"""
import os
import sys

from apify_client import ApifyClient

ACTOR_ID = "asia-data-desk/google-trends-sea"


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set the APIFY_TOKEN environment variable first.")

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(
        run_input={"mode": "trending_now", "countryPreset": "SEA", "maxItems": 60}
    )
    if run is None:
        sys.exit("The run did not return a Run object.")

    for item in client.dataset(run.default_dataset_id).iterate_items():
        if item.get("record_type") != "trending":
            continue
        traffic = item.get("approx_traffic_raw") or "n/a"
        print(f"{item['country']}  #{item['rank']:<2} {item['title']}  (traffic {traffic})")


if __name__ == "__main__":
    main()
