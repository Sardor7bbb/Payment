from database import Database

def create():

    users = """
    CREATE TABLE users (
    user_id SERIAL  PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    card_number VARCHAR(16),
    expiration VARCHAR(6),
    phone_number VARCHAR(10),
    password VARCHAR(8),
    create_date TIMESTAMP DEFAULT now());
    """


    payment_status = """
    CREATE TABLE  payment_status (
    payment_status_id SERIAL  PRIMARY KEY,
    status BOOLEAN ,
    create_date TIMESTAMP DEFAULT now());"""


    payments = """
    CREATE TABLE payment (
    payment_id SERIAL  PRIMARY KEY,
    payment_status_id INT REFERENCES payment_status(payment_status_id),
    user_id INT REFERENCES users(user_id),
    history TEXT,
    create_date TIMESTAMP DEFAULT now());"""

    data = {
        "users": users,
        'payment_status': payment_status,
        "payments": payments
    }

    for i in data:
        print(f"{i} => {Database.connect(data[i], 'create')}")


if __name__ == "__main__":
    create()