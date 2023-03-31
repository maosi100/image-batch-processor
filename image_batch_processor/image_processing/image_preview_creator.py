import cv2
import numpy as np

def image_preview_creator(image_batch, output_dir):
    output_format = {'width': 1140, 'height': 760}

    preview_image = 255 * np.ones(shape=[output_format['height'], output_format['width'], 3], dtype=np.uint8)

    target_width = output_format['width'] // (len(image_batch) // 2)
    target_height = output_format['height'] // 2

    for i, image in enumerate(image_batch):
        loaded_image = cv2.imread(image)
        
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

    cv2.imwrite(output_dir, preview_image)
