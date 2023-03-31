import cv2
from cv2 import dnn_superres

def image_upscaler(image_path, output_path, multiplier):
    sr = dnn_superres.DnnSuperResImpl_create()
    image = cv2.imread(image_path)

    path = './image_batch_processor/image_processing/utilities/EDSR_x3.pb'

    sr.readModel(path)
    sr.setModel('edsr', multiplier)

    result = sr.upsample(image)
    cv2.imwrite(output_path, result)
