import cv2

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
