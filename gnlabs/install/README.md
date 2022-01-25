# Local setup

## Environment

-   OS: Ubuntu 20.04
-   GPU: NVIDIA GeForce RTX 2070 SUPER / RTX 3080
-   CUDA: 10.1.2 / 11.1.1, respectively

## Install

### conda

```bash
conda create -n gn python=3.7 -y
conda activate gn
```

### General case v0.18.0
```bash
# install PyTorch with CUDA
conda install pytorch==1.5.0 cudatoolkit=10.1 torchvision==0.6.0 -c pytorch

# install mmcv
pip install mmcv-full

# install mmdetection
pip install git+https://github.com/open-mmlab/mmdetection.git

# install mmsegmentation
pip install git+https://github.com/open-mmlab/mmsegmentation.git
```

### RTX 2070 case v0.17.0 (support docker image)

```bash
# install PyTorch with the CUDA version
conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch
sudo apt-get update && sudo apt-get install -y ffmpeg libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# install mmcv
pip install mmcv-full==1.3.8 -f https://download.openmmlab.com/mmcv/dist/cu101/torch1.6.0/index.html
# install mmdetection
pip install mmdet==2.14.0
# install mmsegmentation
pip install mmsegmentation==0.14.1
```

### RTX 3080 case v0.17.0 (better performance)

```bash
conda install pytorch==1.8.0 torchvision==0.9.0 cudatoolkit=11.1 -c pytorch -c nvidia
pip install mmcv-full==1.4.0
pip install mmdet==2.19.0
pip install mmsegmentation==0.19.0
```

#### out of memory

-   Change parameters (4096 -> 2048 ) on mmdet3d/ops/spconv/src/indice_cuda.cu

#### system reboot when training
https://discuss.pytorch.org/t/system-reboot-when-training/108317
```bash
nvidia-smi -i 0,1 -pl 250
```

### common

```bash
# install mmdetection3d-0.17.0
git clone https://github.com/Comverser/mmdetection3d.git
cd mmdetection3d
pip install -v -e .

# compatibility error fix
pip install pycocotools==2.0.1
# install visualization package
pip install open3d
```

# set "samples_per_gpu" to 1

-   https://github.com/open-mmlab/mmdetection3d/issues/37
