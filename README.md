# Google Trends Multi-Country: examples

Ready-to-run examples for the Apify Actor [Google Trends Scraper: Multi-Country Compare + Trending Now](https://apify.com/asia-data-desk/google-trends-sea) (`asia-data-desk/google-trends-sea`).

## What the Actor does

- **Compare.** Interest over time for 1 to 5 keywords in up to 15 countries, **on one 0-100 scale per keyword**, so countries can be compared directly. Optional top and rising related queries, and interest by subregion (province or state level) for each keyword and country, optionally within one Google Trends category.
- **Trending now.** Today's trending searches for each country you pick, one record per search, with approximate traffic, start time and up to three news links.
- Country presets: `SEA` (default), `ASEAN`, `APAC`, `EU5`, `ANGLO`, `G7`, or your own list of ISO country codes.
- HTTP only: no browser, no login, no CAPTCHA solving. Google rate limits apply; see the Limits section of the Store page.

Most Google Trends Actors take one country per run, and each run is scaled to its own peak, so the series cannot be compared with each other. This Actor chains requests through an anchor market so that up to 15 markets share one scale per keyword. Every record states how its scale was made (`scale_method`).

## Who it is for

Market researchers, marketers, analysts and developers who need to compare search interest across several countries, or monitor what is trending in a region, without stitching single-country runs together.

## Quick start

1. Create an Apify account and copy your API token from the Console (Settings, Integrations).
2. `export APIFY_TOKEN=your_token_here` (never commit it).
3. Run one of the examples below, for example:

```bash
cd examples/python
pip install -r requirements.txt
python compare_countries.py durian "bubble tea"
```

Running the Actor is billed by Apify (pay per event). Prices at the time of writing (free plan, from the Actor's pricing; check the Store page for current prices): US$0.02 per run start, US$0.008 per interest series (one keyword in one country), US$0.002 per trending search, US$0.004 per related-queries set or subregion set. Every example sets `maxItems` to cap spend.

## Examples

| Path | What it shows |
|---|---|
| `examples/python/compare_countries.py` | Compare 1-2 keywords across SEA with `apify-client`, print average interest per country |
| `examples/python/trending_now.py` | Today's trending searches for SEA |
| `examples/node/compare_countries.mjs` | The same comparison with `apify-client` for JavaScript |
| `examples/curl/run_sync.sh` | One `run-sync-get-dataset-items` call with curl (300 second limit) |
| `examples/notebook/compare_chart.ipynb` | Jupyter notebook that charts the comparison with matplotlib |
| `examples/inputs/sea_compare.json` | Compare two keywords across Southeast Asia with related queries |
| `examples/inputs/apac_trending.json` | Trending now across the APAC preset |
| `examples/inputs/eu5_compare.json` | Compare a keyword across five European countries |
| `examples/inputs/one_country_subregions.json` | One country with interest by subregion |
| `examples/inputs/category_filter.json` | Compare within one category (71, Food & Drink) |

The input files can be pasted into the Console or passed to `run_sync.sh`: `./run_sync.sh ../inputs/sea_compare.json`.

## Notes

- Subregion values run 0-100 within each country only; they cannot be compared between countries.
- Interest values are Google's relative 0-100 index, not search counts.
- Data source: Google Trends (https://www.google.com/trends). This project and the Actor are not made, endorsed or sponsored by Google.

## License

MIT, see [LICENSE](LICENSE). Issues: see [CONTRIBUTING.md](CONTRIBUTING.md).
