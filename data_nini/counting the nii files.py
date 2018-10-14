import os
import os.path
path = '/Users/xinwang/Downloads/TRAINING'

nii_num = 0
txt_num = 0
list_size = []
list_name = []

for parentdir, dirname, filenames in os.walk(path):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.nii':
            nii_num = nii_num + 1
        if os.path.splitext(filename)[1] == '.txt':
            txt_num = txt_num + 1   
print("in all folders, the nii formats files are: ",nii_num,"items")
print("in all folders, the nii formats files are: ",txt_num,"items")

