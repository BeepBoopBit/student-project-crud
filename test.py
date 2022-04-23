import sys
from CRUD_API import CRUD


cd = CRUD();
cd.useDatabase("temp");


for i in cd.getDatabaseList():
    temp = CRUD();
    str = "%s" % i
    temp.useDatabase(str)
    for j in temp.getTableList():
        str1 = "%s" % j
        print(str1);