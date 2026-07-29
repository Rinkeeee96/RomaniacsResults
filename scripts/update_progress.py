import json
import urllib.request
from pathlib import Path


URL = "https://www.redbullromaniacs.com/data-json/rbr2026/day1/progress.json"
OUT = Path(__file__).resolve().parents[1] / "data" / "progress.json"


def main() -> None:
    request = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)

    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated {OUT}")


if __name__ == "__main__":
    main()
