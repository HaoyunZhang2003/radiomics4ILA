from lungmask_master.lungmask import mask
import SimpleITK as sitk
import numpy as np
import nibabel as nib
import os
import pandas as pd
import matplotlib.pyplot as plt
import shutil
from xpinyin import Pinyin 
import xlsxwriter
import numpy as np
import nibabel as nib

excelpath=r"G:\CT\ipf2024\CT_one\wholelung.xlsx" #写入excel的准备
workbook = xlsxwriter.Workbook(excelpath)
worksheet = workbook.add_worksheet()
row,col=1,0


niiFile=r"G:\CT\ila\image" #该文件夹下有待分割的多个nii.gz文件
outputFile=r"G:\CT\ila\mask"

for nii in os.listdir(niiFile):
    print(nii)

    if not os.path.exists(os.path.join(outputFile,nii)): #如果已经处理好了就跳过

        input_image = sitk.ReadImage(os.path.join(niiFile,nii))
        segmentation = mask.apply(input_image)  # default model is U-net(R231)
        lung_mask = sitk.GetImageFromArray(segmentation)
        #注意这里将direction和origin对应
        lung_mask.SetDirection(input_image.GetDirection())
        lung_mask.SetOrigin(input_image.GetOrigin())
        lung_mask.SetSpacing(input_image.GetSpacing())
        sitk.WriteImage(lung_mask, os.path.join(outputFile,nii))
        #output_path = os.path.join(outputFile,nii)
        #nib.save(lung_mask, output_path)

        onemaskniipath=os.path.join(outputFile, nii)
        worksheet.write(row, col, onemaskniipath)
        row+=1


workbook.close()