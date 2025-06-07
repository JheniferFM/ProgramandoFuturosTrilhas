# models.py
from database import connect_db

class User:
    def __init__(self, id=None, username=None, password=None, role='learner'):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    @staticmethod
    def get_by_id(user_id):
        with connect_db() as db:
            user_data = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
            if user_data:
                return User(**user_data)
        return None

    @staticmethod
    def get_by_username(username):
        with connect_db() as db:
            user_data = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            if user_data:
                return User(**user_data)
        return None

    def save(self):
        with connect_db() as db:
            if self.id:
                db.execute('UPDATE users SET username = ?, password = ?, role = ? WHERE id = ?',
                           (self.username, self.password, self.role, self.id))
            else:
                cursor = db.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                                    (self.username, self.password, self.role))
                self.id = cursor.lastrowid
            db.commit()

class Trail:
    def __init__(self, id=None, title=None, description=None, difficulty=None, creator_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.creator_id = creator_id

    @staticmethod
    def get_all():
        with connect_db() as db:
            trails_data = db.execute('SELECT * FROM trails').fetchall()
            return [Trail(**trail_data) for trail_data in trails_data]

    @staticmethod
    def get_by_id(trail_id):
        with connect_db() as db:
            trail_data = db.execute('SELECT * FROM trails WHERE id = ?', (trail_id,)).fetchone()
            if trail_data:
                return Trail(**trail_data)
        return None

    def save(self):
        with connect_db() as db:
            if self.id:
                db.execute('UPDATE trails SET title = ?, description = ?, difficulty = ?, creator_id = ? WHERE id = ?',
                           (self.title, self.description, self.difficulty, self.creator_id, self.id))
            else:
                cursor = db.execute('INSERT INTO trails (title, description, difficulty, creator_id) VALUES (?, ?, ?, ?)',
                                    (self.title, self.description, self.difficulty, self.creator_id))
                self.id = cursor.lastrowid
            db.commit()

    def get_modules(self):
        with connect_db() as db:
            modules_data = db.execute('SELECT * FROM modules WHERE trail_id = ? ORDER BY id ASC', (self.id,)).fetchall()
            return [Module(**module_data) for module_data in modules_data]

class Module:
    def __init__(self, id=None, trail_id=None, title=None, content=None):
        self.id = id
        self.trail_id = trail_id
        self.title = title
        self.content = content

    @staticmethod
    def get_by_id(module_id):
        with connect_db() as db:
            module_data = db.execute('SELECT * FROM modules WHERE id = ?', (module_id,)).fetchone()
            if module_data:
                return Module(**module_data)
        return None

    def save(self):
        with connect_db() as db:
            if self.id:
                db.execute('UPDATE modules SET trail_id = ?, title = ?, content = ? WHERE id = ?',
                           (self.trail_id, self.title, self.content, self.id))
            else:
                cursor = db.execute('INSERT INTO modules (trail_id, title, content) VALUES (?, ?, ?)',
                                    (self.trail_id, self.title, self.content))
                self.id = cursor.lastrowid
            db.commit()