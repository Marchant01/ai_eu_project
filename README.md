# AI Project Predictor

Welcome to the AI Project Predictor, a Streamlit-based application that uses machine learning to forecast the implementation status and estimated duration of public sector AI projects. This tool is designed to help policymakers, analysts, and project managers assess the viability of AI initiatives based on key project attributes.

The project uses and is based on a dataset by [Public Sector Tech Watch](https://interoperable-europe.ec.europa.eu/collection/public-sector-tech-watch) managed by the European Commission.

Streamlit application: [AI Project Predictor](ai-eu-project.streamlit.app)

## Features

### Predicts whether an AI project will be:
  - Implemented
  - Pilot
  - In development
  - Planned
  - Not in use

- Estimates time to implementation (in years)
- Interactive form for entering project details
- Uses pre-trained classification and reression models

### Requirements
- 3.8+
- pandas
- numpy
- joblib
- openpyxl
- sklearn