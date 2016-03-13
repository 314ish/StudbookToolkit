"""
This module is a general example using test data showing usage of sparks, excel
and studbookStruct.
"""

import sparks as sparks
import excel as ew
import studBookStruct as sb


excelPairs = ew.ExcelReader("testData/2016_pairs.xlsx")
exchangeSparks = sparks.SPARKSReader("testData/EXCHANGE.DBF")
movesSparks = sparks.SPARKSReader("testData/MOVES.DBF")
myExcel = ew.ExcelWriter("testData/test_excel_data.xlsx")

myStudbook = sb.Studbook()
myStudbook.add_header(exchangeSparks.fieldNames)
myStudbook.add_header(movesSparks.fieldNames)
myStudbook.add_records_from_list(exchangeSparks.get_records_as_list())


for move in movesSparks.get_records_as_list():
    returnValue = myStudbook.add_move(move)
    if returnValue is not "ADDED":
        print "ERROR, could not add this move ("+str(returnValue)+")"

for sire, dam in excelPairs.getRecordsAsList():
    myStudbook.add_chick_record(sire, dam)

myExcel.write_studbook(myStudbook)

myExcel.close()


