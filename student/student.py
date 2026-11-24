from dataclasses import dataclass

DIVIDER = "-" * 74


@dataclass
class Student:
    """A single student record."""

    roll_no: int = -1
    name: str = "NA"
    age: int = -1
    gender: str = "NA"
    branch: str = "NA"
    curr_sem: int = -1
    email: str = "NA@java.com"
    phno: str = "1234567890"

    def view_student(self) -> None:
        print(DIVIDER)
        print(f"Roll Number : {self.roll_no}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Branch : {self.branch}")
        print(f"Current Semester : {self.curr_sem}")
        print(f"Email : {self.email}")
        print(f"Phone Number : {self.phno}")
        print(DIVIDER)
