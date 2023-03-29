import unittest
import mock

from image_batch_processor.data_collection.image_file_finder import ImageFileFinder

class TestImageFileFinder(unittest.TestCase):
    def setUp(self):
        self.image_file_finder = ImageFileFinder()
        self.fake_start_dir = '/my/fake/dir'
        self.fake_file_dir = [
                ('/my/fake/dir', ['subdir1', 'subdir2', 'subdir3'], []),
                ('/my/fake/dir/subdir1', ['subdir4'], ['file_1.png', 'file_2.png']),
                ('/my/fake/dir/subdir1/subdir4', [], ['file_3.png', 'file_4.png']),
                ('my/fake/dir/subdir2', [], ['file_5.png', 'fake_file.jpg']),
                ('/my/fake/dir/subdir3', [], ['file_6.png'])
                ]
        self.expected_output = [
            ['/my/fake/dir/subdir1/file_1.png', '/my/fake/dir/subdir1/file_2.png'],
            ['/my/fake/dir/subdir1/subdir4/file_3.png', '/my/fake/dir/subdir1/subdir4/file_4.png'],
            ['my/fake/dir/subdir2/file_5.png'], 
            ['/my/fake/dir/subdir3/file_6.png']
            ]

    
    @mock.patch('image_batch_processor.data_collection.image_file_finder.os.path.abspath')
    @mock.patch('image_batch_processor.data_collection.image_file_finder.os.walk')
    @mock.patch('image_batch_processor.data_collection.image_file_finder.ImageFileFinder._ImageFileFinder__is_supported_image_file')
    def test_find_calls(self, mock_is_supported_image_file, mock_walk, mock_abspath):
        mock_abspath.return_value='/my/fake/dir'
        mock_walk.return_value=self.fake_file_dir
        mock_is_supported_image_file.side_effect=[True, True, True, True, True, False, True]

        fake_output = self.image_file_finder.find(self.fake_start_dir)

        mock_abspath.assert_called_once_with(self.fake_start_dir)
        mock_walk.assert_called_once_with(mock_abspath.return_value)
        mock_is_supported_image_file.assert_has_calls([
            mock.call('file_1.png'),
            mock.call('file_2.png'),
            mock.call('file_3.png'),
            mock.call('file_4.png'),
            mock.call('file_5.png'),
            mock.call('fake_file.jpg'),
            mock.call('file_6.png'),
            ])

        self.assertEqual(fake_output, self.expected_output)

    @mock.patch('image_batch_processor.data_collection.image_file_finder.os.walk')
    def test_find_functionality(self, mock_walk):
        mock_walk.return_value=self.fake_file_dir
        fake_output = self.image_file_finder.find(self.fake_start_dir)

        mock_walk.assert_called_once_with(self.fake_start_dir)
        self.assertEqual(fake_output, self.expected_output)
