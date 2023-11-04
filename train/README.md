# Fork of [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

Differences between original repository and fork:

* Instructions how to train face detection model using WIDERFace dataset.

# Installation

```shell
pip install -r requirements.txt
```

# Training

## Face detection (WIDERFace dataset)

* Start training:

```shell
python train.py --weights yolov8n.pt --data train/data/widerface.yaml
```

* Resume training:

```shell
python train.py --weights runs/detect/train/weights/last.pt --data train/data/widerface.yaml --resume
```
