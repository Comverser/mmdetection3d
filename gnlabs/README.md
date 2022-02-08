# PointPillars

## demo

```bash
python demo/pcd_demo.py gnlabs/demo/000012_data.bin \
    configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py checkpoints/pointpillars.pth --show
```

## train

-   set dataset directory

```bash
vim configs/_base_/datasets/kitti-3d-3class.py
vim configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py
```

```bash
tools/dist_train.sh configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py 2
```

-   increase max_epoch value for continued training on configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py

```bash
vim configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py
```

```bash
tools/dist_train.sh configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py 2 --resume-from work_dirs/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class/latest.pth
```

## test

```bash
python tools/test.py configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py \
    checkpoints/pointpillars.pth \
    --out data/kitti/results_pointpillars.pkl \
    --eval mAP

python tools/test.py configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py \
    checkpoints/pointpillars.pth 2 \
    --out data/kitti/results_pointpillars.pkl \
    --format-only --option submission_prefix=gnlabs/calc_ap/results/submission/

python tools/misc/visualize_results.py configs/pointpillars/hv_pointpillars_secfpn_6x8_160e_kitti-3d-3class.py \
    --result data/kitti/results_pointpillars.pkl --show-dir data/kitti/show_results_pointpillars
```

# SECOND

## demo

```bash
python demo/pcd_demo.py gnlabs/demo/000012_data.bin \
    configs/second/hv_second_secfpn_6x8_80e_kitti-3d-3class.py checkpoints/second.pth --show
```

## train

```bash
tools/dist_train.sh configs/second/hv_second_secfpn_6x8_80e_kitti-3d-3class.py 2
```

-   increase max_epoch value for continued training on configs/\_base\_/schedules/cyclic_40e.py

```bash
tools/dist_train.sh configs/second/hv_second_secfpn_6x8_80e_kitti-3d-3class.py 2 --resume-from work_dirs/hv_second_secfpn_6x8_80e_kitti-3d-3class/latest.pth
```

## test

```bash
python tools/test.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-3class.py \
    checkpoints/second.pth \
    --out data/kitti/results_second.pkl \
    --eval mAP

python tools/test.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-3class.py \
    checkpoints/second.pth 2 \
    --out data/kitti/results_second.pkl \
    --format-only --option submission_prefix=gnlabs/calc_ap/results/submission/

python tools/misc/visualize_results.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-3class.py \
    --result data/kitti/results_second.pkl --show-dir data/kitti/show_results_second
```

# MVXNet

## demo

```bash
python demo/multi_modality_demo.py gnlabs/demo/000012_data.bin gnlabs/demo/000012_img.png gnlabs/demo/000012_infos.pkl \
    configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py checkpoints/mvxnet.pth --show
```

## train

-   set dataset directory

```bash
vim configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py
```

multi gpu (not stable)

```bash
python tools/train.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py

tools/dist_train.sh configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py 2
```

-   increase max_epoch value for continued training on configs/\_base\_/schedules/cosine.py

```bash
vim configs/_base_/schedules/cosine.py
```

```bash
tools/dist_train.sh configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py 2 --resume-from work_dirs/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class/latest.pth

python tools/train.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py --resume-from work_dirs/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class/latest.pth
```

## test

```bash
python tools/test.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py \
    checkpoints/mvxnet.pth \
    --out data/kitti/results_mvxnet.pkl \
    --eval mAP

python tools/test.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py \
    checkpoints/mvxnet.pth 2 \
    --out data/kitti/results_mvxnet.pkl \
    --format-only --option submission_prefix=gnlabs/calc_ap/results/submission/


python tools/misc/visualize_results.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py \
    --result data/kitti/results_mvxnet.pkl --show-dir data/kitti/show_results_mvxnet/
```

# mis

## dataset preparation

```bash
python tools/create_data.py kitti --root-path data/kitti --out-dir data/kitti --extra-tag kitti
```

## browse

```bash
python tools/misc/browse_dataset.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py --task multi_modality-det --output-dir data/kitti/results/ --online
```

## mmdetection demo

```bash
mkdir checkpoints
wget https://download.openmmlab.com/mmdetection3d/v0.1.0_models/second/hv_second_secfpn_6x8_80e_kitti-3d-car/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth -P checkpoints/
```

```bash
python demo/pcd_demo.py demo/data/kitti/kitti_000008.bin configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth --show
```

## sample dataset download

```bash
pip install gdown
```

-   kitti 3 (overwrite)

```bash
rm -rf data/kitti
mkdir data/tmp
gdown https://drive.google.com/uc?id=1rXb4RPC1ZclLlfKWLUppW71iKXvTFIEB -O data/tmp/kitti.zip
unzip data/tmp/*.zip -d data/ && rm -rf data/tmp
```

-   kitti 40 (overwrite)

```bash
rm -rf data/kitti
mkdir data/tmp
gdown https://drive.google.com/uc?id=1_3yU3HmFf-SqBrXXJLZw8-a_k7E6LV_D -O data/tmp/kitti.zip
unzip data/tmp/*.zip -d data/ && rm -rf data/tmp
```

### kitti dataset structure

```
trainval                 test
   |                      |
   +-----------+          |
   |           |          |
train(50%)  val(50%)     test
```
