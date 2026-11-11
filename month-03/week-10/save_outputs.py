from pathlib import Path
import geopandas as gpd

# Works whether you run from project root OR from week-10
if Path("month-03/week-10/data/processed/wards.gpkg").exists():
    BASE = Path("month-03/week-10")
else:
    BASE = Path.cwd()

wards = gpd.read_file(BASE / "data/processed/wards.gpkg", layer="wards")
wards.to_file(BASE / "data/processed/week10_outputs.gpkg", layer="wards_copy")
wards.drop(columns="geometry").to_csv(BASE / "wards_table.csv", index=False)

print(gpd.list_layers(BASE / "data/processed/week10_outputs.gpkg"))
print("Saved to:", BASE)