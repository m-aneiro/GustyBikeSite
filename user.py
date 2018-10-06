from collections import OrderedDict

from werkzeug.security import check_password_hash


class user:

    @staticmethod
    def exists(username, db):
        db.get_cursor().execute("SELECT id FROM users WHERE username = %s", (username))

        count = db.get_cursor().rowcount

        return count == 1

    @staticmethod
    def create(email, password, username, db):
        db.get_cursor().execute(
            "INSERT INTO users (email, password, username) VALUES (%s, %s, %s) RETURNING id",
            (email, password, username))

        generated = db.get_cursor().fetchone()[0]

        db.commit()

        return generated

    @staticmethod
    def check_password(username, password, db):
        db.get_cursor().execute("SELECT password FROM users WHERE username = %s", (username,))

        row = db.get_cursor().fetchone()

        if db.get_cursor().rowcount < 1:
            return False

        correct_pw = row[0]

        return check_password_hash(correct_pw, password)

    def __init__(self, id, db, username=None):
        self.db = db
        self.id = id

        if username is None:
            self.db.get_cursor().execute("SELECT * FROM users WHERE id = %s", (id,))

            row = self.db.get_cursor().fetchone()

            self.username = row["username"]
        else:
            self.username = username

