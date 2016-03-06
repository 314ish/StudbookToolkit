from dbfpy import dbf


class SPARKSReader:

    def __init__(self,filename):
        self.db = dbf.Dbf(filename)
        self.fieldNames=self.db.fieldNames

    def getRecordsAsList(self):
        returnMe = []
        for record in self.db:
            returnMe.append(record.fieldData)
        return returnMe
