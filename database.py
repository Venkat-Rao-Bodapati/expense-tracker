import sqlite3

def get_connection():
    conn = sqlite3.connect("data")
    conn.row_factory = sqlite3.Row
    return conn

# create tables
def initialize_db():
    conn=get_connection()
    cursor=conn.cursor()
    with open("schema.sql","r") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

# add a record
def add_record(field1, field2, field3,field4):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO expenses (amount,category,description,expense_date)
            VALUES (?, ?, ?,?)
        """, (field1, field2, field3,field4))
        conn.commit()
        print("\n✅ Record added successfully!")
    except sqlite3.IntegrityError as e:
        print(f"\n❌ Error: {e}")
    finally:
        conn.close()


# ─── VIEW all records ──────────────────────────────────────────
def view_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()
    conn.close()
    return records

# ─── SEARCH records ────────────────────────────────────────────
def search_record(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM expenses
        WHERE category LIKE ? OR description LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    conn.close()
    return results

# ─── UPDATE a record ───────────────────────────────────────────
def update_record(record_id, field1, field2, field3,field4):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE expenses
        SET amount=?, category=?, description=?, expense_date=?
        WHERE id=?
    """, (field1, field2, field3,field4, record_id))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    if updated:
        print(f"\n✅ Record {record_id} updated successfully!")
    else:
        print(f"\n❌ Record ID {record_id} not found.")

# ─── DELETE a record ───────────────────────────────────────────
def delete_record(record_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id=?", (record_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    if deleted:
        print(f"\n✅ Record {record_id} deleted successfully!")
    else:
        print(f"\n❌ Record ID {record_id} not found.")

