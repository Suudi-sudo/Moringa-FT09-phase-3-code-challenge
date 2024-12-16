from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
<<<<<<< HEAD

    # Create authors table
=======
    
>>>>>>> parent of 2934b6d (complete code challenge)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
<<<<<<< HEAD

    # Create magazines table
=======
>>>>>>> parent of 2934b6d (complete code challenge)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
<<<<<<< HEAD

    # Create articles table
=======
>>>>>>> parent of 2934b6d (complete code challenge)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (id)
        )
    ''')

<<<<<<< HEAD
    # Commit and close connection
=======
>>>>>>> parent of 2934b6d (complete code challenge)
    conn.commit()
    conn.close()

# CRUD operations for authors

def create_author(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO authors (name) VALUES (?)
    ''', (name,))
    conn.commit()
    conn.close()

def get_author(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM authors WHERE id = ?
    ''', (id,))
    author = cursor.fetchone()
    conn.close()
    return author

def update_author(id, name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE authors SET name = ? WHERE id = ?
    ''', (name, id))
    conn.commit()
    conn.close()

def delete_author(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM authors WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

# CRUD operations for magazines

def create_magazine(name, category):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO magazines (name, category) VALUES (?, ?)
    ''', (name, category))
    conn.commit()
    conn.close()

def get_magazine(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM magazines WHERE id = ?
    ''', (id,))
    magazine = cursor.fetchone()
    conn.close()
    return magazine

def update_magazine(id, name, category):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE magazines SET name = ?, category = ? WHERE id = ?
    ''', (name, category, id))
    conn.commit()
    conn.close()

def delete_magazine(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM magazines WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

# CRUD operations for articles

def create_article(title, author_id, magazine_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)
    ''', (title, author_id, magazine_id))
    conn.commit()
    conn.close()

def get_article(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM articles WHERE id = ?
    ''', (id,))
    article = cursor.fetchone()
    conn.close()
    return article

def update_article(id, title, author_id, magazine_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?
    ''', (title, author_id, magazine_id, id))
    conn.commit()
    conn.close()

def delete_article(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM articles WHERE id = ?
    ''', (1,))
    conn.commit()
    conn.close()
