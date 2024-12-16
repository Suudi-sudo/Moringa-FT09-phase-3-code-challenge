from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self._title = None  # Initialize _title to avoid AttributeError
        print(f"Initializing Article with title: '{title}' (Length: {len(title)})")  # Debugging line
        self.title = title  # This will invoke the setter for title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

        # Creating a new article entry in the database when initializing
        self.create_article()

    def __repr__(self):
        return f'<Article {self.title}>'

    # Creating a new article in the database
    def create_article(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        ''', (self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        conn.close()

    # Property to get article's title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        print(f"Setting title: '{value}' (Length: {len(value)})")  # Debugging line
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    # Method to retrieve the author of the article from the database
    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM authors WHERE id = ?
        ''', (self.author_id,))
        author_data = cursor.fetchone()
        conn.close()
        return author_data

    # Method to retrieve the magazine of the article from the database
    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM magazines WHERE id = ?
        ''', (self.magazine_id,))
        magazine_data = cursor.fetchone()
        conn.close()
        return magazine_data
