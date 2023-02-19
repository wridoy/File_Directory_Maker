#!/usr/bin/env python
# coding: utf-8

# pyinstaller --onefile File_Directory_Maker_V2.py

# In[150]:


# =============================================================================
# =============================================================================
# # Create a File Directory Maker containing all files within the current working directory
# =============================================================================
# =============================================================================

# to execute--------pip install pyinstaller
#----------pyinstaller file_directory_maker.py -F
import os
from csv import DictWriter
import datetime

# file_dict={"File name":0, "File Type":0, "File Location":0, "Last Modified":0}

# l = os.walk(os.getcwd()) # walk is used for deep searching through files, folders, subfolders
                            # on current working directory
                #returns an iterator containing current_directory,folder_name & file_name
# wrk_dir=input("Enter your working directory location")
# wrk_dir = r"G:\WRIDOY\Python_prac\EXE Maker"
wrk_dir = os.getcwd()
l = os.walk(wrk_dir)

all_file_name=[]
all_file_location=[]
file_type=[]

for current_path,folder_name,file_name in l:
       all_file_name += file_name
       # joining current path with file name to create file path
       all_file_location+= [os.path.join(current_path,file) for file in file_name] 
       # splitting file name to get file type
       file_type+= [os.path.splitext(file)[1].lower() for file in file_name]
#        print(all_file_location)

def get_last_modified_time (file_location_list):
    last_modified_list=[]
    for f in file_location_list:
        t=os.path.getmtime(f) # this returns unix format time
        p=datetime.datetime.fromtimestamp(t) # this converts unix to datetime object(readable)
        last_modified_list.append(p)
    return last_modified_list

# file_dict["File name"]=all_file_name
# file_dict["File Location"]=all_file_location
# file_dict["File Type"]=file_type
# file_dict["Last Modified"]= get_last_modified_time(all_file_location)
last_modified = get_last_modified_time(all_file_location)
print(get_last_modified_time(all_file_location))

# df=pd.DataFrame(file_dict)

# sorting dataframe & sorting will be done according to the selected column order

# sorted_df=df.sort_values(by=["File Type","File name","Last Modified"]) 

# sorted_df.to_csv('File Directory.csv',index=False)
# 
all_file_location_updt=[]

for i in all_file_location:
    a = i.split('\\')
    del a[-1]
    all_file_location_updt.append('\\'.join(a))

combined_list = list(zip(all_file_name, file_type, all_file_location_updt, last_modified))

combined=[{"File name":i[0], "File Type":i[1], "File Location":i[2], "Last Modified":i[3]} for i in combined_list]
combined= sorted(combined,key=lambda x :(x["File Type"],x["File name"],x["Last Modified"]))

with open('File Directory.csv','w',newline='') as wf:
    csv_writer = DictWriter(wf,fieldnames=["File name", "File Type", "File Location", "Last Modified"])
    csv_writer.writeheader()
    csv_writer.writerows(combined)

