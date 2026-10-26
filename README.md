# Ottawa-Flood-Exposure-Assessment
GIS-based assessment of urban building and road exposure to flood hazards in Ottawa using QGIS and Python.
# Ottawa Urban Flood Exposure Assessment

## Project Overview
This independent GIS portfolio project assesses urban building and road exposure to mapped flood hazards in Ottawa, Ontario, Canada.

The analysis examines three flood scenarios: 50-year, 100-year, and 350-year events.

## Objectives
- Identify building footprints intersecting flood extents.
- Calculate the length of road segments within flood extents.
- Compare infrastructure exposure across flood scenarios.
- Produce professional cartographic outputs.

## Tools and Technologies
- QGIS
- Python (PyQGIS)
- GeoPackage
- Spatial analysis and geoprocessing
- NAD83 / UTM Zone 18N (EPSG:26918)

## Methodology
1. Collect and prepare spatial datasets.
2. Validate and repair flood polygon geometries.
3. Clip flood extents to Ottawa's urban study boundary.
4. Identify exposed building footprints using spatial intersection.
5. Clip road segments to flood polygons and calculate their lengths.
6. Create maps to communicate the results.

## Results

| Flood Scenario | Exposed Building Footprints | Exposed Road Length |
|---|---:|---:|
| 50-Year | 876 | 9.71 km |
| 100-Year | 1,521 | 17.09 km |
| 350-Year | 607 | 7.01 km |

## Important Notes
The results represent spatial exposure to mapped flood hazards, not confirmed infrastructure damage.

Flood scenario datasets may differ in geographic coverage. The 350-year scenario has known source-coverage limitations, so comparisons require caution.

## Project Status
The 100-year flood exposure map has been completed. Additional scenario maps and portfolio documentation are in progress.

## Author
Mahsa Baghi
GIS Analyst | Remote Sensing Specialist
