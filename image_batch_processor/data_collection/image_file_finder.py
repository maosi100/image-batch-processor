import os

SUPPORTED_FILE_EXTENSIONS = ['.png']

class ImageFileFinder:
    def find(self, start_dir: str) -> list[list[str]]:
        abs_start_dir = os.path.abspath(start_dir)
        image_files = []
        for root, _, files in os.walk(abs_start_dir):
            temporary_image_files = []
            for file_name in files:
                if self.__is_supported_image_file(file_name):
                    temporary_image_files.append(os.path.join(root, file_name))
            if temporary_image_files:
                image_files.append(temporary_image_files)

        return image_files

    def __is_supported_image_file(self, file_name: str) -> bool:
        file_extension = os.path.splitext(file_name)[1]
        
        return file_extension in SUPPORTED_FILE_EXTENSIONS
