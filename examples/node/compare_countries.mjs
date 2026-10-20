// Compare keywords across Southeast Asia on one 0-100 scale per keyword.
//
// Usage:
//   npm install
//   export APIFY_TOKEN=...
//   node compare_countries.mjs durian "bubble tea"
import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_TOKEN;
if (!token) {
    console.error('Set the APIFY_TOKEN environment variable first.');
    process.exit(1);
}

const keywords = process.argv.slice(2, 4);
const client = new ApifyClient({ token });

const run = await client.actor('asia-data-desk/google-trends-sea').call({
    mode: 'compare',
    countryPreset: 'SEA',
    keywords: keywords.length ? keywords : ['durian'],
    timeframe: 'today 12-m',
    maxItems: 20,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();

const byKeyword = new Map();
for (const item of items) {
    if (item.record_type !== 'interest' || !item.has_data) continue;
    if (!byKeyword.has(item.keyword)) byKeyword.set(item.keyword, []);
    byKeyword.get(item.keyword).push({ country: item.country, average: item.average });
}

for (const [keyword, rows] of byKeyword) {
    console.log(`\n${keyword} (average interest, 0-100, one scale across countries)`);
    rows.sort((a, b) => b.average - a.average);
    console.table(rows);
}
