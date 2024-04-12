import psycopg2

from rich import print as printc
from rich.console import Console

def dbconfig():
  try:
    db = psycopg2.connect(
      host = 'localhost',
      user= 'password_manager',
      passwd = 'happynewyear'
      )
  except Exception as e:
    console.print_exception(show_locals =True)

  return db