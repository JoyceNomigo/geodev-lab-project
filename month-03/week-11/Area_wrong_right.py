from pathlib import Path

import geopandas as gpd

wards_path = (
    Path(__file__).resolve().parents[1]
    / "week-10"
    / "data"
    / "processed"
    / "wards.gpkg"
)
wards = gpd.read_file(wards_path, layer="wards")
print("CRS:", wards.crs)

wards["area_wrong"] = wards.area
print(wards[["ward_name", "area_wrong"]].head(3))

print("Suggested UTM:", wards.estimate_utm_crs())
wards_utm = wards.to_crs(epsg=32631)
wards_utm["area_km2"] = wards_utm.area / 1_000_000
print(wards_utm[["ward_name", "area_km2"]].head(3))
print("Ibadan North total:", round(wards_utm["area_km2"].sum(), 1), "km2")