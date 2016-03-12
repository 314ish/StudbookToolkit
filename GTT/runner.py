"""
Created on 27  2013

@author:
"""

import sparks as sparks
import excel as ew
import studBookStruct as sb


excelPairs = ew.excelReader("testData/2016_pairs.xlsx")
exchangeSparks = sparks.SPARKSReader("testData/EXCHANGE.DBF")
movesSparks = sparks.SPARKSReader("testData/MOVES.DBF")
myExcel = ew.excelWriter("testData/test.xlsx")

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

myExcel.writeStudbook(myStudbook)

myExcel.close()


