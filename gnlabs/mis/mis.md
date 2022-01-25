1. dataset preparation

```bash
python tools/create_data.py kitti --root-path /data/kitti --out-dir /data/kitti --extra-tag kitti
```

2. train

```bash
python tools/train.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py --resume-from checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth
```

3. test

```bash
python tools/test.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth --show --show-dir data/kitti/show_dir/
```

-   mAP only

```bash
python tools/test.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth --eval mAP
```

4. browse

```bash
python tools/misc/browse_dataset.py configs/mvxnet/dv_mvx-fpn_second_secfpn_adamw_2x8_80e_kitti-3d-3class.py --task multi_modality-det --output-dir data/kitti/results/ --online
```

5. visualization

-   prediction results (Car class only)

```bash
python tools/test.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py checkpoints/hv_second_secfpn_6x8_80e_kitti-3d-car_20200620_230238-393f000c.pth --show --show-dir data/kitti/show_dir/
```
