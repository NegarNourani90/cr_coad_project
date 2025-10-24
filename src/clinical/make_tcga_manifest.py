import pandas as pd
import glob, os
RAW_CLIN_DIR = "data/raw/clinical"   # put your COAD/READ TSVs here
OUT_DIR = "data/raw/tcga"            # outputs stay local (ignored by git)
os.makedirs(OUT_DIR, exist_ok=True)

files = glob.glob(os.path.join(RAW_CLIN_DIR, "*.tsv"))
if not files:
    raise SystemExit(f"No .tsv files found in {RAW_CLIN_DIR}. Put COAD/READ TSVs there.")

dfs = []
for f in files:
    df = pd.read_csv(f, sep="\t", dtype=str)
    if "cases.submitter_id" in df.columns:
        df = df.rename(columns={"cases.submitter_id":"submitter_id"})
    if "cases.case_id" in df.columns:
        df = df.rename(columns={"cases.case_id":"case_id"})
    dfs.append(df)

big = pd.concat(dfs, axis=0, ignore_index=True, sort=False)

id_col = "case_id" if "case_id" in big.columns else ("submitter_id" if "submitter_id" in big.columns else None)
if id_col is None:
    raise SystemExit("No case_id or submitter_id column present in the TSVs.")

big = big.groupby(id_col, as_index=False).agg(lambda s: s.dropna().iloc[0] if s.dropna().shape[0] else pd.NA)

def derive_mets(row):
    for col in ["diagnoses.ajcc_pathologic_m","diagnoses.ajcc_clinical_m","diagnoses.ajcc_m_pathologic","diagnoses.ajcc_m"]:
        if col in big.columns:
            v = row.get(col)
            if pd.notna(v):
                u = str(v).strip().upper()
                if "M1" in u or u == "1":
                    return 1
                if "M0" in u or u == "0":
                    return 0
    for col in ["diagnoses.ajcc_pathologic_stage","diagnoses.ajcc_clinical_stage","diagnoses.uicc_pathologic_stage","diagnoses.uicc_clinical_stage"]:
        if col in big.columns:
            v = row.get(col)
            if pd.notna(v):
                u = str(v).upper()
                if "IV" in u or "STAGE IV" in u or u.strip() == "4":
                    return 1
                if any(x in u for x in ["I","II","III","1","2","3"]):
                    return 0
    if "diagnoses.metastasis_at_diagnosis" in big.columns:
        v = row.get("diagnoses.metastasis_at_diagnosis")
        if pd.notna(v):
            u = str(v).lower()
            if any(k in u for k in ["yes","present","1","true"]):
                return 1
            if any(k in u for k in ["no","absent","0","false"]):
                return 0
    return pd.NA

big["metastasis_status"] = big.apply(derive_mets, axis=1)

def first_present(cols):
    for c in cols:
        if c in big.columns:
            return big[c]
    return pd.Series([pd.NA]*len(big))

manifest = pd.DataFrame({
    "submitter_id": first_present(["submitter_id"]),
    "case_id": first_present(["case_id"]),
    "primary_diagnosis": first_present(["diagnoses.primary_diagnosis","diagnoses.primary_disease"]),
    "gender": first_present(["demographic.gender","demographic.sex"]),
    "age_at_diagnosis": first_present(["diagnoses.age_at_diagnosis","demographic.age_at_index"]),
    "tumor_stage": first_present(["diagnoses.ajcc_pathologic_stage","diagnoses.ajcc_clinical_stage","diagnoses.uicc_pathologic_stage"]),
    "metastasis_status": big["metastasis_status"],
    "vital_status": first_present(["demographic.vital_status"]),
    "days_to_death": first_present(["demographic.days_to_death","diagnoses.days_to_death"]),
})

full_csv = os.path.join(OUT_DIR, "tcga_coad_read_clinical.csv")
manifest_csv = os.path.join(OUT_DIR, "tcga_clinical_manifest.csv")
big.to_csv(full_csv, index=False)
manifest.to_csv(manifest_csv, index=False)
print("Saved:", full_csv)
print("Saved:", manifest_csv)
