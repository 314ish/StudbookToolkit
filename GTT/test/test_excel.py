import unittest
import excel
import hashlib


class TestExcelModule(unittest.TestCase):

    testFile = "testData/test_excel_data.xlsx"
    recordsInTestFile = 11
    testFileMD5 = "423171b7712f08069fe47300a36f8d1f"

    def test_excel_data_file_integrity(self):
        md5sum = hashlib.md5(open(self.testFile, 'rb').read()).hexdigest()
        self.assertEqual(md5sum, self.testFileMD5)

    def test_create_excel_writer(self):
        ew = excel.ExcelWriter("testWriter")
        self.assertIsInstance(ew, excel.ExcelWriter)

    # def test_write_excel_record(self):
    #     ew = excel.ExcelWriter("testWriter")
    #     # TODO: fill this test out

    def test_create_excel_reader(self):
        ew = excel.ExcelReader(self.testFile)
        self.assertIsInstance(ew, excel.ExcelReader)

    def test_read_all_lines(self):
        er = excel.ExcelReader(self.testFile)
        self.assertEqual(len(er.get_records_as_list()), self.recordsInTestFile)


if __name__ == '__main__':
    unittest.main()
