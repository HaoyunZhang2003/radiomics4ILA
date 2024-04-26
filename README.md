# radiomics4ILA

This repository contains the complete processing pipeline for Radiomics Analysis of ILA (Interstitial Lung Abnormalities).

**Code availability for paper "Progression and mortality of interstitial lung abnormalities in patients with lung cancer resection: a single center report" (In submission)**

The entire process can be broadly divided into four parts:

1. **Screening and quality control of raw data and conversion from DICOM files to NII format**

    - **File**: `step1_dicom2nii.ipynb`
    
    We completed the batch acquisition of files of the highest resolution CT scans for each patient according to our center's data storage format. These files were then converted into NII.gz format for ease of subsequent processing. It's noteworthy that this step needs to be aligned with the storage format. The core transformation code is `dic2nii_sitk(path_read, path_save)`.

2. **Segmentation of lung CT images using existing neural networks to obtain left and right lung regions**

    - **File**: `step2_lung_region_segmentation.py`
    
    Prior to usage, the GitHub repository needs to be installed. Please refer to [JoHof/lungmask](https://github.com/JoHof/lungmask) for detailed instructions. This code implements segmentation of all NII.gz files in a folder to isolate lung regions. The default model used is U-net (R231), which is also employed in this paper.

3. **Image radiomics feature extraction after manual correction of regions by a clinician**

    - **File**: `step3_radiomics.py`
    
    Before usage, please install PyRadiomics as per the instructions on the [official website](https://pyradiomics.readthedocs.io/en/latest/installation.html). This step provides a sample input CSV file (`step3_sample_inputCSV.csv`) and a sample configuration file (`exampleCT.yaml`). The code accomplishes image radiomics feature extraction based on CT images and manually corrected lesion area masks.

4. **Construction of a machine learning model based on image radiomics features**

    - **File**: `step4_ML_Progression_model.ipynb`
    
    A prediction model was developed based on machine learning techniques. This included model selection, optimization, feedback of results, and generation of significant plots.
   The data are examples only, not thesis research data, and are retained only to demonstrate the work accomplished by the code block

 **Environment:**
- Python 3.9.13 (Guido van Rossum, Python Software Foundation)

**Versions of key Python packages:**
- PyRadiomics 3.0.1
- catboost 1.2
- scikit-learn 1.0.2
- numpy 1.21.6
- scipy 1.9.1

Work is underway to develop automatic segmentation models for different subtypes of lesions in ILA. This is expected to significantly reduce the workload associated with manually delineating lesion regions in step 3.
