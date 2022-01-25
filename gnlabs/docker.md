# Docker setup

## Environment

-   OS: Ubuntu 18.04
-   GPU: NVIDIA GeForce RTX 2070 SUPER
-   CUDA: 11.1.1 / 10.1.2

## Install

1. install docker
2. install nvidia-container-toolkit
3. build

```bash
sudo docker build -t mmdetection3d gnlabs/
```

# docker env

```bash
sudo docker run --gpus all --shm-size=8g -it -v /home/s/dev/mmdetection3d/data:/mmdetection3d/data mmdetection3d
```

```bash
apt-get update
apt-get install wget
apt-get install vim
```
