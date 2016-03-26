"""
This module is a general example using test data showing usage of sparks, excel
and the studbook structure.
"""
import os

from GTT import SPARKS
from GTT import excel as ew
from GTT import studBookStruct

TEST_DIR = os.path.dirname(__file__)
TEST_DATA_DIR = os.path.join(TEST_DIR, 'testData')

# my_sparks_reader = SPARKS.SPARKSReader("test/testData/test_sparks_data.dbf")
moves_data = os.path.join(TEST_DATA_DIR, 'test_moves_data.dbf')
my_sparks_reader = SPARKS.SPARKSReader(moves_data)
my_excel_writer = ew.ExcelWriter("test/testData/test_excel_write.xlsx")

my_studbook = studBookStruct.Studbook()

my_studbook.add_header(my_sparks_reader.get_header_as_list())
my_studbook.add_records_from_list(my_sparks_reader.get_records_as_list())

my_excel_writer.write_studbook(my_studbook)
my_excel_writer.close()


