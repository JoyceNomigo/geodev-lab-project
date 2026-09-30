# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
Author: <Joyce Nomigo>

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** EPSG:32632 

**Why this one:** AREA OF AMAC LGA is 1,475,000.625 SQM  , the study Area CRS is in metres and UTM zone 32N (EPSG:32632) .

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
|Ward Boundary | EPSG:4326 | EPSG:32632 | Reprojected |
| Waterway | EPSG:4326 | EPSG:32632 | Reprojected |
| Settlment Extent | EEPSG:4326 | EPSG:32632 |  Reprojected  |



## 2. Clipping to the study area

**AMAC Boundary:** [GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about)    and [Ward Boundary.gpkg](../../../GEODEV_LAB/Ward%20Boundary.gpkg)
- **Features before clipping:** 109
- **Features after clipping:** 12

 **Waterway:** QuickOSM PLugin in QGIS and [Waterway.gpkg](../../../GEODEV_LAB/DATA/processed/Waterway.gpkg)
- **Features before clipping:** Same
- **Features after clipping:** Same

 **Settlement Extent:** [GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) and [AMAC_Settlement_extent.gpkg](../../../GEODEV_LAB/DATA/processed/AMAC_Settlement_extent.gpkg)
- **Features before clipping:** 2546560
- **Features after clipping:** 4654



## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | yes | Reprojected|
| Are there nulls in the fields I need? | 0 | <what you did> |
| Are there duplicate features? |           No | <what you did> |
| Is the geometry valid? | yes | <what you did> |
| Does coverage span the whole study area? | yes  | |

## 4. Problems found, and what I did

**Wrong CRS** Data was in wrong CRS, and Fixed it by repojeceting to the right CRS.


## 5. The analysis-ready output

- **File:** [Ward Boundary.gpkg](../../../GEODEV_LAB/Ward%20Boundary.gpkg)
- **Format:** GeoPackage
- **CRS:** <EPSG:32632>
- **Features:** 12
- **Produced by:** python


- **File:**  [Waterway.gpkg](../../../GEODEV_LAB/DATA/processed/Waterway.gpkg)
- **Format:** GeoPackage
- **CRS:** <EPSG:32632>
- **Features:** 515
- **Produced by:** python

- **File:**  [GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) and [AMAC_Settlement_extent.gpkg](../../../GEODEV_LAB/DATA/processed/AMAC_Settlement_extent.gpkg)
- **Format:** GeoPackage
- **CRS:** <EPSG:32632>
- **Features:** 4654
- **Produced by:** python 

 **Spatial Analysis**
---

**Status:** Week 3 complete. First spatial analysis in Week 4.
