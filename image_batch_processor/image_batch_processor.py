from image_batch_processor.image_processing.image_modification import image_upscaler, image_watermarker, image_preview_creator 
from image_batch_processor.image_processing.preview_label_creator import create_preview_label
import zipfile
import os

class ImageBatchProcessor:
    def __init__(self, image_batch: list[str], multiplier: int) -> None:
        self.image_batch = image_batch
        self.multiplier = multiplier
        self.batch_name = self._create_batch_name(self.image_batch)
        self.upscaled_output_dir = None
        self.preview_output_dir = None

    def upscale_images(self) -> None:
        self.upscaled_output_dir = self._create_output_directory(self.image_batch, 'Upscaled_Images')

        for i, image_path in enumerate(self.image_batch, start=1):
            output_file_name = self._create_file_name(image_path, self.batch_name, i)
            output_path = os.path.join(self.upscaled_output_dir, output_file_name)

            image_upscaler(image_path, output_path, self.multiplier)

        self._create_zip_files(self.upscaled_output_dir)

    def watermark_images(self) -> None:
        self.preview_output_dir = self._create_output_directory(self.image_batch, 'Preview_Images')

        for i, image_path in enumerate(self.image_batch, start=1):
            output_file_name = self._create_file_name(image_path, self.batch_name, i)
            output_path = os.path.join(self.preview_output_dir, output_file_name)

            image_watermarker(image_path, output_path)

    def create_preview_image(self, label: str = None) -> None:
        if not self.preview_output_dir:
            self.preview_output_dir = self._create_output_directory(self.image_batch, 'Preview_Images')
        
        preview_label = None
        if label:
            preview_label = create_preview_label(self.batch_name, len(self.image_batch), self.preview_output_dir)

        output_path = f"{self.preview_output_dir}/{self.batch_name}_preview.png" 
        image_preview_creator(self.image_batch, output_path, preview_label)
    

    def _create_zip_files(self, input_dir: str) -> None:
        zip_file_name = input_dir + self.batch_name + ".zip"

        zip_file = zipfile.ZipFile(zip_file_name, "w", zipfile.ZIP_DEFLATED)

        for root, _, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, input_dir))

        zip_file.close()

    @staticmethod
    def _create_file_name(image_path: str, batch_name: str, count: int) -> str:
        file_extension = os.path.splitext(image_path)[1]
        return f"{batch_name}_{count}{file_extension}"
    
    @staticmethod
    def _create_batch_name(image_batch: str) -> str:
        root = os.path.split(image_batch[0])[0]
        return root.replace('_', ' ').split('/')[-1]
    
    @staticmethod
    def _create_output_directory(image_batch: str, directory_name: str) -> str:
        root = os.path.split(image_batch[0])[0]
        os.mkdir(os.path.join(root, directory_name))
        return os.path.join(root, directory_name)
