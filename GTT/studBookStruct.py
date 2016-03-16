import datetime


class Studbook:
    """These objects are base object for GTT. All reader and writer modules in
    this project use this to data structure for translating data from one
    format to another.

    Leveraging the capabilities of this project does not require any
    understanding of this data structure but if you are looking to create a new
    reader or writer you just need to read into and write from this structure
    """

    def __init__(self):
        """Initialize an Studbook: object.

        Returns:
           Studbook:
        """
        self.numberOfRecords = 0
        self.directory = []
        self.has_header = False
        self.header = []

    # assume that $move is (a list) a move line from Moves.dbf
    # return "ADDED" if it was added, "PRESENT" if already there, "FAIL" otherwise
    def add_move(self, move):
        """moves are an attribute of a studbook record. For convenience, we
        combine a few tasks to add a move to a record

        Args:
           move (list): each element in the list must contain a list containing a move record

        Returns:
           ADDED (str): a record was found that matched the move and the move was added to it
           FAIL (str): no record was found that matched the move
           PRESENT (str): a record was found that matched the move but the move was already present
        """

        my_stud_id = move[0]
        for record in self.directory:
            if record.data['STUD_ID'] == my_stud_id:
                return_value = record.has_move(move)
                if return_value == -1:
                    record.add_move(move)
                    return "ADDED"
                else:
                    return "PRESENT @ index", str(return_value)
        return "FAIL"

    def add_records_from_list(self, list_of_records):
        """Read in a list of records and add them all to this object

        Args:
           list_of_records (list):  Each element of the list is a list
           representing an entire row of data. In each internal list each
           element is a single column.

        Returns:
           nothing
        """

        if not self.has_header:
            print "you have to add a header before you can do any population of data!"
            return

        for record in list_of_records:
            sbr = StudbookRecord()
            sbr.set_metadata(self.header)
            sbr.populate_all_data(record, self.header)
            self.add_complete_record(sbr)

    def add_chick_record(self, sire, dam):
        """append a single record to this object based on a template chick data and input variables

        Args:
           sire (str): name of the sire to be considered (FIXME: check that these are supposed to be string/names)

           dam (str): name of the dam to be considered (FIXME: check that these are supposed to be string/names)

        Returns:
           nothing
        """

        if not self.has_header:
            print "you have to add a header before you can do any population of data!"
            return

        sbr = StudbookRecord()
        sbr.set_metadata(self.header)
        sbr.populate_new_chick_data(dam, sire)
        self.add_complete_record(sbr)

    def add_complete_record(self, record):
        """append a single record to this object

        Args:
           record (StudbookRecord): object to add to this object

        Returns:
           nothing
        """

        if not self.has_header:
            print "you have to add a header before you can do any population of data!"
            return

        if isinstance(record, StudbookRecord):
            self.directory.append(record)
        else:
            print "ERROR: records can only be of type studbookRecord!"

    def get_record(self, index):
        """return the record with the given index

        Args:
           index (int)

        Returns:
            StudbookRecord
        """
        return self.directory[index]

    def get_index_of_record(self, stud_id):
        """find the record that matches the input argument using the unique key
        `for the animal known as the 'stud_id'

        Args:
           stud_id (int): the stud_id of the animal to find.

        Returns:
            int: return the index of the (first) record that matches the input
            argument. If no match return -1
        """
        counter = 0
        for record in self.directory:
            if record.data['STUD_ID'] == stud_id:
                return counter
            counter += 1
        return -1

    def add_header(self, data):
        """ headers are the basic data validation object for studbooks. every
        studbookRecord must conform to header standards.

        Args:
           data (list):  each element in the list represents a single type of
           data. any records added to this studbook will contain data for each
           field of the header

        Returns:
           nothing
        """

        if self.has_header:
            print "ERROR: what the heck, we already have a header in this studbook!"
        else:
            self.header = data
            self.has_header = True


class StudbookRecord:
    """These objects are the internal records inside Studbook: objects. These
    objects should not be needed to be used directly by translators and can be
    considered internal/private objects
    """

    def __init__(self):
        """Initialize a studbookRecord: object"""

        self.created = False
        self.myMoves = []
        self.metadata = []
        self.data = {}

    def set_metadata(self, metadata):
        """populate all metadata fields with data from input argument
        Args:
           metadata (list):  each element of this list represents a data
           element for this record. All elements will be initialized to be
           empty strings

        Returns:
           nothing
        """
        for field in metadata:
            self.data[field] = ''
        self.metadata = metadata

    def populate_all_data(self, input_list, input_types):
        """given list: input_list, populate all internal data with the list.
        This is super dangerous as we're not really doing any checking
        TODO: fix error checking!

        Args:
           input_list (list):  each element of this list represents an internal
           data element of studbookRecord:
           input_types (list): each element of this list represents the type of
           field corresponding to the same location in input_list:

        Returns:
           nothing
        """

        if self.created:
            print "ERROR, Trying to re-assign the values for this record (this is way bad!)"

        i = 0
        for key in input_types:
            self.data[key] = input_list[i]
            i += 1

        self.created = True

    def populate_new_chick_data(self, dam_id, sire_id):
        """given a dam and sire (maw & paw) fill out this record with what the
        chick would be. We're currently really only using default values for a
        chick and adding the DAM and SIRE, not a lot of math is going on here
        to guess what a chick should 'be'

        Args:
           dam_id (str):  identifier of the DAM

           sire_id (str): identifier of the SIRE

        Returns:
           nothing
        """

        if self.created:
            print "ERROR, Trying to re-assign the values for this record (this is way bad!)"

        self.data['DAM_ID'] = dam_id
        self.data['SIRE_ID'] = sire_id
        self.data['STUD_ID'] = "H"+str(dam_id) + "_16"

        # default data
        self.data['BDATE'] = datetime.today().date()
        self.data['SEX'] = 5
        self.data['DATEIN'] = datetime.today().date()
        self.data['LOCATION'] = 'CHICK'
        self.data['SELECTED'] = 'TRUE'
        self.data['DEAD'] = 'FALSE'
        self.data['INBREED'] = 0
        self.data['AGE'] = 0
        self.data['KNOWN'] = -1
        self.data['INBREED_KN'] = -1
        self.data['MK'] = -1
        self.data['MK_KN'] = -1
        self.data['KV'] = -1
        self.data['KV_KN'] = -1
        self.data['VX'] = -1
        self.data['GU_ALL'] = -1
        self.data['GU_DESC'] = -1
        self.data['PR_LOST'] = 0
        self.data['COMMENT'] = '2016_HYPO_CHICK'

        self.created = True

    def has_move(self, move):
        """each studbookRecord has internal data representing 'moves', we are
        checking this record to see if we have a move that matches the input
        argument

        Args:
           move (list):  a move record

        Returns:
           int: Return the index of the match in this object's move list when
           found. If no match found then return -1
        """

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

    def add_move(self, move):
        """Without checking if it already exists, add the input argument to
        this object's move list.

        Args:
           move (list): move record to add

        Returns:
           nothing
        """

        self.myMoves.append(move)

    def get_record(self):
        """return all data from the record as a dictionary

        Returns:
           dictionary:
        """
        return self.data


        # self.data = OrderedDict([
        #             ('STUD_ID', ''),
        #             ('DAM_ID', ''),
        #             ('SIRE_ID', ''),
        #             ('BDATE', ''),
        #             ('BIRTH_EST', ''),
        #             ('SEX', ''),
        #             ('ID', ''),
        #             ('DID', ''),
        #             ('SID', ''),
        #             ('DATEIN', ''),
        #             ('IN_EST', ''),
        #             ('DATEOUT', ''),
        #             ('OUT_EST', ''),
        #             ('DEATHDATE', ''),
        #             ('DEATH_EST', ''),
        #             ('LOCATION', ''),
        #             ('LOCAL_ID', ''),
        #             ('INSTCODE', ''),
        #             ('SOCIALGRP', ''),
        #             ('SELECTED', ''),
        #             ('DEAD', ''),
        #             ('DAM_ID_TMP', ''),
        #             ('SIRE_IDTMP', ''),
        #             ('INBREED', ''),
        #             ('AGE', ''),
        #             ('KNOWN', ''),
        #             ('INBREED_KN', ''),
        #             ('MK', ''),
        #             ('MK_KN', ''),
        #             ('KV', ''),
        #             ('KV_KN', ''),
        #             ('VX', ''),
        #             ('GU_ALL', ''),
        #             ('GU_DESC', ''),
        #             ('PR_LOST', ''),
        #             ('COMMENT', '')
        #             ])
