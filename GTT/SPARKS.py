from dbfpy import dbf


class SPARKSReader:
    """These objects can be used to read SPARKS formatted files. SPARKS uses the dBase format for data storage
     For more information on SPARKS see http://www2.isis.org/support/SPARKS/Pages/home.aspx
     For more information on dBase see https://en.wikipedia.org/wiki/.dbf
    """
    def __init__(self,filename):
        """Initialize an excelReader: object.

        Args:
           name (str):  name of the file to read from

        Returns:
           excelWriter:
        """        self.db = dbf.Dbf(filename)
        self.fieldNames=self.db.fieldNames

    def getRecordsAsList(self):
        """Initialize an excelReader: object.

        Args:
           name (str):  name of the file to read from

        Returns:
           excelWriter:
        """
        returnMe = []
        for record in self.db:
            returnMe.append(record.fieldData)
        return returnMe
