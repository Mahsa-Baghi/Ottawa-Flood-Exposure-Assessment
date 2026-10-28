from qgis.core import QgsProject
project = QgsProject.instance()
buildings = project.mapLayersByName("Ottawa_Buildings_urban — Ottawa_Buildings_Urban")

flood = project.mapLayersByName("Ottawa_Flood_50yr_Urban")

print("Building layers found:", len(buildings))
print("Flood layers found:", len(flood))

if not buildings or not flood:
    raise RuntimeError(
        "Required building or flood layer was not found in QGIS."
    )

building_layer = buildings[0]
flood_layer = flood[0]
print("Total building footprints:", building_layer.featureCount())
print("Buildings CRS:", building_layer.crs().authid())
print("Flood CRS:", flood_layer.crs().authid())
import processing
result = processing.run(
"native:extractbylocation",
{
"INPUT": building_layer,
"PREDICATE": [0],
"INTERSECT": flood_layer,
"OUTPUT": "memory:"
}
)
exposed_buildings = result["OUTPUT"]
print("Exposed building footprints:", exposed_buildings.featureCount())
# Save exposed building footprints
from pathlib import Path

project_dir = Path.home() / "Desktop" / "Ottawa_Flood_Project"

output_path = (
    project_dir
    / "Processed_Data_02"
    / "Buildings_Exposed_50yr.gpkg"
)

if output_path.exists():
    print("Output already exists. No file overwritten.")
else: 
    processing.run(
    "native:savefeatures",
    {
         "INPUT": exposed_buildings,
         "OUTPUT": str(output_path)
    }
    )
    print("Saved:", output_path)
    