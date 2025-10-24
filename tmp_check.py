import pandas as pd
m = pd.read_csv("data/raw/tcga/tcga_clinical_manifest.csv")
print(m.head(3))
print(m["metastasis_status"].value_counts(dropna=False))
