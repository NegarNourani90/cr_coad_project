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
```


Project Summary – Multimodal Metastasis Prediction (TCGA-COAD)

Repository: cr_coad_project

Objective: Predict metastasis in colorectal adenocarcinoma using clinical data, histopathology image embeddings, and their fusion.

📁 Data Workflow
Step	Notebook	Description	Output
01–05	Data preprocessing	Extracted and cleaned clinical + image data from TCGA and TCIA.	data/processed/
06	Image model training	Fine-tuned EfficientNetB0 on representative WSI slices.	results/images/baseline_image_model_clean_tf
07	Feature extraction	Exported 1280-dimensional embeddings per case.	data/processed/images/image_embeddings_1280.csv
08	Clinical model	Trained XGBoost on structured clinical features.	results/clinical/eval_metrics.csv
09	Fusion model	Combined clinical + image features, trained XGBoost fusion model.	results/fusion/fusion_model.pkl
10	Final report	Consolidated all metrics, visualized results, generated summary report.	results/report/final_summary.pdf

📈 Model Performance
Model	Accuracy	AUC	F1
Clinical (XGBoost)	0.976	0.930	0.870
Image-only	0.400	—	—
Clinical + Image Fusion	1.000	—	0.000

Interpretation:
Clinical data alone provides robust prediction.

Image-only model underperforms due to limited feature diversity.

Fusion model shows promising synergy but overfits small datasets.


📊 Visualization
results/report/final_summary.pdf includes:

Comparative bar chart of model metrics (Accuracy, AUC, F1).

Ranked performance summary and “Best Model per Metric” table.