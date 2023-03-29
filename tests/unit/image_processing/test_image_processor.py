import unittest
import mock

from image_batch_processor.image_processing.image_processor import ImageProcessor

class TestImageProcessor(unittest.TestCase):

    def setUp(self):
        self.fake_image_batch = ['/my/fake/dir/file_x.png', '/my/fake/dir/file_y.png']
        self.fake_multiplier = 3
        self.fake_batch_name = 'dir'
        self.fake_target_directory = '/my/fake/dir/Upscaled_Images'
        self.fake_image_processor = ImageProcessor(self.fake_image_batch, self.fake_multiplier)


    @mock.patch.object(ImageProcessor, '__init__')
    def test_init_calls(self, mock_init):
        mock_init.return_value = None

        ImageProcessor(self.fake_image_batch, self.fake_multiplier)
        mock_init.assert_called_once_with(self.fake_image_batch, self.fake_multiplier)


    def test_init_functionality(self):
        fake_image_processor = ImageProcessor(self.fake_image_batch, self.fake_multiplier)
        
        self.assertEqual(fake_image_processor.image_batch, self.fake_image_batch)
        self.assertEqual(fake_image_processor.multiplier, self.fake_multiplier)
        self.assertEqual(fake_image_processor.batch_name, self.fake_batch_name)


    @mock.patch('image_batch_processor.image_processing.image_processor.image_upscaler')
    @mock.patch('image_batch_processor.image_processing.image_processor.os.path.join')
    @mock.patch('image_batch_processor.image_processing.image_processor.ImageProcessor._ImageProcessor__create_output_directory')
    def test_upscale_images(self, mock_create_output_directory, mock_join, mock_image_upscaler):
        mock_create_output_directory.return_value = '/my/fake/dir/Upscaled_Images'
        mock_join.side_effect = ['/my/fake/dir/Upscaled_Images/dir_1.png', '/my/fake/dir/Upscaled_Images/dir_2.png']
        
        self.fake_image_processor.upscale_images()

        mock_join.assert_has_calls([
            mock.call(mock_create_output_directory.return_value, 'dir_1.png'),
            mock.call(mock_create_output_directory.return_value, 'dir_2.png')
            ])
        mock_image_upscaler.assert_has_calls([
            mock.call('/my/fake/dir/file_x.png', '/my/fake/dir/Upscaled_Images/dir_1.png', self.fake_multiplier),
            mock.call('/my/fake/dir/file_y.png', '/my/fake/dir/Upscaled_Images/dir_2.png', self.fake_multiplier)
            ])


    @mock.patch('image_batch_processor.image_processing.image_processor.os.mkdir')
    def test_create_output_directory(self, mock_mkdir):
        fake_output = self.fake_image_processor._ImageProcessor__create_output_directory(
                self.fake_image_batch, 'Upscaled_Images'
                )
        
        mock_mkdir.assert_called_once_with(self.fake_target_directory)

        self.assertEqual(fake_output, self.fake_target_directory)
