🧠 Multimodal AI for Early Metastasis Detection in Colorectal Cancer

This research project investigates early prediction of metastasis in colorectal cancer using medical imaging and clinical data.
It integrates CT imaging (from TCIA) and clinical records (from TCGA COAD/READ) to build, explain, and evaluate multimodal AI models that predict metastasis risk.

🚀 Quick Start (GPU Training)

To train the EfficientNetB3 image model on a GPU machine:

conda env create -f environment_gpu.yml
conda activate crlm
jupyter nbconvert --to notebook --execute notebooks/06_train_image_model.ipynb


➡️ See the full GPU Training Guide
 for detailed setup and troubleshooting.

📂 Project Structure
Folder	Description
data/	Processed clinical and imaging data
notebooks/	Jupyter notebooks for preprocessing, training, and evaluation
results/	Saved model outputs (clinical, imaging, fusion)
scripts/	Utility scripts for automation or evaluation
docs/	Documentation and supporting files
📊 Datasets Used
Dataset	Description	Access
TCGA-COAD	Clinical data for colon adenocarcinoma patients	GDC Data Portal

TCGA-READ	Clinical data for rectum adenocarcinoma patients	GDC Data Portal

TCIA CRLM	CT imaging dataset of colorectal cancer patients with/without metastases	The Cancer Imaging Archive (TCIA)

(Optional) TCGA-COAD Imaging	CT or MRI subset of TCGA-COAD	TCIA

Note: All datasets are publicly available.
Genomic or private data requiring dbGaP authorization is not included.

🎯 Research Objectives

Develop deep learning models using medical imaging (CT)

Build machine learning models using clinical features

Design fusion models combining both modalities

Compare image-only, clinical-only, and multimodal models

Provide interpretability via Grad-CAM (for images) and SHAP (for clinical data)

⚙️ Environment & Requirements

Recommended setup:

Python 3.10

Conda (for environment management)

NVIDIA GPU with CUDA ≥ 11.2 (optional but strongly recommended)

Example setup (CPU):

conda create -n crlm python=3.10 -y  
conda activate crlm
pip install -r requirements.txt


For GPU setup, use:

conda env create -f environment_gpu.yml  
conda activate crlm

📘 Data Workflow Summary
Step	Notebook	Description	Output
01–05	Preprocessing	Extract and clean clinical + image data	data/processed/  
06	Image model training	Fine-tune EfficientNetB3 on CT slices	results/images/  
07	Feature extraction	Export embeddings for each image slice	data/processed/images/  
08	Clinical model	Train XGBoost on structured features	results/clinical/  
09	Fusion model	Combine embeddings + clinical features	results/fusion/  
10	Reporting	Summarize metrics and visualizations	results/report/  
📈 Model Performance (Preliminary)  
Model	Accuracy	AUC	F1  
Clinical (XGBoost)	0.976	0.930	0.870  
Image-only (EfficientNetB3)	0.400	—	—  
Fusion (Clinical + Image)	1.000	—	0.000  

Interpretation:

Clinical data alone provides strong predictive power.

Image-only model underperforms due to limited data volume.

Fusion model shows potential but overfits with small datasets.

📊 Visualization Outputs

results/report/final_summary.pdf includes:

Bar charts comparing model metrics (Accuracy, AUC, F1)

Ranked performance summary

“Best model per metric” table

👩‍🔬 Citation

If you use this project, please cite it as:

Nourani, N. et al., “Multimodal AI for Early Metastasis Detection in Colorectal Cancer,” 2025.

🧠 Contact

For questions, collaborations, or dataset details:
📧 nenonegar [at] gmail [dot] com