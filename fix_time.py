
import sqlite3
from datetime import datetime, timedelta

def fix_timezone():
    conn = sqlite3.connect('purchase_system.db')
    cursor = conn.cursor()
    
    # Get all requests
    cursor.execute("SELECT id, created_at FROM requests")
    rows = cursor.fetchall()
    
    for row_id, created_at in rows:
        if created_at:
            try:
                # SQLite DateTime usually looks like '2026-02-05 07:05:00.000000'
                # or '2026-02-05 07:05:00'
                dt = datetime.strptime(created_at.split('.')[0], '%Y-%m-%d %H:%M:%S')
                # Add 3 hours to compensate for UTC vs Local (+3)
                new_dt = dt + timedelta(hours=3)
                cursor.execute("UPDATE requests SET created_at = ? WHERE id = ?", (new_dt.strftime('%Y-%m-%d %H:%M:%S'), row_id))
            except Exception as e:
                print(f"Error updating row {row_id}: {e}")
    
    conn.commit()
    print("Timezone correction complete for existing records.")
    conn.close()

if __name__ == "__main__":
    fix_timezone()
