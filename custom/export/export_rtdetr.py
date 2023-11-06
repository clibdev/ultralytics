import os
import sys
import argparse
sys.path.append(os.getcwd())
from ultralytics import RTDETR


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='rtdetr-l.pt', help='Weights path')
    parser.add_argument('--img-size', type=int, default=640, help='Image size')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--dynamic', action='store_true', default=False, help='Enable dynamic axis in ONNX model')
    opt = parser.parse_args()

    model = RTDETR(opt.weights)
    model.export(
        format='onnx',
        imgsz=opt.img_size,
        device=opt.device,
        dynamic=opt.dynamic
    )
