from unittest import TestCase
import ya_api


class TestYaApi(TestCase):

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(ya_api.create_folder(), 201)

    def test_passed_create_folder(self):
        self.assertEqual(ya_api.create_folder('test_passed'), 409)

    def tearDown(self):
        ya_api.delete_folder('test')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()