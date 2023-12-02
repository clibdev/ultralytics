# Fork of [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

Differences between original repository and fork:

* Instructions how to train face detection model using WIDERFace dataset.

# Installation

```shell
pip install -r requirements.txt
```

# Inference

## YOLOv8

```shell
python custom/inference/detect_yolo.py --weights yolov8n.pt --source ultralytics/assets/bus.jpg --save-img
```

## RT-DETR

```shell
python custom/inference/detect_rtdetr.py --weights rtdetr-l.pt --source ultralytics/assets/bus.jpg --save-img
```

# Export to ONNX format

## YOLOv8

```shell
python custom/export/export_yolo.py --weights yolov8n.pt
```

## RT-DETR

```shell
python custom/export/export_rtdetr.py --weights rtdetr-l.pt
```

# Training

## Face detection (WIDERFace dataset)

* Start training:

```shell
python custom/train/train.py --weights yolov8n.pt --data custom/train/data/widerface.yaml --epochs 300 2>&1 | tee -a results.txt
```

* Resume training:

```shell
python custom/train/train.py --weights runs/detect/train/weights/last.pt --data custom/train/data/widerface.yaml --resume 2>&1 | tee -a results.txt
```
