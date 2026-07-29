# Romaniacs Fast Site

Fastest public hosting for a snapshot:

1. Open `https://app.netlify.com/drop`.
2. Drag the whole `romaniacs_fast_site` folder onto the page.
3. Share the generated Netlify URL.

This is a static snapshot. To refresh it, replace `data/progress.json` with a newer copy from:

`https://www.redbullromaniacs.com/data-json/rbr2026/day1/progress.json`

Then drag the folder to Netlify Drop again.

Auto-refresh hosting:

1. Create a GitHub repository.
2. Upload the contents of this `romaniacs_fast_site` folder to the repository root.
3. In GitHub, go to `Settings` -> `Pages`.
4. Set `Build and deployment` to `Deploy from a branch`.
5. Select the `main` branch and `/ (root)`.
6. Go to `Actions` and enable workflows if GitHub asks.
7. Run `Update Romaniacs Progress` once manually, or wait for the schedule.

The workflow refreshes `data/progress.json` every 5 minutes. The webpage itself checks for a newer `data/progress.json` every 60 seconds.

Local preview:

```bash
cd romaniacs_fast_site
python3 -m http.server 8000
```

Open `http://localhost:8000`.
