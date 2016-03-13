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

myStudbook = sb.studbook()
myStudbook.addHeader(exchangeSparks.fieldNames)
myStudbook.addHeader(movesSparks.fieldNames)
myStudbook.addRecordsFromList(exchangeSparks.getRecordsAsList())


for move in movesSparks.getRecordsAsList():
    returnValue = myStudbook.addMove(move)
    if returnValue is not "ADDED":
        print "ERROR, could not add this move ("+str(returnValue)+")"

for sire, dam in excelPairs.getRecordsAsList():
    myStudbook.addChickRecord(sire, dam)

myExcel.write_studbook(myStudbook)

myExcel.close()


