# Data Sources

This file documents all datasets, geospatial layers, outbreak records, machine learning inputs, and derived outputs used in the **Foot-and-Mouth Disease (FMD) Risk Analysis in KwaZulu-Natal** project.

---

# 1. Study Area Boundary

## Area of Interest (AOI)

The study area represents **KwaZulu-Natal (KZN)**, a province located in eastern South Africa.

Used for:

- clipping national datasets
- municipal-level analysis
- outbreak mapping
- risk modelling
- map centering

---

# 2. Administrative Boundaries

## South Africa Administrative Boundaries

**Source:**

Humanitarian OpenStreetMap Team via Humanitarian Data Exchange (HDX)

Used to extract KwaZulu-Natal provincial boundaries and local municipalities.

### Files Used

- zaf_admin_boundaries.gdb
- kzn_boundary
- kzn_municipalities

### Format

- File Geodatabase (.gdb)
- GeoPackage (.gpkg)

### Derived Uses

- municipality polygons
- municipality centroids
- zonal analysis
- thematic mapping

---

# 3. Road Network Data

## KwaZulu-Natal Roads

**Source:**

OpenStreetMap export via Humanitarian Data Exchange

Used to model accessibility, livestock movement corridors, and human-mediated transmission pathways.

### Geometry Type

- Line features

### Derived Output

- road density by municipality
- road proximity relationships

---

# 4. Protected Areas

## Wildlife-Livestock Interface Zones

Protected areas associated with potential wildlife reservoirs of FMD were digitized / extracted for analysis.

### Areas Used

- Hluhluwe-iMfolozi Park
- iSimangaliso Wetland Park

### Purpose

Used to model proximity-based FMD spillover risk.

---

# 5. Disease Management Area (DMA)

## FMD Control Zone

South African Disease Management Area (DMA) boundaries were used to represent official FMD containment zones.

### Purpose

Used to calculate municipal distance from the regulated control area.

---

# 6. FMD Outbreak Data

## KwaZulu-Natal FMD Cases

Compiled from South African national outbreak reports.

### Source

Directorate: Animal Health  
South Africa Government

### Attributes Used

- outbreak location
- outbreak status
- municipality
- date (where available)

### Geometry Type

- Point locations

Used for:

- outbreak visualization
- hotspot analysis
- supervised learning labels

---

# 7. Derived GIS Layers

The following analytical layers were generated in QGIS:

## Municipality Centroids

Geographic centers of local municipalities.

## Road Density

Total road length divided by municipal area.

## DMA Distance

Distance from municipalities to Disease Management Area.

## Protected Area Distance

Distance from municipalities to Hluhluwe-iMfolozi and iSimangaliso.

## Risk Intensity Index

Composite normalized risk surface based on:

- road density
- inverse DMA distance
- inverse protected area distance

Defined as:

R_i = (1/3)(RD_i + D_DMA,i* + D_PA,i*)

---

# 8. Machine Learning Inputs

## Dataset File

KZN_FMD_dataset.csv

## Predictor Variables

- road_norm
- dma_norm
- protected_area_norm

## Target Variable

- outbreak_present

### Sampling Split

- 70% training
- 30% testing

---

# 9. Classification Model

## Random Forest

Implemented in Python using scikit-learn.

### Parameters

- n_estimators = 100
- random_state = 42

### Outputs

- classification report
- feature importance chart

---

# 10. Exported Outputs

Generated outputs include:

## Maps

- KZN_FMD_Cases.png
- KZN_Risk_Intensity.png

## Figures

- feature_importance.png

## Documents

- report.pdf
- project_poster.pdf
- project_poster.png

## GIS Project

- fmd_analysis.qgz

## GeoPackage

- kzn_fmd_layers.gpkg

---

# 11. Software Environment

## Platforms Used

- QGIS
- Python
- GitHub

## Python Libraries

- pandas
- scikit-learn
- matplotlib
- numpy

---

# 12. Notes

- OpenStreetMap-derived datasets may differ slightly from official government cartography.
- Outbreak data quality depends on public reporting completeness.
- Risk index values represent relative susceptibility, not confirmed outbreak probability.
- Wildlife proximity is used as a proxy indicator rather than direct infection confirmation.

---

# 13. Citation Suggestions

Humanitarian OpenStreetMap Team (HDX)  
South African Directorate: Animal Health  
OpenStreetMap  
QGIS Development Team  
scikit-learn Documentation

---