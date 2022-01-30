# common

1. dataset preparation

```bash
python tools/create_data.py kitti --root-path /data/kitti --out-dir /data/kitti --extra-tag kitti
```

2. browse

```bash
python tools/misc/browse_dataset.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py --task multi_modality-det --output-dir /data/kitti/results/ --online
```

3. visualization
- using predicted results
```bash
./tools/dist_test.sh configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py work_dir/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class_20200621_003904-10140f2d.pth 8 --out /data/kitti/pred_result.pkl --eval mAP
```
```bash
python tools/misc/visualize_results.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py --result /data/kitti/pred_result.pkl --show-dir /data/kitti/show_dir/
```
- using model
```bash
python tools/test.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth --show --show-dir /data/kitti/show_dir/
```

# model development (3 classes and multi gpu)

## SECOND

### train
```bash
wget https://download.openmmlab.com/mmdetection3d/v0.1.0_models/second/hv_second_secfpn_6x8_80e_kitti-3d-3class/hv_second_secfpn_6x8_80e_kitti-3d-3class_20200620_230238-9208083a.pth -P ./checkpoints/
```
```bash
./tools/dist_train.sh configs/second/hv_second_secfpn_6x8_80e_kitti-3d-3class.py 2 --resume-from checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-3class_20200620_230238-9208083a.pth
```
-   increase max_epoch value for continued training on configs/\_base\_/schedules/cyclic_40e.py

```bash
./tools/dist_train.sh configs/second/hv_second_secfpn_6x8_80e_kitti-3d-3class.py 2 --resume-from work_dirs/hv_second_secfpn_6x8_80e_kitti-3d-3class/latest.pth
```

### test
```bash
./tools/dist_test.sh configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth 2 --eval mAP
```
## MVXNet

### train

```bash
wget https://download.openmmlab.com/mmdetection3d/v0.1.0_models/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class_20200621_003904-10140f2d.pth -P ./checkpoints/
```
```bash
./tools/dist_train.sh configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py 2 --resume-from checkpoints/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class_20200621_003904-10140f2d.pth
```
-   increase max_epoch value for continued training on configs/\_base\_/schedules/cosine.py

```bash
./tools/dist_train.sh configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py 2 --resume-from work_dirs/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class/latest.pth
```

### test


```bash
./tools/dist_test.sh configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py checkpoints/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class_20200621_003904-10140f2d.pth 2 --eval mAP
```

# demo

1. checkpoint download

```bash
mkdir checkpoints
wget https://download.openmmlab.com/mmdetection3d/v0.1.0_models/second/hv_second_secfpn_6x8_80e_kitti-3d-car/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth -P ./checkpoints/
```

2. run demo

```bash
python demo/pcd_demo.py demo/data/kitti/kitti_000008.bin configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth --show
```
Multimodal
```bash
python demo/multi_modality_demo.py demo/data/gn_data/000012_data.bin demo/data/gn_data/000012_img.png demo/data/gn_data/000012_infos.pkl configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py ${CheckPointPath} --show
```


# dataset download

## Sample download

```bash
pip install gdown
```

## input file directory

```bash
/data/kitti/
# kitti-3d-3class.py
# dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py
```

## download kitti dataset sample to **/data**/kitti/ directory

-   gnict sample (overwrite)

```bash
gdown https://drive.google.com/uc?id=1zoQ0IA7ZVX58S1JFx34vvlbQHXMdkaDY -O /data/original/input/kitti.zip
```

-   gnict sample wo 2d (overwrite)

```bash
gdown https://drive.google.com/uc?id=1dCTaJ754XH2S2fr-e7M9ZzHl5VvGv2py -O /data/original/input/kitti_wo_2d.zip
```

-   kitti 3 (overwrite)

```bash
rm -rf /data/kitti
mkdir /data/tmp
gdown https://drive.google.com/uc?id=1rXb4RPC1ZclLlfKWLUppW71iKXvTFIEB -O /data/tmp/kitti.zip
unzip /data/tmp/*.zip -d /data/ && rm -rf /data/tmp
```

-   kitti 40 (overwrite)

```bash
rm -rf /data/kitti
mkdir /data/tmp
gdown https://drive.google.com/uc?id=1_3yU3HmFf-SqBrXXJLZw8-a_k7E6LV_D -O /data/tmp/kitti.zip
unzip /data/tmp/*.zip -d /data/ && rm -rf /data/tmp
```

## kitti dataset structure

```
trainval                 test
   |                      |
   +-----------+          |
   |           |          |
train(50%)  val(50%)     test
```

# NCP

```bash
chmod go= aica_083_ftp.pem
ssh -i aica_083.pem ubuntu@address
```
