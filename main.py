import sys
from API.Database_API import Database
from API.Login_API import Login
from API.Table_API import Table
sys.path.append("API")
sys.path.append("GUI")

# API
import Database_API
import Table_API
import Login_API

# GUI

userData = Login("UserData/login.csv")

db = Database(userData.getUsername(), userData.getPassword())
db.useDatabase("temp");

tb = Table(db.getDatabase())

tb.dropTable("salary");
tb.dropTable("employee");

tb.createTable("employee", "EMP_ID", "INT", ["Primary","Key"])
tb.createTable("salary", "salary_id", "INT" , [["FOREIGN", "KEY", "(salary_id)", "REFERENCES", "employee", "(EMP_ID)"], "NOT NULL"])
tb.addColumn("salary", "asdf", "INT");
tb.changeType("salary", "asdf", "VARCHAR(255)");
tb.removeColumn("salary", "asdf");
tb.describeTable("salary");

