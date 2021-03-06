import unittest
import app

class TestApp(unittest.TestCase):

    # run before each case
    def setUp(self):
        self.app = app.app.test_client()

    # behaviour test for save
    def test_save_value(self):
        response = self.app.post('/', data=dict(submit='save',key='2',cache_value='two'))
        assert response.status_code = 200
        assert b'2' in response.data
        assert b'two' in response.data

    # behaviour test for load
    def test_load_value(self):
        self.app.post('/', data=dict(submit='value',key='2',cache_value='two'))
        response = self.app.post('/', data=dict(submit='load',key='2'))
        assert response.status_code == 200
        assert b'2' in response.data
        assert b'two' in response.data

if __name__ == '__main__':
    unittest.main()
