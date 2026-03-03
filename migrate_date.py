
import sqlite3

def migrate():
    conn = sqlite3.connect('purchase_system.db')
    cursor = conn.cursor()
    
    try:
        # Add created_at column. SQLite doesn't support DEFAULT with complex expressions in ALTER TABLE easily, 
        # but for DateTime we can just add it and it will be NULL for old ones, 
        # then we can populate it.
        cursor.execute("ALTER TABLE requests ADD COLUMN created_at DATETIME")
        conn.commit()
        print("Column 'created_at' added successfully.")
        
        # Populate existing rows with current time
        from datetime import datetime
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("UPDATE requests SET created_at = ? WHERE created_at IS NULL", (now,))
        conn.commit()
        print("Existing rows updated with current timestamp.")
        
    except sqlite3.OperationalError as e:
        print(f"Notice: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
