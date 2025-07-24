import sqlite3
def init_db():
    conn=sqlite3.connect("typing.db")
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                wpm INTEGER,
                accuracy REAL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                ''')
    conn.commit()
    conn.close()
def ins(name,wpm,accuracy):
    conn=sqlite3.connect("typing.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO leaderboard (name,wpm,accuracy) VALUES(?,?,?)",(name,wpm,accuracy))
    conn.commit()
    conn.close()
def gts(limit=5):
    conn=sqlite3.connect("typing.db")
    cur=conn.cursor()
    cur.execute("SELECT name,wpm,accuracy,date FROM leaderboard ORDER BY wpm DESC LIMIT ?",(limit,))
    results=cur.fetchall()
    conn.close()
    return results