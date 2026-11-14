from pathlib import Path

import geopandas as gpd

data_dir = (
    Path(__file__).resolve().parents[1]
    / "week-10"
    / "data"
    / "processed"
)

wards = gpd.read_file(data_dir / "wards.gpkg", layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file(
    data_dir / "facilities.gpkg", layer="facilities"
).to_crs(epsg=32631)

centres = wards[["ward_name", "geometry"]].copy()
centres["geometry"] = wards.centroid

nearest = gpd.sjoin_nearest(
    centres, facilities[["name", "geometry"]], how="left", distance_col="distance_m"
)
nearest["distance_km"] = (nearest["distance_m"] / 1000).round(2)
print(nearest[["ward_name", "name", "distance_km"]])