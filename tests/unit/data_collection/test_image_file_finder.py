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
        self.mock_abspath = mock.patch(
            'image_batch_processor.data_collection.image_file_finder.os.path.abspath',
            return_value='/my/fake/dir'
            ).start()
        self.mock_walk = mock.patch(
            'image_batch_processor.data_collection.image_file_finder.os.walk',
            return_value=self.fake_file_dir
                ).start()
        self.mock_is_supported_image_file = mock.patch(
            'image_batch_processor.data_collection.image_file_finder.\
                    ImageFileFinder._ImageFileFinder__is_supported_image_file',
            side_effect=[True, True, True, True, True, False, True]
                ).start()

    def tearDown(self):
        self.mock_abspath.stop()
        self.mock_walk.stop()
        self.mock_is_supported_image_file.stop()

    def test_find_calls(self):
        fake_output = self.image_file_finder.find(self.fake_start_dir)

        self.mock_abspath.assert_called_once_with(self.fake_start_dir)
        self.mock.walk.assert_called_once_with(self.mock_abspath.return_value)
        self.mock_is_supported_image_file.assert_has_calls([
            mock.call('file_1.png'),
            mock.call('file_2.png'),
            mock.call('file_3.png'),
            mock.call('file_4.png'),
            mock.call('file_5.png'),
            mock.call('fake_file.jpg'),
            mock.call('file_6.png'),
            ])

        self.assertEqual(fake_output, self.expected_output)

    def test_find_functionality(self):
        fake_output = self.image_file_finder.find(self.fake_start_dir)

        self.mock_walk.assert_called_once_with(self.fake_start_dir)
        self.assertEqual(fake_output, self.expected_output)

