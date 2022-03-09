import pandas as pd
from pandas import DataFrame
from csv import reader

##location setting

labs_link = 'gnlabs/calc_ap/results/' # gnlabs folder
origin_link = 'data/kitti/' # Ground Truth folder
open_iou_csv = 'iou_value.csv' #saved iou csv file
dir_origin = 'training/label_2/' #Ground Truth value txt folder

# HShin
dir_pred = 'submission/' # predict value txt folder,  if mvx net = submission/pts_bbox/
# dir_pred = 'submission/pts_bbox/' # predict value txt folder,  if mvx net = submission/pts_bbox/

list_up_file = 'ImageSets/val.txt' #Ground Truth file list txt file

save_result_name = 'gnlabs/calc_ap/results/merged_results.csv' #where will save the merged csv file

### Start get IOU value
with open(labs_link+open_iou_csv, 'r') as csv_file: #get iou value 
    csv_reader = reader(csv_file)
    iou_value = list(csv_reader)

#ex) iou_value = [['[0.38255972 0.        ]'], ['[0.         0.70822877]'], ['[0.]']]
proc_process = [] 
for p in range(len(iou_value)):
    p_list = []
    for q in range(len(iou_value[p])):
        proc = iou_value[p][q]
        proc_strip = proc.strip("[""]"" ")
        proc_strip = proc_strip.replace("\n", "")
        proc_strip = proc_strip.replace("        ", "")
        proc_strip = proc_strip.replace("0.", ",0.")
        proc_split = proc_strip.split(",")
        if proc_split[0] == '':
             del proc_split[0]
        for proc_num in range(len(proc_split)):
            try:
                proc_split[proc_num] = float(proc_split[proc_num])
            except(ValueError) as e:
                iou_list = []
                for iou_str in proc_split[proc_num].split():
                    iou_num = float(iou_str)
                    iou_list.append(iou_num)
                    proc_split[proc_num] = iou_num
        p_list.append(proc_split)
    proc_process.append(p_list)
# proc_process = list format of iou_value.
#rest problem. it can't get "void" result.
### Finish get iou value



### Start get Files
#get annotation files, predict file


list_up = pd.read_csv(origin_link+list_up_file, names=['list'], converters={'list': str}) #read list file
list_up_data = []

for i in range(len(list_up)):
    list_up_data.append(list_up.loc[i, 'list']) #ready to get test file

origin_data = []
pred_data = []
for j in list_up_data:
    origin_data.append(origin_link+dir_origin + j + ".txt")
    pred_data.append(labs_link+dir_pred + j + ".txt") 
### Finish get Files


comp = pd.DataFrame({'ID':[],'origin_type':[], 'pred_type':[],'iou':[],'score':[], 'index':[]})
### Start Merge
for Fi in range(len(list_up)):
    #data config
    origin = pd.read_csv(origin_data[Fi], sep=' ', names = ['origin_type', 'truncated', 'occluded', 'alpha', 'bbox1', 'bbox2','bbox3','bbox4',
                       "dimensions1","dimensions2","dimensions3", "location1","location2","location3", "rotation_y"])
    pred = pd.read_csv(pred_data[Fi], sep=' ' ,names = ['pred_type', 'truncated', 'occluded', 'alpha', 'bbox1', 'bbox2','bbox3','bbox4',
                       "dimensions1","dimensions2","dimensions3", "location1","location2","location3", "rotation_y", "score"])       
    proc_data = proc_process[Fi]
    #--


    idx_col = []
    iou_loc_list = []
    max_iou_list = []
    ID_list = []

    for k in range(len(origin)):
        idx_col.append(k) #index number
        ID_list.append(list_up_data[Fi])

    for LL in range(len(proc_data)):
        try:
            max_iou = max(proc_data[LL])
            iou_loc = proc_data[LL].index(max_iou)
            iou_loc_list.append(iou_loc)
            max_iou_list.append(max_iou) #iou value maximum
        except ValueError:
            max_iou = 0
            iou_loc = 0
            iou_loc_list.append(iou_loc)
            max_iou_list.append(max_iou) #error handle

    origin_pro = pd.DataFrame({})
    pred_pro = pd.DataFrame({'index':[], 'iou':[], 'pred_type':[]})

    origin_pro['index'] = idx_col
    origin_pro['origin_type'] = origin['origin_type']
    origin_pro['ID'] = ID_list

    try:
        pred_pro['index'] = iou_loc_list
        pred_pro['iou'] = max_iou_list
        pred_pro['pred_type'] = pred['pred_type'] 
        pred_pro['score']= pred['score']
    finally:
        pass

    step = pd.merge(origin_pro, pred_pro, how='outer')
    if len(origin) == 0:
        step['ID'].fillna(list_up_data[Fi], inplace=True)
    comp = pd.concat([comp, step], axis=0)

comp.to_csv(save_result_name, index=False)
print("Result saved at "+save_result_name)
