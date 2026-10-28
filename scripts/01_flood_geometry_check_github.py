import processing
from qgis.core import QgsVectorLayer

from pathlib import Path

project_dir = Path.home() / "Desktop" / "Ottawa_Flood_Project"
input_path = project_dir / "Raw_Data_01" / "Ottawa_Flood_50yr.gpkg"

flood50 = QgsVectorLayer(str(input_path, "Ottawa_Flood_50yr", "ogr")

if not flood50.isValid():
    raise RuntimeError(f"Failed to load flood layer: {input_path}")

print("Flood layer loaded successfully.")

total_features = flood50.featureCount()
invalid_before = sum(1 for feature in flood50.getFeatures() if not feature.geometry().isGeosValid())
print("Total features:", total_features)
print("Invalid geometries before fixing:", invalid_before)
# Fix invalid geometries
result = processing.run(
"native:fixgeometries",
{
"INPUT": flood50,
"METHOD": 1,
"OUTPUT": "memory:"
}
)
fixed_flood50 = result["OUTPUT"]
# Check geometries after fixing
total_after = fixed_flood50.featureCount()
invalid_after = sum(
1 for feature in fixed_flood50.getFeatures() 
if not feature.geometry().isGeosValid()
)
print("Total features after fixing:", total_after)
print("Invalid geometries after fixing:", invalid_after)
# Verify the results
if total_after != total_features or invalid_after != 0:
 raise RuntimeError("Geometry quality check failed.")
# Save the corrected flood layer
from pathlib import Path
output_path = Path.home() / "Desktop" / "Ottawa_Flood_Project" / "Processed_Data_02" / "Ottawa_Flood_50yr_Fixed.gpkg"
if output_path.exists():
 print("Output already exists. No file overwritten.")
else:
    processing.run(
    "native:savefeatures",
    {
    "INPUT": fixed_flood50,
    "OUTPUT": str(output_path)
    }
    )
    print("Saved:", output_path)