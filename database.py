import sqlite3


class Person:
    def __init__(self, name, car):
        self.name = name.upper()
        self.car = car.upper()
        self.conn = sqlite3.connect('votes.db')
        self.cursor = self.conn.cursor()

    def save(self):
        self.cursor.execute(f"INSERT INTO votes VALUES ('{self.name}', '{self.car}')")
        self.conn.commit()


def getResults():
    connection = sqlite3.connect('votes.db')
    connCursor = connection.cursor()

    connCursor.execute("SELECT car FROM votes")

    votes = connCursor.fetchall()
    connection.commit()
    connection.close()

    result = {
        'Fronx': 0,
        'GrandVitara': 0,
        'Ertiga': 0,
        'Total': len(votes)
    }

    for vote in votes:
        if vote == ('FRONX',):
            result['Fronx'] += 1
        if vote == ('GRAND VITARA',):
            result['GrandVitara'] += 1
        if vote == ('ERTIGA',):
            result['Ertiga'] += 1
    return result


if __name__ == '__main__':
    conn = sqlite3.connect('votes.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE voting (name TEXT, car TEXT)")
    conn.commit()
    conn.close()
