
# Food Wastage Analytics — Colab + Streamlit Repo

## Structure
```
Food/
├─ app/                 # Streamlit app (DB + UI)
│  ├─ app.py
│  └─ Data/             # CSVs for app if you want
├─ notebooks/
│  └─ Food_Wastage_Colab.ipynb   # This notebook
├─ models/
│  
└─ README.md
```

## Using the Colab Notebook
1. Open Google Colab and upload `notebooks/Food_Wastage_Colab.ipynb`.
2. Upload 4 CSVs into Colab (paths default to `/content`):
   - `providers_data.csv`
   - `receivers_data.csv`
   - `food_listings_data.csv`
   - `claims_data.csv`
3. Run the notebook top-to-bottom.
4. It will export `best_model_pipeline.pkl` which you can save into `models/`.

## Streamlit App (optional, no ML)
- From the `Food/app/` folder, run:  
  `streamlit run app.py`
- App handles DB (SQLite), CRUD, and basic charts.

## GitHub Tips
- Keep `Data/` out of the repo or use small anonymized samples.
- Commit the notebook, app, and a small sample dataset schema (CSV headers) if needed.
- Add a clear project overview in README and screenshots from the notebook charts.
