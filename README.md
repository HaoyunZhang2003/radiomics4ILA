# radiomics4ILA
Complete Processing of Radiomics of ILA (Interstitial lung abnormalities)
Code availability for paper "Progression and mortality of interstitial lung abnormalities in patients with lung cancer resection: a single center report" (In submission)

The whole process can be roughly divided into four parts
1 Screening and quality control of raw data and conversion from dicom files to nii format
2 Segmentation of lung CT images using existing neural networks to obtain left and right lung regions
3 Image radiomics feature extraction after the doctor manually corrects the regions
4 Construct a machine learning model based on the image radiomics features

Automatic segmentation models for different subtypes of lesions in ILA are being developed, which is expected to greatly reduce the workload of manually applying lesion regions in step 3.
