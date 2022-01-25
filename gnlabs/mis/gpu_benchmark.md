We would like to share my benchmark results of NVIDIA GeForce RTX series match: 2070 SUPER vs 3080.

**Results**
| 2070 SUPER | 2070 SUPER (docker) | 3080      |
| ------------------ | ----------------------------- | ------------ |
| 14m 38s         | 14m 55s                      | 10m 51s |

**Conditions**
1. Dataset: Kitti dataset
2. Data size: 40 frames
3. Model: SECOND
4. Code change:  set "samples_per_gpu" to 1
5. Command
```bash
python tools/train.py configs/second/hv_second_secfpn_6x8_80e_kitti-3d-car.py
```
6. Systems
- OS: Ubuntu 18.04 and 20.04 respectively
- CPU: Intel i7-10700K @ 3.80 GHz
- Memory: 32GiB
- CUDA: 10.1.2 and 11.1 respectively
- Pytorch: 1.6.0 and 1.8.0 respectively
- Conda version: 2021 and 2019 respectively
