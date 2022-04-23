from dataclasses import dataclass
from pydoc import describe
import MySQLdb

class Select:
    def __init__(self, db, tb) -> None:
        self.db = db
        self.cursor = self.db.cursor()
    
    #just get all
    def getAllData(self):
        pass
    
    # with constraints 
    def getData(self):
        pass
    
    def getDataGroupedBy(self):
        pass
    
    def getDataSortedBy(self):
        pass
    