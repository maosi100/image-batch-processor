from image_batch_processor.image_processing.image_upscaler import image_upscaler
from image_batch_processor.image_processing.image_watermarker import image_watermarker
import os

class ImageProcessor:
    def __init__(self, image_batch: list[str], multiplier: int) -> None:
        self.image_batch = image_batch
        self.multiplier = multiplier
        self.batch_name = self._create_batch_name(self.image_batch)

    def upscale_images(self) -> None:
        output_directory = self._create_output_directory(self.image_batch, 'Upscaled_Images')

        for i, image_path in enumerate(self.image_batch, start=1):
            output_file_name = self._create_file_name(image_path, self.batch_name, i)
            output_path = os.path.join(output_directory, output_file_name)

            image_upscaler(image_path, output_path, self.multiplier)

    def watermark_images(self) -> None:
        output_directory = self._create_output_directory(self.image_batch, 'Preview_Images')

        for i, image_path in enumerate(self.image_batch, start=1):
            output_file_name = self._create_file_name(image_path, self.batch_name, i)
            output_path = os.path.join(output_directory, output_file_name)

            image_watermarker(image_path, output_path)

    def create_preview_images(self) -> None:
        pass

    @staticmethod
    def _create_file_name(image_path: str, batch_name: str, count: int) -> str:
        file_extension = os.path.splitext(image_path)[1]
        return f"{batch_name}_{count}{file_extension}"
    
    @staticmethod
    def _create_batch_name(image_batch: str) -> str:
        root = os.path.split(image_batch[0])[0]
        return root.split('/')[-1]
    
    @staticmethod
    def _create_output_directory(image_batch: str, directory_name: str) -> str:
        root = os.path.split(image_batch[0])[0]
        os.mkdir(os.path.join(root, directory_name))
        return os.path.join(root, directory_name)
