# src/images/preprocess_dicom.py
import os, re, sys
import numpy as np
import SimpleITK as sitk
from pathlib import Path
from PIL import Image

# Look here for all manifests/collections
RAW_DIR = r"C:/Users/Negar/Desktop/paper_results/Myself/cr_coad_project/data/raw/tcia"
OUT_DIR = "data/processed/images/patches"

# skip folders that are likely non-image objects
SKIP_PATTERNS = re.compile(r"(SEGMENTATION|RTSTRUCT|RTDOSE|RADIATION|STRUCT)", re.I)

def natural_key(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]

def save_slices(arr, out_dir, patient_id, series_id):
    out = Path(out_dir) / patient_id / series_id
    out.mkdir(parents=True, exist_ok=True)
    for i in range(arr.shape[0]):
        sl = (arr[i] * 255.0).clip(0,255).astype(np.uint8)
        Image.fromarray(sl).save(out / f"slice_{i:04d}.png")

def try_series(dir_path):
    # Ignore obvious non-image leaf folders
    leaf = Path(dir_path).name
    if SKIP_PATTERNS.search(leaf):
        return None
    try:
        sids = sitk.ImageSeriesReader.GetGDCMSeriesIDs(dir_path)
    except Exception:
        return None
    if not sids:
        return None

    ok = 0
    for sid in sids:
        try:
            files = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(dir_path, sid)
            if len(files) < 10:   # tiny series tend to be SEG/SCOUT; skip
                continue
            files = sorted(files, key=natural_key)
            reader = sitk.ImageSeriesReader()
            reader.SetFileNames(files)
            img = reader.Execute()
            arr = sitk.GetArrayFromImage(img).astype(np.float32)  # [z,y,x]
            if arr.ndim != 3 or arr.shape[0] < 4:
                continue  # skip 2D or very thin series
            # CT HU -> clip/normalize
            arr = np.clip(arr, -100, 400)
            arr = (arr + 100.0) / 500.0

            # infer IDs from hierarchy: .../<Collection>/<Patient>/<Study>/<Series>/
            p = Path(dir_path)
            def infer_patient_id(path: Path) -> str:
                # Look up the path for a folder that looks like CRLM-CT-#### or similar
                for ancestor in [path] + list(path.parents):
                    name = ancestor.name
                    if name.startswith("CRLM-"):  # CRLM collection pattern
                        return name
                # Fallback: use the folder 2 levels up from the series (usually the patient)
                try:
                    return path.parents[1].name
                except Exception:
                    return path.name

            patient_id = infer_patient_id(Path(dir_path))
            series_id = sid.replace(":", "_")

            save_slices(arr, OUT_DIR, patient_id, series_id)
            ok += 1
            print(f"OK  patient={patient_id} series={series_id} slices={arr.shape[0]}")
        except Exception as e:
            # just skip bad series
            # print(f"SKIP {dir_path} sid={sid}: {e}")
            pass
    return ok if ok > 0 else None

def main(limit=None):
    processed = 0
    for root, dirs, files in os.walk(RAW_DIR):
        # work only in dirs that actually contain DICOM files
        if any(f.lower().endswith(".dcm") for f in files):
            r = try_series(root)
            if r:
                processed += r
                if limit and processed >= limit:
                    break
    print(f"Done. Processed {processed} series.")

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    main(limit=n)
