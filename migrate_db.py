import sqlite3

def add_column():
    conn = sqlite3.connect('purchase_system.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE requests ADD COLUMN requester_name TEXT")
        conn.commit()
        print("Column 'requester_name' added successfully.")
    except sqlite3.OperationalError as e:
        print(f"Error (maybe column exists): {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    add_column()
