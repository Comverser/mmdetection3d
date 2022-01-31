# Local setup

## Environment

-   OS: Ubuntu 18.04/20.04
-   GPU: NVIDIA GeForce GTX 1070 / RTX 2070 SUPER / RTX 3080
-   CUDA: 10.1.2/11.1.1

## Install

```bash
# create conda env
conda create -n gn python=3.7 -y
conda activate gn

# install PyTorch with CUDA
conda install pytorch==1.6.0 cudatoolkit=10.1 torchvision==0.7.0 -c pytorch

# install mmcv
pip install mmcv-full==1.3.13 -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.6.0/index.html

# install mmdetection
pip install mmdet==2.19.0

# install mmsegmentation
pip install mmsegmentation==0.20.0

# install mmdetection3d
git clone https://github.com/Comverser/mmdetection3d.git
cd mmdetection3d
pip install -v -e .

# install visualization package
pip install open3d

```

### set "samples_per_gpu" to 1

-   https://github.com/open-mmlab/mmdetection3d/issues/37


### Search "HShin" comments in the source code to find other modifications 

# RTX 3080 case

## out of memory (RTX 3080 case)

-   Change parameters (4096 -> 2048 ) on mmdet3d/ops/spconv/src/indice_cuda.cu

## system reboot when training
https://discuss.pytorch.org/t/system-reboot-when-training/108317
```bash
nvidia-smi -i 0,1 -pl 250
```
