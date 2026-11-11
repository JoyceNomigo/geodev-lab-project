from pathlib import Path
import geopandas as gpd
import matplotlib.pyplot as plt

BASE = Path.cwd()

wards = gpd.read_file(BASE / "data/processed/wards.gpkg", layer="wards")
facilities = gpd.read_file(BASE / "data/processed/facilities.gpkg", layer="facilities")

fig, ax = plt.subplots(figsize=(7, 8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=10)
ax.set_title("Health facilities in Ibadan North")
ax.set_axis_off()

fig.savefig(BASE / "facilities_map.png", dpi=150, bbox_inches="tight")
print("Map saved")