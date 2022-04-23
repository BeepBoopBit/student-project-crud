import sys
sys.path.append("API")
sys.path.append("GUI")

# API
import Database_API
import Table_API


db = Database_API.Database();
db.useDatabase("temp");

tb = Table_API.Table(db.getDatabase());

tb.createTable("shemay", "shit", "int", "Primary Key");
for i in tb.getTable():
    print(i);




