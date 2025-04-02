import sqlite3
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# === Загрузка .env или создание, если его нет ===
load_dotenv()
env_path = ".env"

key_str = os.getenv("FERNET_KEY")
if not key_str:
    new_key = Fernet.generate_key().decode()
    with open(env_path, "a") as f:
        f.write(f"\nFERNET_KEY={new_key}\n")
    key_str = new_key
    print("[+] Новый ключ сгенерирован и записан в .env")

key = key_str.encode()
fernet = Fernet(key)

# === Шифрование/расшифровка ===
def encrypt(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt(token: str) -> str:
    return fernet.decrypt(token.encode()).decode()

# === Работа с SQLite ===
conn = sqlite3.connect('storage.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vault (
    name TEXT PRIMARY KEY,
    login TEXT,
    encrypted_password TEXT
)
''')

def save_generated(name, login, password):
    encrypted = encrypt(password)
    with sqlite3.connect('storage.db') as conn:
        cursor = conn.cursor()
        cursor.execute('REPLACE INTO vault (name, login, encrypted_password) VALUES (?, ?, ?)',
                       (name, login, encrypted)
                       )
        conn.commit()
    print(f"[{name}] сохранено.")


def get_entry(name):
    with sqlite3.connect('storage.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT login, encrypted_password FROM vault WHERE name = ?', (name,))
        row = cursor.fetchone()
        if row:
            login, encrypted = row
            password = decrypt(encrypted)
            print(f"\n[{name}]\n\nLogin: {login}\nPassword: {password}")
        else:
            print("\nНе найдено.")


def list_names():
    with sqlite3.connect('storage.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM vault')
        rows = cursor.fetchall()
        return [name for (name,) in rows]