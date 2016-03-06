import excel as ew
import studBookStruct as sb
import SPARKSReader as sparks



excelPairs = ew.excelReader("2016_pairs.xlsx")
exchangeSparks = sparks.SPARKSReader("EXCHANGE.DBF")
movesSparks = sparks.SPARKSReader("MOVES.DBF")
myExcel = ew.excelWriter("test")

myStudbook = sb.studbook()
myStudbook.addHeader(exchangeSparks.fieldNames)
myStudbook.addHeader(movesSparks.fieldNames)
myStudbook.addRecordsFromList(exchangeSparks.getRecordsAsList())


for move in movesSparks.getRecordsAsList():
    returnValue = myStudbook.addMove(move)
    if returnValue is not "ADDED":
        print "ERROR, could not add this move ("+str(returnValue)+")"


for sire, dam in excelPairs.getRecordsAsList():
    myStudbook.addChickRecord(sire,dam)

myExcel.writeStudbook(myStudbook)

myExcel.close()


