import unittest
import excel
import hashlib


class TestExcelModule(unittest.TestCase):

    testFile = "testData/test_excel_data.xlsx"

    def test_excel_data_file_integrity(self):
        md5sum=hashlib.md5(open(self.testFile, 'rb').read()).hexdigest()
        self.assertEqual(md5sum, "423171b7712f08069fe47300a36f8d1f")

    def test_create_excel_writer(self):
        ew = excel.excelWriter("testWriter")
        self.assertIsInstance(ew, excel.excelWriter)

    def test_create_excel_reader(self):
        ew = excel.excelReader(self.testFile)
        self.assertIsInstance(ew, excel.excelReader)

    def test_read_all_lines(self):
        ew = excel.excelReader(self.testFile)
        self.assertEqual(len(ew.getRecordsAsList()), 11)


if __name__ == '__main__':
    unittest.main()
