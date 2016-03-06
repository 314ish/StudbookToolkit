from collections import OrderedDict
from datetime import *

class studbook:

    def __init__(self):
        self.numberOfRecords = 0
        self.directory = []
        self.header = []

    # assuming each entry in the list is a complete record, add all the records to the studbook
    def addRecordsFromList(self, listOfRecords):
        for record in listOfRecords:
            sbr = studbookRecord()
            sbr.populateAllData(record)
            self.addRecord(sbr)

    # add a single record to the studbook based on template chick data (and provided $sire & $dam)
    def addChickRecord(self, sire, dam):
        sbr = studbookRecord()
        sbr.populateNewChickData(dam, sire)
        self.addRecord(sbr)

    # add a single record of type studbookRecord
    def addRecord(self, record):
        if isinstance(record, studbookRecord):
            self.directory.append(record)
        else:
            print "ERROR: records can only be of type studbookRecord!"

    # assume that $move is (a list) a move line from Moves.dbf
    # return "ADDED" if it was added, "PRESENT" if already there, "FAIL" otherwise
    def addMove(self, move):
        mSTUD_ID = move[0]
        for record in self.directory:
            if record.data['STUD_ID'] == mSTUD_ID:
                returnValue = record.hasMove(move)
                if returnValue == -1:
                    record.addMove(move)
                    return "ADDED"
                else:
                    return "PRESENT @ index", str(returnValue)
        return "FAIL"

    # headers are a simple list (to be printed 1-entry per row)
    def addHeader(self, data):
        self.header.append(data)


class studbookRecord:

    def __init__(self):
        self.created = False
        self.myMoves = []
        self.data = OrderedDict([
                    ('STUD_ID', ''),
                    ('DAM_ID', ''),
                    ('SIRE_ID', ''),
                    ('BDATE', datetime.today().date()),
                    ('BIRTH_EST', ''),
                    ('SEX', 5),
                    ('ID', ''),
                    ('DID', ''),
                    ('SID', ''),
                    ('DATEIN', datetime.today().date()),
                    ('IN_EST', ''),
                    ('DATEOUT', ''),
                    ('OUT_EST', ''),
                    ('DEATHDATE', ''),
                    ('DEATH_EST', ''),
                    ('LOCATION', 'CHICK'),
                    ('LOCAL_ID', ''),
                    ('INSTCODE', ''),
                    ('SOCIALGRP', ''),
                    ('SELECTED', 'TRUE'),
                    ('DEAD', 'FALSE'),
                    ('DAM_ID_TMP', ''),
                    ('SIRE_IDTMP', ''),
                    ('INBREED', 0),
                    ('AGE', 0),
                    ('KNOWN', -1),
                    ('INBREED_KN', -1),
                    ('MK', -1),
                    ('MK_KN', -1),
                    ('KV', -1),
                    ('KV_KN', -1),
                    ('VX', -1),
                    ('GU_ALL', -1),
                    ('GU_DESC', -1),
                    ('PR_LOST', 0),
                    ('COMMENT', '2016_HYPO_CHICK')
                    ])

    # this assumes that the $inputList has exactly enough data to fill the database and is in the right order
    def populateAllData(self, inputList):

        if self.created:
            print "ERROR, Trying to re-assign the values for this record (this is way bad!)"

        i = 0
        for key in self.data.keys():
            self.data[key] = inputList[i]
            i += 1

        self.created = True

    def populateNewChickData(self, DAM_ID, SIRE_ID):
        if self.created:
            print "ERROR, Trying to re-assign the values for this record (this is way bad!)"

        self.data['DAM_ID'] = DAM_ID
        self.data['SIRE_ID'] = SIRE_ID
        self.data['STUD_ID'] = "H"+str(DAM_ID)+"_16"

        self.created = True


    # does this record have a move that matches $move
    # return -1 if not present, otherwise return the index of which move matches
    def hasMove(self, move):
        counter = 0
        for sMove in self.myMoves:
            counter += 1
            i = 0
            match = True
            while i < len(sMove):
                if not sMove[i] == move[i]:
                    match = False
                    break
                i += 1
            if match:
                return counter-1  # index is 1 less than counter
        return -1  # no matches found, return -1


    # blindly add $move to self.myMoves (without checking if $move
    # already is in this record)
    def addMove(self, move):
        self.myMoves.append(move)

    def returnExcelFormat(self):
        returnMe = []

        # first, get the 'main' row of data
        row = []
        for key in self.data.keys():
            row.append(self.data[key])
        returnMe.append(row)

        # now get all the 'moves' rows
        row = []
        for move in self.myMoves:
            returnMe.append(move)

        return returnMe



class studbookPairs:

    def __init__(self):
        self.numberOfRecords = 0
        self.directory = []
        self.header = ""

    def readPairsFromFile(self, pairFile):
        return True
        # read pairs from $pairFile into list of lists
