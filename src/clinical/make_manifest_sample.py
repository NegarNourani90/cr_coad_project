import pandas as pd
import os

in_path = "data/raw/tcga/tcga_clinical_manifest.csv"
out_path = "data/processed/clinical/manifest_sample.csv"
os.makedirs(os.path.dirname(out_path), exist_ok=True)

use_cols = [
    "submitter_id","case_id","primary_diagnosis","gender",
    "age_at_diagnosis","tumor_stage","metastasis_status",
    "vital_status","days_to_death"
]

m = pd.read_csv(in_path, dtype=str)
keep = [c for c in use_cols if c in m.columns]
sample = m[keep].head(200).copy()   # small sample
sample.to_csv(out_path, index=False)
print(f"Saved sample -> {out_path}, shape={sample.shape}")
