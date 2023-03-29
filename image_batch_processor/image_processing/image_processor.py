from image_batch_processor.image_processing.image_upscaler import image_upscaler
import os

class ImageProcessor:
    def __init__(self, image_batch: list[str], multiplier: int):
        self.image_batch = image_batch
        self.multiplier = multiplier
        self.batch_name = self.__create_batch_name(self.image_batch)

    def upscale_images(self):
        output_directory = self.__create_output_directory(self.image_batch, 'Upscaled_Images')

        for i, image_path in enumerate(self.image_batch, start=1):
            output_file_name = self.__create_file_name(image_path, self.batch_name, i)
            output_path = os.path.join(output_directory, output_file_name)

            image_upscaler(image_path, output_path, self.multiplier)

    def watermark_images(self):
        pass

    def create_preview_images(self):
        pass

    def __create_file_name(self, image_path, batch_name, count):
        file_extension = os.path.splitext(image_path)[1]
        return f"{batch_name}_{count}{file_extension}"

    def __create_batch_name(self, image_batch):
        root = os.path.split(image_batch[0])[0]
        return root.split('/')[-1]
        
    def __create_output_directory(self, image_batch, directory_name):
        root = os.path.split(image_batch[0])[0]
        os.mkdir(os.path.join(root, directory_name))
        return os.path.join(root, directory_name)
