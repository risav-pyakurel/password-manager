from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console

def config():
  #creating a database
  db = dbconfig()
  cursor = db.cursor()

  try:
    cursor.execute("CREATE DATABASE password_manager")
  except Exception as e:
    printc("[red][!] An error occured while trying to create db. ")
    console.print_exception(show_locals = True)
    sys.exit(0)



