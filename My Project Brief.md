
# Project brief

**Week 1 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Joyce Nomigo

---

## 1. The question

> Which areas in AMAC lie within 200m of a watercourse?

## 2. Why this question

> AMAC has experienced severe flooding this year, worse than in recent years, including in areas with no previous history of flooding. Areas close to waterways are more likely to be exposed when water levels rise. This analysis identifies which settlements sit within 200m of a waterway, so that intending visitors, residents and planners can tell which areas are more likely to flood.

## 3. Study area

> Abuja Municipal Area Council (AMAC), Federal Capital Territory, Nigeria.

## 4. What I mean by the terms

- **Watercourse / waterway:** any linear water feature (river, stream, canal, drain) mapped in OpenStreetMap under the waterway tag and downloaded with QuickOSM. Unmapped streams are not included.
- **Within 200m:** any part of a settlement extent that falls inside a 200m buffer around a waterway. The buffer is measured in metres in a projected CRS (UTM zone 32N), not in degrees.
- **Settlement:** a built-up area from the GRID3 Settlement Extents v4.1 dataset.
- **Likely to flood:** I do not measure flooding. This project measures proximity to a waterway only. "Within 200m" means potentially exposed, not flooded.

## 5. Datasets

No link, no dataset. Every row below has a source you have opened yourself.

|   | Dataset | What it gives me | Source |
|---|---|---|---|
| 1 | AMAC boundary | The study area outline and the ward boundaries used to compare areas | [GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about) |
| 2 | Waterway | The line features that are buffered by 200m | QuickOSM plugin in QGIS (OpenStreetMap) |
| 3 | Settlement extent | The built-up areas that are classed as inside or outside the buffer | [GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) |

## 6. What "done" looks like

A map of AMAC showing settlement extent inside and outside the 200m waterway buffer, with ward boundaries, plus a table of the share of settlements within 200m for each ward. Anyone with QGIS and the three linked datasets should be able to reproduce it from the documented steps.

## 7. Known risks

**Incomplete settlement data.** Coverage looks uneven across wards, with large gaps in Gui, Jiwa, Orozo and Karshi 1. Wards with missing data will look safer than they are. I will state this on the map and in the results, and will not rank wards without that caveat.

**Incomplete waterway data.** OpenStreetMap may be missing smaller streams and drains, which would understate exposure. I will note this as a limitation and compare against satellite imagery where I can.

**Proximity is not flooding.** A 200m buffer ignores terrain, drainage and flood history. I will word results as "near waterways" and not "flooded", unless I add flood or elevation data.

---

**Status:** Week 1 complete. Data acquisition in Week 2, see
[DATA NOTES.md](https://github.com/JoyceNomigo/geodev-lab-project/blob/main/DATA%20NOTES.md) complete,week 3 Data preparation [Data preparation.md](https://github.com/JoyceNomigo/geodev-lab-project/blob/main/Data%20preparation.md) Complete, week 4 Month 1 Summary [MONTH 1 SUMMARY.md](https://github.com/JoyceNomigo/geodev-lab-project/blob/main/MONTH%201%20SUMMARY.md) Complete.
