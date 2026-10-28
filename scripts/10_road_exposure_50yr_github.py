
from qgis.core import QgsProject
import processing

project = QgsProject.instance()


road_layers = project.mapLayersByName("Ottawa_Roads_Urban")
flood_layers = project.mapLayersByName("Ottawa_Flood_50yr_Urban")
if not road_layers or not flood_layers:
    raise RuntimeError("Required road or flood layer not found.")

roads = road_layers[0]
flood = flood_layers[0]


print("Total road features:", roads.featureCount())
print("Roads CRS:", roads.crs().authid())
print("Flood CRS:", flood.crs().authid())

result = processing.run(
    "native:clip",
    {
        "INPUT": roads,
        "OVERLAY": flood,
        "OUTPUT": "memory:"
    }
)

exposed_roads = result["OUTPUT"]

exposed_length_km = sum(
    feature.geometry().length()
    for feature in exposed_roads.getFeatures()
) / 1000

print("50-year exposed road length (km):",
      round(exposed_length_km, 2))

from pathlib import Path

output_path = (
    Path.home()
    / "Desktop"
    / "Ottawa_Flood_Project"
    / "Processed_Data_02"
    / "Roads_Exposed_50yr.gpkg"
)

if output_path.exists():
    print("Output already exists. No file overwritten.")
else:
    processing.run(
        "native:savefeatures",
        {
            "INPUT": exposed_roads,
            "OUTPUT": str(output_path)
        }
    )
    print("Saved:", output_path)
