import csv


class Login_API:
    def __init__(self, dataPath) -> None:
        file = open(dataPath);
        csvreader = csv.reader(file);
        # should only contains one row
        header = next(csvreader);
        self.user = header[0];
        self.password = header[1];
        
    def getUsername(self):
        return self.user
    
    def getPassword(self):
        return self.password