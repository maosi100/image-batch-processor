import cv2
from cv2 import dnn_superres

def image_upscaler(input_path, output_path, multiplier):
    sr = dnn_superres.DnnSuperResImpl_create()
    image = cv2.imread(input_path)

    path = './upscaling_models/EDSR_x3.pb'
    sr.readModel(path)
    sr.setModel('edsr', multiplier)

    result = sr.upsample(image)
    cv2.imwrite(output_path, result)
