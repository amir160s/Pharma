import sqlite3

class PharmacyDB:
    def __init__(self, db_name='pharmacy.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_medicine(self, manufacturer,dosages,name, generic_name,exp, price, quantity):
        self.cursor.execute("INSERT INTO Medicines (name, generic_name, manufacturer, price, quantity) VALUES (?, ?, ?, ?, ?)",
                            (manufacturer,dosages,name, generic_name,exp, price, quantity))
        self.conn.commit()

    def update_medicine(self, med_id, manufacturer,dosages,name, generic_name,exp, price, quantity):
        self.cursor.execute("UPDATE Medicines SET name=?, generic_name=?, manufacturer=?, price=?, quantity=? WHERE id=?",
                            (manufacturer,dosages,name, generic_name,exp, price, quantity, med_id))
        self.conn.commit()

    def delete_medicine(self, name):
        self.cursor.execute("DELETE FROM Medicines WHERE id=?", (name,))
        self.conn.commit()

    def fetch_medicines(self):
        self.cursor.execute("SELECT * FROM Medicines")
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
