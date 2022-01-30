# Docker setup

## Environment

-   OS: Ubuntu 18.04 / 20.04
-   GPU: NVIDIA GeForce GTX 1070 / RTX 2070 SUPER

## Install

1. install docker
2. install nvidia-container-toolkit
3. build

```bash
sudo docker build -t mmdetection3d docker/
```

# docker env

```bash
sudo docker run --gpus all --shm-size=8g -it -v /home/s/dev/mmdetection3d/data:/mmdetection3d/data -v /home/s/dev/mmdetection3d/work_dirs:/mmdetection3d/work_dirs mmdetection3d
```

```bash
apt update
apt install vim
apt install tmux
apt install wget
```
