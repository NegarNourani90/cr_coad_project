import os, csv, pydicom

ROOT = r"C:\Users\Negar\Desktop\paper_results\Myself\cr_coad_project\data\raw\tcia"
OUT  = r"C:\Users\Negar\Desktop\paper_results\Myself\cr_coad_project\data\processed\images\index_tcia.csv"

os.makedirs(os.path.dirname(OUT), exist_ok=True)

rows = []
for r, d, f in os.walk(ROOT):
    dcm_files = [x for x in f if x.lower().endswith(".dcm")]
    if not dcm_files:
        continue
    # peek first file in this folder
    fp = os.path.join(r, dcm_files[0])
    try:
        ds = pydicom.dcmread(fp, stop_before_pixels=True, force=True)
    except Exception as e:
        ds = None
    row = {
        "dir": r,
        "num_dcm": len(dcm_files),
        "PatientID": getattr(ds, "PatientID", None) if ds else None,
        "StudyInstanceUID": getattr(ds, "StudyInstanceUID", None) if ds else None,
        "SeriesInstanceUID": getattr(ds, "SeriesInstanceUID", None) if ds else None,
        "Modality": getattr(ds, "Modality", None) if ds else None,
        "BodyPartExamined": getattr(ds, "BodyPartExamined", None) if ds else None,
        "StudyDate": getattr(ds, "StudyDate", None) if ds else None,
        "SeriesDescription": getattr(ds, "SeriesDescription", None) if ds else None,
    }
    rows.append(row)

# de-duplicate per SeriesInstanceUID (keep the folder with most files)
by_series = {}
for r in rows:
    k = r["SeriesInstanceUID"] or r["dir"]
    if k not in by_series or r["num_dcm"] > by_series[k]["num_dcm"]:
        by_series[k] = r

cols = ["PatientID","StudyInstanceUID","SeriesInstanceUID","Modality",
        "BodyPartExamined","StudyDate","SeriesDescription","num_dcm","dir"]

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in by_series.values():
        w.writerow({c: r.get(c) for c in cols})

print(f"wrote {OUT} with {len(by_series)} series")
