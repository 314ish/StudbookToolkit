import unittest
import studBookStruct

class TestStringMethods(unittest.TestCase):

    def test_create_studbook(self):
        sb = studBookStruct.Studbook()
        self.assertIsInstance(sb, studBookStruct.Studbook)

    def test_add_records_from_list(self):
        self.assertTrue(True)

    def test_add_chick_record(self):
        self.assertTrue(True)

    def test_add_complete_record(self):
        self.assertTrue(True)

    def test_add_move(self):
        self.assertTrue(True)

    def test_add_header(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
