from skill_bootcamp.service_layer.app_services import AppServices
from skill_bootcamp.application_base import ApplicationBase
from prettytable import PrettyTable
import sys
from skill_bootcamp.infrastructure_layer.cohort import Cohort
from skill_bootcamp.infrastructure_layer.module import Module
from skill_bootcamp.infrastructure_layer.student import Student

class ConsoleUI(ApplicationBase):
    """ Define the ConsoleUI class. """

    def __init__(self, config:dict)->None:
        """ Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
                logfile_prefix_name=self.META["log_prefix"])
        self.app_services = AppServices(config)

    # Public Methods
    def display_menu(self)->None:
        """ Display the menu. """
        print(f"\n\n\tSkill Bootcamp Management System")
        print()
        print(f"\t1. List all students")
        print(f"\t2. List all cohorts")
        print(f"\t3. List all modules")
        print(f"\t4. Add Student")
        print(f"\t5. Add Cohort")
        print(f"\t6. Add Module")
        print(f"\t7. Record Student Cohort")
        print(f"\t8. Record Student Module")
        print(f"\t9. Exit")
        print()

    def process_menu_choice(self)->None:
        """ Process users menu choice. """
        choice = input("\tEnter your choice (1-9): ")

        match choice:
            case '1': self.list_students()
            case '2': self.list_cohorts()
            case '3': self.list_modules()
            case '4': self.add_student()
            case '5': self.add_cohort()
            case '6': self.add_module()
            case '8': self.record_student_cohort()
            case '8': self.record_student_module()
            case '9': sys.exit(0)
            case _: print("\tInvalid Menu choice {choice}. Please try again.")

    def list_students(self)->None:
        """ Listing all students. """
        print("\tListing all students...")
        students = self.app_services.get_all_students()
        students_table = PrettyTable()
        students_table.field_names = ["ID", "First Name", "Last Name", "Email", "Cohort", "Modules"]
        modules_table = PrettyTable()
        modules_table.field_names = ["Name", "Status"]
        for student in students:
            for module in student.modules:
                modules_table.add_row([module.module_name, module.status])
            students_table.add_row([student.id, student.first_name, student.last_name, student.email, student.cohort.cohort_name, modules_table.get_string()])
            students_table.add_divider()
            modules_table.clear_rows()
        print(students_table)

    def list_cohorts(self)->None:
        """ Listing all cohorts. """
        print("\tListing all cohorts...")

    def list_modules(self)->None:
        """ Listing all modules. """
        print("\tListing all modules...")

    def add_student(self)->None:
        """ Add a new student. """
        print("\tAdding a new student...")

    def add_cohort(self)->None:
        """ Add a new cohort. """
        print("\tAdding a new cohort...")

    def add_module(self)->None:
        """ Add a new module. """
        print("\tAdding a new module...")

    def record_student_cohort(self)->None:
        """ Record a student cohort. """
        print("\tRecording a student cohort...")

    def record_student_module(self)->None:
        """ Record a student module. """
        print("\tRecording a student module...")

    def start(self)->None:
        while True:
            self.display_menu()
            self.process_menu_choice()