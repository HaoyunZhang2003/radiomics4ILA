# radiomics4ILA
Complete Processing of Radiomics of ILA (Interstitial lung abnormalities)
Code availability for paper "Progression and mortality of interstitial lung abnormalities in patients with lung cancer resection: a single center report" (In submission)

The whole process can be roughly divided into four parts
1 Screening and quality control of raw data and conversion from dicom files to nii format
  File:step1_dicom2nii.ipynb
  According to the data storage format of our center, we completed the batch acquisition of the files of the highest resolution CT of each patient and converted them into nii.gz files for easy subsequent processing.
  It's worth noting that this needs to be done in conjunction with the storage format. The core transformation code is dic2nii_sitk(path_read, path_save).
  
  

2 Segmentation of lung CT images using existing neural networks to obtain left and right lung regions
 You need to install the github repository before using it, refer to https://github.com/JoHof/lungmask for more details
 File：step2_lung_region_segmentation.py
 This code implements the segmentation of all nii.gz files in a folder, for the lung region. The default model is U-net (R231), which is also used in this paper.
 
  

  
3 Image radiomics feature extraction after the doctor manually corrects the regions
  Before using, please install pyradiomics according to the official website: https://pyradiomics.readthedocs.io/en/latest/installation.html
  Provides a sample inputCSV:step3_sample_inputCSV.csv, and a sample configuration file: exampleCT.yaml
  File：step3_radiomics.py
  The code accomplishes image radiomics feature extraction based on CT images and lesion area masks



4 Construct a machine learning model based on the image radiomics features
  File: step4_ML_Progression_model.ipynb
  A prediction model was built based on machine learning, which included model selection, model optimization, feedback of results and output of significant plots





Automatic segmentation models for different subtypes of lesions in ILA are being developed, which is expected to greatly reduce the workload of manually applying lesion regions in step 3.
