import sqlite3

class Ma'lumotlarBazasi:
    def __init__(self, nom):
        self.nom = nom
        self.baza = sqlite3.connect(nom)
        self.cursor = self.baza.cursor()

    def yarat(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ma'lumotlar (
                id INTEGER PRIMARY KEY,
                ism TEXT NOT NULL,
                familiya TEXT NOT NULL,
                yosh INTEGER NOT NULL
            )
        """)
        self.baza.commit()

    def qo'sh(self, ism, familiya, yosh):
        self.cursor.execute("INSERT INTO ma'lumotlar (ism, familiya, yosh) VALUES (?, ?, ?)", (ism, familiya, yosh))
        self.baza.commit()

    def o'chir(self, id):
        self.cursor.execute("DELETE FROM ma'lumotlar WHERE id = ?", (id,))
        self.baza.commit()

    def o'zgartir(self, id, ism, familiya, yosh):
        self.cursor.execute("UPDATE ma'lumotlar SET ism = ?, familiya = ?, yosh = ? WHERE id = ?", (ism, familiya, yosh, id))
        self.baza.commit()

    def chiqar(self):
        self.cursor.execute("SELECT * FROM ma'lumotlar")
        return self.cursor.fetchall()

    def yop(self):
        self.baza.close()

bazasi = Ma'lumotlarBazasi("ma'lumotlar.db")
bazasi.yarat()

while True:
    print("1. Qo'sh")
    print("2. O'chir")
    print("3. O'zgartir")
    print("4. Chiqar")
    print("5. Yop")
    print("6. Chiqish")
    tanlov = input("Tanlovni kiriting: ")

    if tanlov == "1":
        ism = input("Ismni kiriting: ")
        familiya = input("Familiyani kiriting: ")
        yosh = int(input("Yoshni kiriting: "))
        bazasi.qo'sh(ism, familiya, yosh)
    elif tanlov == "2":
        id = int(input("Idni kiriting: "))
        bazasi.o'chir(id)
    elif tanlov == "3":
        id = int(input("Idni kiriting: "))
        ism = input("Ismni kiriting: ")
        familiya = input("Familiyani kiriting: ")
        yosh = int(input("Yoshni kiriting: "))
        bazasi.o'zgartir(id, ism, familiya, yosh)
    elif tanlov == "4":
        ma'lumotlar = bazasi.chiqar()
        for ma'lumot in ma'lumotlar:
            print(ma'lumot)
    elif tanlov == "5":
        bazasi.yop()
        break
    elif tanlov == "6":
        break
    else:
        print("Xato tanlov!")
```

Bu kodda biz SQLite3 kutubxonasidan foydalanib oddiy ma'lumotlar bazasi yaratib, CRUD (Create, Read, Update, Delete) amallarini bajaramiz.
