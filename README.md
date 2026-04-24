# 🔐 Simple Password Manager (Python CLI)

A beginner-friendly command-line password manager built with Python.
This project allows you to store, view, update, and delete passwords directly from the terminal.

---

## 📌 Features

* ➕ Add new passwords
* 📋 View all saved passwords
* 🔄 Change existing passwords
* ❌ Delete passwords
* 🧭 Simple menu-based navigation

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/password-manager.git
cd password-manager
```

### 2. Run the program

```bash
python main.py
```

---

## 🖥️ How It Works

When you run the program, you’ll see a menu like this:

```
Welcome to your password manager
1. Add a password
2. View all password
3. Change a password
4. Delete password
```

---

## 📸 Example Output

```
Wlcome to your password manager
1. Add a password
2. View all password
3. Change a password
4. Delete password
Enter your choise: 1
Add password
Enter site name: Gmail
Enter site domain: someone@gamil.com (gmail.com)
Enter site password: 12345
Site successfully added

Wlcome to your password manager
1. Add a password
2. View all password
3. Change a password
4. Delete password
Enter your choise: 1
Add password
Enter site name: Facebook
Enter site domain: facebook.com
Enter site password: 123
Site successfully added

Wlcome to your password manager
1. Add a password
2. View all password
3. Change a password
4. Delete password
Enter your choise: 2
View all password
1.
Site number: 1
Site name: Gmail
Site domain: someone@gamil.com (gmail.com)
Site password: 12345
------------------------------------------
2.
Site number: 2
Site name: Facebook
Site domain: facebook.com
Site password: 123
------------------------------------------

Wlcome to your password manager
1. Add a password
2. View all password
3. Change a password
4. Delete password
Enter your choise: 3
Change a password
Enter site number: 2
No site found
Site number: 2
Site name: Facebook
Site domain: facebook.com
Site password: 123
Enter new password: 000000000
Password successfully changed

Wlcome to your password manager
1. Add a password
2. View all password
3. Change a password
4. Delete password
Enter your choise: 2
View all password
1.
Site number: 1
Site name: Gmail
Site domain: someone@gamil.com (gmail.com)
Site password: 12345
------------------------------------------
2.
Site number: 2
Site name: Facebook
Site domain: facebook.com
Site password: 000000000
------------------------------------------

Wlcome to your password manager
1. Add a password
2. View all password
3. Change a password
4. Delete password
Enter your choise: 4
Delete a password
Enter the site number: 1
Site number: 1
Site name: Gmail
Site domain: someone@gamil.com (gmail.com)
Site password: 12345
Press 1 to delete or 0 to back: 1
Password successfully deleted

Wlcome to your password manager
1. Add a password
2. View all password
3. Change a password
4. Delete password
Enter your choise: 2
View all password
1.
Site number: 2
Site name: Facebook
Site domain: facebook.com
Site password: 000000000
------------------------------------------
```

---

## 📂 Data Storage

* Passwords are stored **in memory (list)** during runtime
* ⚠️ Data is lost when the program exits

---

## ⚠️ Limitations

* No encryption (plain text passwords)
* No persistent storage
* Limited input validation
* Minor logic issues may still exist

---

## 🛠️ Future Improvements

* Save passwords to a file (JSON/database)
* Add encryption
* Improve input validation
* Better menu loop (avoid recursion)
* Search by site name

---

## 🧑‍💻 Built With

* Python (no external libraries)

---

## 📄 License

Free to use and modify.

---

## 💡 Author

Your Name
GitHub: https://github.com/has6237

---

⭐ Star the repo if you found it useful!
