# Data notes

**Week 2 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Joyce Nomigo

What I downloaded, where it came from, what is in it, and what is wrong
with it.

---

## Summary

|  | Dataset | Type | Retrieved | Status | 
|---|---|---|---|---|
| 1 |  AMAC BOUNDARY | Raster | 13/9/2026 | Partial |
| 2 | Settlement extent |  Vector | 13/9/2026 | OK |
| 3 | Waterways | Vector | 13/9/2026 | OK |


---

## 1. AMAC BOUNDARY

- [GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about)
- **Retrieved:** 13/9/2026
- **File:**  [Ward Boundary.gpkg](../../../GEODEV_LAB/Ward%20Boundary.gpkg)
- **Format:** GeoPackage 
- **Geometry type:** Polygon
- **Feature count:** 12
- **CRS as downloaded:** <EPSG:4326>

| Column | What it holds | Nulls |
|---|---|---|
| Ward | AMAC (e.g. Gwarinpa, Wuse, City Center 1) | 0 |
| LGA  | FCT, used to select AMAC | 0 |

## 2. Waterway

- **QuickOSM** PLugin in QGIS
- **Retrieved:** 13/9/2026
- **File:** [Waterway.gpkg](../../../GEODEV_LAB/DATA/processed/Waterway.gpkg)
- **Format:** GeoPackage
- **Geometry type:**  Line / Polygon 
- **Feature count:**  515
- **CRS as downloaded:** <EPSG:4326>

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| waterway| Feature type (river, stream, drain, canal) | 0 |
| Adm1_name | Municipal| 0 |

## 3. Settlment Extent 

-  [GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about)
- **Retrieved:** 13/9/2026
- **File:**  [AMAC_Settlement_extent.gpkg](../../../GEODEV_LAB/DATA/processed/AMAC_Settlement_extent.gpkg)
- **Format:** GeoPackage
- **Geometry type:**  Polygon
- **Feature count:** 4654
- **CRS as downloaded:** <EPSG:4326>

**Key columns**


| Column | What it holds | Nulls |
|---|---|---|
| Extent Type | Built-up area class | 4 |
|ward | AMAC| 0 |

**What I noticed**

- Large gaps in Gui, Jiwa, Orozo and Karshi 1. Wards with missing settlements will look safer than they are.



---

## 2. <Dataset name>

<Repeat the block above for each dataset.>

---

## Cross-cutting problems

**Everything is in EPSG:4326.** Ward boundary,settlement needs a projected CRS in metres. Reproject all three layers ( to EPSG:32632) before Carrying analysis, or the data will be applied in degrees.




---

**Status:** Week 2 complete. Reprojection and quality checks in Week 3 complete, week 4 complete,
see [Data preparation.md](https://github.com/JoyceNomigo/geodev-lab-project/blob/main/Data%20preparation.md?plain=1).




