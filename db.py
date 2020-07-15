import sqlite3

def ensure_connection(func):

    def inner(*args, **kwargs):
        with sqlite3.connect('my.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res
    return inner

@ensure_connection
def init_db(conn, force: bool = False):
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS user_base')

    c.execute('''
        CREATE TABLE IF NOT EXISTS item_base(
        id INTEGER PRIMARY KEY,
        item_name TEXT NOT NULL,
        item_price TEXT NOT NULL,
        item_city TEXT NOT NULL,
        item_state TEXT NOT NULL,
        item_category TEXT NOT NULL 
        )
    ''')

    conn.commit()

@ensure_connection
def delete_from_db(conn, id_to_delete):
    c = conn.cursor()
    c.execute('DELETE FROM item_base WHERE id = id_to_delete')
    conn.commit()

@ensure_connection
def add_message(conn, item_name: str, item_price: str, item_city: str, item_state: str, item_category: str):
    c = conn.cursor()
    c.execute('INSERT INTO item_base (item_name,item_price,item_city,item_state, item_category) VALUES (?, ?, ?, ?, ?)',
              (item_name,item_price,item_city,item_state, item_category))
    conn.commit()

@ensure_connection
def list_messages(conn):
    c = conn.cursor()
    c.execute("SELECT id,item_name,item_price,item_city,item_state, item_category FROM item_base")
    row = c.fetchall()
    return row

if __name__ == '__main__':
    init_db()

    add_message(item_name='kekDSFS', item_city='sda',item_price='231', item_state='sadasd', item_category='asd')
    add_message(item_name='sadas',item_city='12321',item_price='1312',item_state='sadsd', item_category='dasc')