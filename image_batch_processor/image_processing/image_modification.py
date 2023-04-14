from cv2 import cv2
from cv2 import dnn_superres
import numpy as np

def image_upscaler(image_path: str, output_path: str, multiplier: int) -> None:
    sr = dnn_superres.DnnSuperResImpl_create()
    image = cv2.imread(image_path)

    path = './image_batch_processor/image_processing/utilities/EDSR_x3.pb'

    sr.readModel(path)
    sr.setModel('edsr', multiplier)

    result = sr.upsample(image)
    cv2.imwrite(output_path, result)


def image_watermarker(image_path: str, output_path:str) -> None:
    image = cv2.imread(image_path)
    path = './image_batch_processor/image_processing/utilities/watermark.png'
    watermark_image = cv2.imread(path)

    h_image, w_image, _ = image.shape
    h_watermark_image, w_watermark_image, _ = watermark_image.shape

    center_y = h_image // 2
    center_x = w_image // 2

    top_y = center_y - h_watermark_image // 2
    bottom_y = top_y + h_watermark_image
    left_x = center_x - w_watermark_image // 2
    right_x = left_x + w_watermark_image

    destination = image[top_y:bottom_y, left_x:right_x]
    output_image = cv2.addWeighted(destination,1, watermark_image, 0.5, 0)
    image[top_y:bottom_y, left_x:right_x] = output_image
    
    cv2.imwrite(output_path, image)


def image_preview_creator(image_batch: str, output_dir: str, label: str = "") -> None:
    output_format = {'width': 1140, 'height': 760}

    preview_image = 255 * np.ones(shape=[output_format['height'], output_format['width'], 3], dtype=np.uint8)

    target_width = output_format['width'] // (len(image_batch) // 2)
    target_height = output_format['height'] // 2

    for i, image in enumerate(image_batch):
        loaded_image = cv2.imread(image)
        resized_image = cv2.resize(loaded_image, (570, 570))
        loaded_image = resized_image
        
        if i < (len(image_batch) / 2):
            top_y = target_height * 0
            bottom_y = target_height * 1
            left_x = target_width * i
            right_x = target_width * i + target_width

            region_of_interest = loaded_image[0:target_height, 0:target_width]
            preview_image[top_y:bottom_y, left_x:right_x] = region_of_interest
        else:
            top_y = target_height * 1
            bottom_y = target_height * 2
            left_x = target_width * (i - len(image_batch) // 2)
            right_x = target_width * (i - len(image_batch) // 2) + target_width
            
            region_of_interest = loaded_image[0:target_height, 0:target_width]
            preview_image[top_y:bottom_y, left_x:right_x] = region_of_interest
    
    if label:
        label_image = cv2.imread(label)
        preview_image[330:430, 0:1140] = label_image

    cv2.imwrite(output_dir, preview_image)
