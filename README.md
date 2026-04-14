Foot-and-Mouth Disease (FMD) Risk Analysis in KwaZulu-Natal
Overview

This project presents a geospatial and machine learning-based analysis of Foot-and-Mouth Disease (FMD) risk across KwaZulu-Natal, South Africa.

The study integrates GIS-derived spatial variables with a Random Forest classification model to identify municipalities at elevated risk of FMD outbreaks.

Objectives
Map the spatial distribution of FMD outbreaks
Quantify key spatial risk factors
Develop a composite risk intensity index
Apply machine learning to predict outbreak occurrence
Methodology
Spatial Analysis

The following geospatial variables were derived:

Road density
Distance to the Disease Management Area (DMA)
Distance to protected areas at the wildlife–livestock interface
Risk Index

The FMD risk intensity index was defined as:

R_i = (1/3)(RD_i + D_DMA,i* + D_PA,i*)

Where:

RD_i = normalized road density
D_DMA,i* = normalized inverse distance to DMA
D_PA,i* = normalized inverse distance to protected areas

Higher values indicate greater relative outbreak risk.

Machine Learning Model

A Random Forest classifier was used to predict outbreak presence.

Features:

road_norm
dma_norm
protected_area_norm

Target:

outbreak_present
Project Structure

fmd-risk-analysis-kzn/
│
├── data/
│ └── processed/
│ └── kzn_fmd_layers.gpkg
├── qgis/
│ └── fmd_analysis.qgz
├── python/
│ ├── model.py
│ └── requirements.txt
├── outputs/
│ ├── maps/
│ └── figures/
├── docs/
│ └── report.pdf
├── README.md
└── LICENSE

GIS Data

Primary dataset:

data/processed/kzn_fmd_layers.gpkg

This GeoPackage includes:

FMD cases
Road network
Protected areas
Municipal boundaries
Derived spatial variables
Risk intensity layer
Outputs

Project outputs include:

Risk intensity maps
Feature importance plots
Spatial analysis outputs
Usage
Clone the repository
git clone https://github.com/benklass/fmd-risk-analysis-kzn.git

cd fmd-risk-analysis-kzn
Install dependencies
pip install -r python/requirements.txt
Run the model
python python/model.py
Open the GIS project
Open in QGIS:
qgis/fmd_analysis.qgz
Data Sources
South African FMD outbreak reports (2025)
OpenStreetMap data via Humanitarian Data Exchange (2026)
Administrative boundary datasets derived from HDX / OpenStreetMap
Notes
Spatial datasets derived from OpenStreetMap may differ slightly from official government datasets
This project is intended for analytical and research purposes
License

This project is licensed under the MIT License.

Geospatial datasets are subject to their respective third-party licenses.

Author

Benjamin Klass
Geospatial Data Analyst (GIS, Remote Sensing, Machine Learning)
Israel
