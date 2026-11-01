import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "my_data.csv"


def read_rows(filename):
    with open(filename, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def clear_values(rows, column):
    values = []
    for row in rows:
        raw = row.get(column, "")
        if raw is None:
            continue
        raw = raw.strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values


def summarize(values):
    if len(values) == 0:
        return {"smallest": None, "largest": None, "count": 0, "average": None}

    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
        "average": sum(values) / len(values),
    }


def summarize_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clear_values(rows, column)
        report[column] = summarize(values)
    return report


report = summarize_all(CSV_PATH, ["area_km2", "population"])

for column, stats in report.items():
    print(column, "->", stats)


