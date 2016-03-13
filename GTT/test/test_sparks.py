import unittest
import hashlib
import sparks


class TestSparksModule(unittest.TestCase):

    testFile = "testData/test_sparks_data.dbf"
    recordsInTestFile = 807
    testFileMD5 = "3d7fb57bf61967786b55c745077d7cd4"

    def test_sparks_data_file_integrity(self):
        md5sum = hashlib.md5(open(self.testFile, 'rb').read()).hexdigest()
        self.assertEqual(md5sum, self.testFileMD5)

    def test_create_sparks_reader(self):
        sp = sparks.SPARKSReader(self.testFile)
        self.assertIsInstance(sp, sparks.SPARKSReader)

    def test_read_all_lines(self):
        sp = sparks.SPARKSReader(self.testFile)
        self.assertEqual(len(sp.get_records_as_list()), self.recordsInTestFile)

if __name__ == '__main__':
    unittest.main()