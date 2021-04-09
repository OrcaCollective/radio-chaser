import unittest

import radio_chaser


class Radio_chaserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = radio_chaser.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to Radio Chaser', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
