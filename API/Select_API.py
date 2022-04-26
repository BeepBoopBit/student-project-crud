from dataclasses import dataclass
from pydoc import describe

class Select_API:
    def __init__(self, db, tb) -> None:
        self.db = db
        self.cursor = self.db.cursor(dictionary=True)
        self.tb = tb;
    
    # Getters
    def getAllData(self, tbName):
        self.cursor.execute(f"SELECT * FROM {tbName};")
        return self.__formatValue();

    def getData(self, tbName, condition):
        self.cursor.execute(f"SELECT * FROM {tbName} WHERE {condition};")
        return self.__formatValue();
    
    def getDataFrom(self, tbName, columnName):
        self.cursor.execute(f"SELECT {columnName} FROM {tbName};")
        return self.__formatValue();
    
    def getDataGroupedBy(self, tbName, condition, conditionGroup):
        self.cursor.execute(f"SELECT * FROM {tbName} WHERE {condition} GROUP BY {conditionGroup};");
        return self.__formatValue();
    
    def getDataSortedBy(self, tbName, condition, conditionSort):
        self.cursor.execute(f"SELECT * FROM {tbName} WHERE {condition} ORDERED BY {conditionSort} ;")
        return self.__formatValue();
    
    # Auxillary
    def __formatValue(self):
        temp = []
        for i in self.cursor.fetchall():
            for j in i.values():
                temp.append(j);
        return temp;