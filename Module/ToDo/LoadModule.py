import sqlite3
import os


def load():
    if not os.path.isdir("ToDo.db"):
        con = sqlite3.connect("ToDo.db")
        cur = con.cursor()

        cur.execute("CREATE TABLE lite_task (id INTEGER PRIMARY KEY, header TEXT, status BOOLEAN)")
