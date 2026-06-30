# Student Management & Analytics System

A modular Python command-line application designed to simulate operational data ingestion, structured storage, and automated business intelligence (BI) performance reporting workflows.

## 🚀 Key Architectural Features

- **Data Ingestion & Integrity (`app.py`):** Interactive interface featuring automatic primary key validation (prevents duplicate IDs) and text normalization (`.upper()`).
- **Data Persistence Layer:** Automatically formats, writes, and serializes structural records into a standardized `students.csv` flat-file schema.
- **Automated Analytics Engine (`analytics.py`):** An independent data pipeline script that reads the CSV dataset to calculate core descriptive KPIs:
  - Total student base tracking metrics.
  - Overall average attendance rate (featuring crash-resilient zero-division checks).
  - Categorical grade frequency distribution tracking.
  - Operational Risk Assessment filtering to flag at-risk students (<75% attendance) for administrative interventions.
- **Data Security:** Implemented a `.gitignore` layer to secure local production datasets from leaking into version control histories.

## 📊 Technical Stack
- **Language:** Python 3.x
- **Storage Format:** Flat CSV (Comma Separated Values)
- **Version Control System:** Git & GitHub

## 🔧 How to Execute the Project

1. **Run the Operational Data Entry Application:**
   ```bash
   python app.py
