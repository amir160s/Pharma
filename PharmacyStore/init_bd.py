import sqlite3

def init_db():
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Medicines (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        generic_name TEXT NOT NULL,
                        manufacturer TEXT NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL)''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
