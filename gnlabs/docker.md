# Docker setup

## Environment

-   OS: Ubuntu 18.04 / 20.04
-   GPU: NVIDIA GeForce GTX 1070 / RTX 2070 SUPER

## Install

1. install docker
2. install nvidia-container-toolkit
3. build

```bash
sudo docker build -t mmdetection3d gnlabs/
```

# docker env

## image
```bash
sudo docker run --gpus all --shm-size=8g -it -v /home/s/dev/mmdetection3d/data:/mmdetection3d/data -v /home/s/dev/mmdetection3d/work_dirs:/mmdetection3d/work_dirs mmdetection3d
```
## mis

### save
```bash
sudo docker save mmdetection3d -o mmdetection3d.tar
```

### load
```bash
sudo docker load -i mmdetection3d.tar
```

### tools
```bash
apt update
apt install wget
```
