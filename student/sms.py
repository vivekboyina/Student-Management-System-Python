import csv
from pathlib import Path

from .execution import Execution
from .student import Student

# students.txt lives next to this file, so the app works from any folder
DATA_FILE = Path(__file__).with_name("students.txt")


class SMS:
    """Core application: loads data, then runs the menu loop."""

    def __init__(self, data_file: Path = DATA_FILE):
        self.data_file = Path(data_file)

    def load(self) -> list[Student]:
        students: list[Student] = []
        try:
            with open(self.data_file, newline="", encoding="utf-8") as f:
                for line_no, row in enumerate(csv.reader(f), start=1):
                    if not row:
                        continue
                    try:
                        students.append(
                            Student(
                                int(row[0]), row[1], int(row[2]), row[3],
                                row[4], int(row[5]), row[6], row[7],
                            )
                        )
                    except (ValueError, IndexError):
                        print(f"Skipping malformed line {line_no}")
            print("Data loaded Successfully")
        except FileNotFoundError:
            print("Error loading data")
        except OSError:
            print("IO Exception occured")
        return students

    def start(self) -> None:
        print()
        students = self.load()
        print()
        ex = Execution(self.data_file)
        actions = {
            1: ex.add_student,
            2: ex.view_students,
            3: ex.search_student,
            4: ex.delete_student,
            5: ex.update_student,
            6: ex.save_progress,
        }
        opt = ex.next_opt()
        while opt != 7:
            action = actions.get(opt)
            if action:
                action(students)
            else:
                print("Enter a valid option")
            opt = ex.next_opt()
        print("Thanks for your valuable time")
        print("Hope you enjoyed SMS!!!")
