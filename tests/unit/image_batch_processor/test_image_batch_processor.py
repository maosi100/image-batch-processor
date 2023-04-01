import unittest
import mock

from image_batch_processor.image_batch_processor import ImageBatchProcessor

class TestImageBatchProcessor(unittest.TestCase):

    def setUp(self):
        self.fake_image_batch = ['/my/fake/dir/file_x.png', '/my/fake/dir/file_y.png']
        self.fake_multiplier = 3
        self.fake_batch_name = 'dir'
        self.fake_target_directory = '/my/fake/dir/Upscaled_Images'
        self.fake_image_processor = ImageBatchProcessor(self.fake_image_batch, self.fake_multiplier)
        self.fake_preview_output_dir ='/my/fake/dir/Preview_Images'


    @mock.patch.object(ImageBatchProcessor, '__init__')
    def test_init_calls(self, mock_init):
        mock_init.return_value = None

        ImageBatchProcessor(self.fake_image_batch, self.fake_multiplier)
        mock_init.assert_called_once_with(self.fake_image_batch, self.fake_multiplier)


    def test_init_functionality(self):
        fake_image_processor = ImageBatchProcessor(self.fake_image_batch, self.fake_multiplier)
        
        self.assertEqual(fake_image_processor.image_batch, self.fake_image_batch)
        self.assertEqual(fake_image_processor.multiplier, self.fake_multiplier)
        self.assertEqual(fake_image_processor.batch_name, self.fake_batch_name)


    @mock.patch('image_batch_processor.image_batch_processor.image_upscaler')
    @mock.patch('image_batch_processor.image_batch_processor.ImageBatchProcessor._create_output_directory')
    def test_upscale_images(self, mock_create_output_directory, mock_image_upscaler):
        mock_create_output_directory.return_value = '/my/fake/dir/Upscaled_Images'
        
        self.fake_image_processor.upscale_images()

        mock_image_upscaler.assert_has_calls([
            mock.call('/my/fake/dir/file_x.png', '/my/fake/dir/Upscaled_Images/dir_1.png', self.fake_multiplier),
            mock.call('/my/fake/dir/file_y.png', '/my/fake/dir/Upscaled_Images/dir_2.png', self.fake_multiplier)
            ])


    @mock.patch('image_batch_processor.image_batch_processor.image_watermarker')
    @mock.patch('image_batch_processor.image_batch_processor.ImageBatchProcessor._create_output_directory')
    def test_watermark_images(self, mock_create_output_directory, mock_image_watermarker):
        mock_create_output_directory.return_value = '/my/fake/dir/Preview_Images'
        
        self.fake_image_processor.watermark_images()
    
        mock_image_watermarker.assert_has_calls([
            mock.call('/my/fake/dir/file_x.png', '/my/fake/dir/Preview_Images/dir_1.png'),
            mock.call('/my/fake/dir/file_y.png', '/my/fake/dir/Preview_Images/dir_2.png')
            ])


    @mock.patch('image_batch_processor.image_batch_processor.create_preview_label')
    @mock.patch('image_batch_processor.image_batch_processor.image_preview_creator')
    @mock.patch('image_batch_processor.image_batch_processor.ImageBatchProcessor._create_output_directory')
    def test_create_preview_image(self, mock_create_output_directory, mock_image_preview_creator, mock_create_preview_label):
        mock_create_output_directory.return_value = '/my/fake/dir/Preview_Images'
        mock_create_preview_label.return_value='/my/fake/dir/label.png'

        self.fake_image_processor.create_preview_image()

        mock_create_preview_label.assert_called_once_with(
                self.fake_batch_name, len(self.fake_image_batch), '/my/fake/dir/Preview_Images')

        mock_image_preview_creator.assert_called_once_with(
                self.fake_image_batch, '/my/fake/dir/Preview_Images/dir_preview.png','/my/fake/dir/label.png')


    @mock.patch('image_batch_processor.image_batch_processor.os.mkdir')
    def test_create_output_directory(self, mock_mkdir):
        fake_output = self.fake_image_processor._create_output_directory(
                self.fake_image_batch, 'Upscaled_Images'
                )
        
        mock_mkdir.assert_called_once_with(self.fake_target_directory)

        self.assertEqual(fake_output, self.fake_target_directory)
