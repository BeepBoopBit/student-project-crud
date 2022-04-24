import sys
from CRUD_API import CRUD

cd = CRUD();
cd.useDatabase("temp");
cd.insertValue("water", "5")
for i in cd.getTableList():
    print(i);
    for k in cd.getAllData(i):
        print(k);
        
        
cd.commit();