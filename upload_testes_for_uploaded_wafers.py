import pandas as pd
import os
wafers_file='CMS_HGCAL_DB/wafers_parts/HGCal Pre-series sensors - 120um HD_AUG26.csv'
unzipped_parts_list_dir = 'CMS_HGCAL_DB/wafers_parts/wafers_parts_1'
# preseries_tested = pd.read_csv('CMS_HGCAL_DB/wafers_parts/HGCal Pre-series sensors - 120um HD_AUG26.csv')
# preseries_tested_scratchpad_id=preseries_tested['Scratch pad ID']
# for ind, row in preseries_tested.iterrows():
#     print(row['Scratch pad ID'])

def return_uploaded_wafers_list_from_spreadsheet(file):
    with open(wafers_file, 'r') as f:
        sensor_id_l=[]; Scratchpad_id_l=[]
        f_readlines = f.readlines()
        for line_ind, line in enumerate(f_readlines):
            if 'Delivery' in line:
                begin_data_ind = line_ind + 1
                for i in range(24):
                    sensor_id = f_readlines[begin_data_ind].split(',')[1]
                    sensor_id_l.append(sensor_id)
                    Scratchpad_id = f_readlines[begin_data_ind].split(',')[2]
                    Scratchpad_id_l.append(Scratchpad_id)
                    # print(Scratchpad_id)
                    begin_data_ind +=1
    return sensor_id_l, Scratchpad_id_l

def return_uploaded_wafers_list_from_zip_file(directory):
    Scratchpad_id_l=[]
    for item in os.listdir(directory):
        Scratchpad_id_l.append(item.split('.')[0])
    return Scratchpad_id_l

if __name__=='__main__':
    # sensor_id_l, Scratchpad_id_l = return_uploaded_wafers_list_from_spreadsheet(wafers_file)
    # print(sensor_id_l)
    # print('\n\n')
    # print(Scratchpad_id_l)
    Scratchpad_id_l=return_uploaded_wafers_list_from_zip_file(unzipped_parts_list_dir)
    print(sorted(Scratchpad_id_l))