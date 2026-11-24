# 🎓 Student Management System (SMS) — Python

A console-based **Student Management System** built in pure Python, using only the standard library. Add, view, update, delete and search student records, with data persisted locally in a text file. 📁

This is a Python port of the original Java project.

---

## ✨ Features

- ➕ **Add Student** — Create a new student record
- 📋 **View Students** — Display all stored student records
- ✏️ **Update Student** — Modify existing student details
- 🗑️ **Delete Student** — Remove a student record
- 🔍 **Search Student** — Look up a student by roll number
- 💾 **Save to File** — Persist student data to `students.txt`
- 🔄 **Load Data on Startup** — Previously saved records are loaded automatically

---

## 🛠️ Technologies Used

| Category | Details |
|---|---|
| 💻 Language | Python 3.9+ (standard library only) |
| 🗄️ Data Storage | Plain text / CSV-style file (`students.txt`) |
| ⚙️ Build Tool | None |

---

## 📂 Project Structure

```
student-management-system-python/
├── main.py
├── student/
│   ├── __init__.py
│   ├── execution.py
│   ├── sms.py
│   ├── student.py
│   └── students.txt
└── .gitignore
```

| Python file | Java original | Role |
|---|---|---|
| `main.py` | `Main.java` | Entry point |
| `student/execution.py` | `Execution.java` | Console menus and CRUD operations |
| `student/sms.py` | `SMS.java` | Loads data and runs the main menu loop |
| `student/student.py` | `Student.java` | Student model (a `dataclass`) |
| `student/students.txt` | `students.txt` | Persistent data (unchanged format) |

---

## ▶️ How to Run

```bash
python main.py
```

No installs or dependencies are needed. `students.txt` is found relative to the code, so you can run it from any folder (`python path/to/main.py`).

---

## 💽 File-Based Data Persistence

Each line of `students.txt` is one student:

```
roll_no,name,age,gender,branch,current_semester,email,phone
```

- **Loading:** records are read on startup (malformed lines are skipped with a message).
- **Saving:** choose option **6. Save Progress**. Exiting without saving discards the changes made in that session.

The file format is identical to the Java version, so existing data files work as-is.

---

## 🔄 What Changed from the Java Version

- **Portable file path** — the Java code hard-coded `D:/B.Tech/fullstack/springboot/projects/SMS/src/student/students.txt`. The Python version locates `students.txt` next to the code.
- **Input handling** — Python's `input()` reads whole lines, so the Java `Scanner` problems (`nextInt()` followed by `nextLine()` skipping inputs, and names with spaces being cut at the first word in Update) don't occur.
- **Validation** — non-numeric input for numeric fields now re-prompts instead of crashing.
- **Search** — the Java check `roll number > number of students` wrongly rejected valid roll numbers after a deletion; it now just reports "not found".
- **CSV module** — reading/writing uses `csv`, so a name containing a comma no longer corrupts the file.

Menus, messages, field order and roll-number assignment (`max + 1`) are otherwise unchanged.

---

## 🖥️ Example Console Output

```
Data loaded Successfully

----------Student Management System----------
           ------Features------
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Update Student
6. Save Progress
7. Exit
NOTE : Exiting without save progress doesnot save the changes did till now
--------------------------------------------------------------------------
Enter your choice : 3
Enter the roll number of the student to be searched : 
1
--------------------------------------------------------------------------
Roll Number : 1
Name : Vivek
Age : 19
Gender : Male
Branch : CSE
Current Semester : 5
Email : vivek@java.com
Phone Number : 9123456781
--------------------------------------------------------------------------
```

---

## 🚧 Future Improvements

- 🗄️ Replace text file storage with a database (e.g., SQLite)
- 🖼️ Add a GUI (Tkinter) or a web front end
- 🔃 Add sorting options (by name, ID, or semester)
- 🧪 Add unit tests (`pytest`) for the CRUD operations

---

## 👨‍💻 Author

**Vivek Boyina**<br>
Computer Science Engineering Undergraduate
