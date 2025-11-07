==========================================
🧬 CR/COAD Project — Image Dataset Setup
==========================================

The original CT image slices used for model training are too large to store directly on GitHub.
Please follow the steps below to download and prepare the dataset before running the image model.

------------------------------------------
📁 Dataset Location
------------------------------------------
Download the ZIP file containing all image slices from the following link:

👉 https://drive.google.com/file/d/1z44obdP7Y7taV5opAwbud2iEqCKHshXn/view?usp=drive_link

------------------------------------------
📦 Step-by-Step Instructions
------------------------------------------

1️⃣ Download the ZIP file mentioned above.
2️⃣ Extract (unzip) it into this exact folder structure inside your project:

   cr_coad_project/
   └── data/
       └── processed/
           └── images/
               └── all_slices/
                   ├── slice_0001.png
                   ├── slice_0002.png
                   ├── ...
                   └── slice_NNNN.png

3️⃣ After extraction, verify that you can see the image files here:
   data/processed/images/all_slices/

4️⃣ Once confirmed, you can proceed to run:
   notebooks/06_train_image_model.ipynb

------------------------------------------
🧠 Notes
------------------------------------------
- The dataset contains preprocessed CT image slices from TCIA and TCGA cases.
- These files are used to train the model for metastasis prediction.
- The dataset must match the filenames and structure expected in:
  `data/processed/images/all_index.csv`
- No manual renaming or reorganization is required.

If you encounter a `FileNotFoundError` for any image path, double-check that
you have extracted the dataset into the correct directory.

------------------------------------------
📧 Contact
------------------------------------------
If you have trouble downloading or verifying the dataset,
contact Negar Nourani (project maintainer) for access to the latest copy.

==========================================
