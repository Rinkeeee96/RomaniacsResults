import json
import urllib.error
import urllib.request
from pathlib import Path


BASE_URL = "https://www.redbullromaniacs.com/data-json/rbr2026"
ROOT = Path(__file__).resolve().parents[1]
DAYS = ("day1", "day2", "day3", "day4")
FILES = ("progress", "details", "overall")


def fetch_json(url: str):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)}")


def main() -> None:
    first_progress = None

    for day in DAYS:
        for name in FILES:
            url = f"{BASE_URL}/{day}/{name}.json"
            try:
                data = fetch_json(url)
            except urllib.error.HTTPError as exc:
                if exc.code == 404:
                    continue
                raise

            write_json(ROOT / "data" / day / f"{name}.json", data)
            if day == "day1" and name == "progress":
                first_progress = data

    if first_progress is not None:
        write_json(ROOT / "data" / "progress.json", first_progress)


if __name__ == "__main__":
    main()
