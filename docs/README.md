# Multimodal AI for Early Metastasis Detection in Colorectal Cancer

This research project investigates the early prediction of metastasis in colorectal cancer using **medical imaging** and **clinical data**.  
The study integrates CT imaging (from TCIA) and clinical records (from TCGA COAD/READ) to build and evaluate model architectures that combine image and clinical features for metastasis risk prediction.

---

## 📂 Project Structure


---

## 📊 Datasets Used

This project uses **publicly available datasets**:

| Dataset | Description | Access |
|--------|--------------|--------|
| **TCGA-COAD** | Clinical data for colon adenocarcinoma patients | GDC Data Portal |
| **TCGA-READ** | Clinical data for rectum adenocarcinoma patients | GDC Data Portal |
| **TCIA CRLM** (Colorectal Liver Metastases) | CT imaging dataset of colorectal cancer patients with/without metastases | The Cancer Imaging Archive (TCIA) |
| *(If available)* TCGA-COAD Imaging (TCIA) | CT or MRI scans for a subset of TCGA-COAD patients | The Cancer Imaging Archive (TCIA) |

> **Note:** All datasets are used under their respective public access policies.  
> Genomic data requiring dbGaP authorization is **not included in this project**.

---

## 🧠 Research Objectives

- Develop deep learning models using **medical imaging** (CT)
- Develop machine learning models using **clinical features**
- Build and evaluate **fusion models** that combine both modalities
- Compare image-only vs clinical-only vs multimodal performance
- Provide explainability using **Grad-CAM** (images) and **SHAP** (clinical)

---

## ⚙️ Environment & Requirements

Recommended environment:

- Python 3.10  
- Conda or virtual environment  
- GPU (optional but recommended)  

Example environment setup:

```bash
conda create -n crlm python=3.10 -y
conda activate crlm
pip install -r requirements.txt

