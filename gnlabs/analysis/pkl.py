import pickle

file_path = "./gnlabs/analysis/kitti_dbinfos_train.pkl"

data = pickle.load(open(file_path, "rb"))

ped = data['Pedestrian'][0]
print(ped.keys())
# print(ped['image_idx'], ped['box3d_lidar'])