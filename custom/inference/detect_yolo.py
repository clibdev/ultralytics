import os
import sys
import argparse
sys.path.append(os.getcwd())
from ultralytics import YOLO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='yolov8n.pt', help='Weights path')
    parser.add_argument('--source', type=str, default='./ultralytics/assets/bus.jpg')
    parser.add_argument('--img-size', type=int, default=640, help='Image size')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--save-img', action='store_true', help='save results')
    opt = parser.parse_args()

    model = YOLO(opt.weights)
    model.predict(
        opt.source,
        imgsz=opt.img_size,
        device=opt.device,
        save=opt.save_img
    )
