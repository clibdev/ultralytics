import argparse
from ultralytics import YOLO


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='yolov8n.pt', help='Initial weights path')
    parser.add_argument('--data', type=str, default='train/data/widerface.yaml', help='Path to data file')
    parser.add_argument('--epochs', type=int, default=300)
    parser.add_argument('--batch', type=int, default=16)
    parser.add_argument('--img-size', type=int, default=640, help='Size of input images')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--resume', nargs='?', const=True, default=False, help='Resume most recent training')
    opt = parser.parse_args()

    model = YOLO(opt.weights)
    model.train(
        data=opt.data,
        epochs=opt.epochs,
        batch=opt.batch,
        imgsz=opt.img_size,
        device=opt.device,
        resume=opt.resume
    )
