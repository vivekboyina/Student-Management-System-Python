import csv
from pathlib import Path

from .student import DIVIDER, Student

# option number -> (prompt, Student attribute, converter)
UPDATE_FIELDS = {
    1: ("Enter the new name : ", "name", str),
    2: ("Enter the new age : ", "age", int),
    3: ("Enter the correct gender : ", "gender", str),
    4: ("Enter the new branch : ", "branch", str),
    5: ("Enter the Current Semester : ", "curr_sem", int),
    6: ("Enter the new email : ", "email", str),
    7: ("Enter the new phone number : ", "phno", str),
}


def read_int(prompt: str) -> int:
    """Prompt until the user types a whole number."""
    while True:
        raw = input(prompt)
        try:
            return int(raw.strip())
        except ValueError:
            print("Please enter a valid number.")


class Execution:
    """Console menu and user interaction."""

    def __init__(self, data_file: Path):
        self.data_file = Path(data_file)

    # ---------- menus ----------
    def display(self) -> None:
        print("----------Student Management System----------")
        print("           ------Features------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Save Progress")
        print("7. Exit")
        print("NOTE : Exiting without save progress doesnot save the changes did till now")
        print(DIVIDER)

    def next_opt(self) -> int:
        self.display()
        return read_int("Enter your choice : ")

    def display2(self) -> None:
        print(DIVIDER)
        print("-----Select Entity-----")
        print("1. Name")
        print("2. Age")
        print("3. Gender")
        print("4. Branch")
        print("5. Current Semester")
        print("6. Email")
        print("7. Phone Number")
        print("8. Exit")
        print(DIVIDER)

    def next_opt2(self) -> int:
        self.display2()
        return read_int("Enter your choice : ")

    # ---------- helpers ----------
    @staticmethod
    def _find(students: list[Student], roll_no: int) -> int:
        """Index of the student with this roll number, or -1."""
        for i, s in enumerate(students):
            if s.roll_no == roll_no:
                return i
        return -1

    # ---------- operations ----------
    def add_student(self, students: list[Student]) -> None:
        name = input("Enter Name : ")
        print()
        age = read_int("Enter Age : ")
        print()
        mail = input("Enter Mail : ")
        print()
        ph = input("Enter Phone Number : ")
        print()
        csem = read_int("Enter Current Semester : ")
        print()
        gdr = input("Enter Gender : ")
        print()
        brh = input("Enter Branch : ")
        print()
        rno = max((s.roll_no for s in students), default=0)
        students.append(Student(rno + 1, name, age, gdr, brh, csem, mail, ph))
        print("New Student Added Successfullyyyy......")

    def view_students(self, students: list[Student]) -> None:
        print(f"Total Number of Students : {len(students)}")
        for s in students:
            s.view_student()

    def search_student(self, students: list[Student]) -> None:
        if not students:
            print("No Students at Present")
            return
        print("Enter the roll number of the student to be searched : ")
        rno = read_int("")
        while rno <= 0:
            rno = read_int("Enter valid roll number : ")
        idx = self._find(students, rno)
        if idx == -1:
            print(f"Student with roll number {rno} is not found!!!")
        else:
            students[idx].view_student()

    def delete_student(self, students: list[Student]) -> None:
        if not students:
            print("No Students to delete at Present")
            return
        rno = read_int("Enter the roll number of student to be deleted : ")
        idx = self._find(students, rno)
        if idx == -1:
            print("No student with this roll number is present...")
            return
        del students[idx]
        print("Student deleted successfully............")

    def update_student(self, students: list[Student]) -> None:
        if not students:
            print("No Students to update at Present")
            return
        self.view_students(students)
        rno = read_int("Enter the roll number of student to be updated : ")
        idx = self._find(students, rno)
        if idx == -1:
            print("Wrong roll number entered...")
            return
        student = students[idx]
        opt = self.next_opt2()
        while opt != 8:
            if opt in UPDATE_FIELDS:
                prompt, attr, convert = UPDATE_FIELDS[opt]
                value = read_int(prompt) if convert is int else input(prompt)
                setattr(student, attr, value)
            else:
                print("Enter a valid choice")
            opt = self.next_opt2()
        print("Changes are noted don't forget to select save progress after all the operations are done")

    def save_progress(self, students: list[Student]) -> None:
        try:
            with open(self.data_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f, lineterminator="\n")
                for s in students:
                    writer.writerow(
                        [s.roll_no, s.name, s.age, s.gender, s.branch, s.curr_sem, s.email, s.phno]
                    )
        except OSError:
            print("Error : File not found")
