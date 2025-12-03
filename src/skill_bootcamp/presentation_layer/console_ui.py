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
        print(f"\t5. Update Student")
        print(f"\t6. Delete Student")
        print(f"\t7. Add Cohort")
        print(f"\t8. Add Module")
        print(f"\t9. Record Student Module")
        print(f"\t10. Exit")
        print()

    def process_menu_choice(self)->None:
        """ Process users menu choice. """
        choice = input("\tEnter your choice (1-10): ")

        match choice:
            case '1': self.list_students()
            case '2': self.list_cohorts()
            case '3': self.list_modules()
            case '4': self.add_student()
            case '5': self.update_student()
            case '6': self.delete_student()
            case '7': self.add_cohort()
            case '8': self.add_module()
            case '9': self.record_student_module()
            case '10': sys.exit(0)
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
        cohorts = self.app_services.get_all_cohorts()
        cohorts_table = PrettyTable()
        cohorts_table.field_names = ["ID", "Cohort Name", "Start Date", "End Date"]
        for cohort in cohorts:
            cohorts_table.add_row([cohort.id, cohort.cohort_name, cohort.start_date, cohort.end_date])
        print(cohorts_table)

    def list_modules(self)->None:
        """ Listing all modules. """
        print("\tListing all modules...")
        modules = self.app_services.get_all_modules()
        modules_table = PrettyTable()
        modules_table.field_names = ["ID", "Module Name", "Description"]
        for module in modules:
            modules_table.add_row([module.id, module.module_name, module.description])
        print(modules_table)

    def add_student(self)->None:
        """ Add a new student. """
        print("\tAdding a new student...")
        try:
            first_name = input("\tEnter First Name: ")
            last_name = input("\tEnter Last Name: ")
            email = input("\tEnter Email: ")
            cohort_id = int(input("\tEnter Cohort ID: "))
            student = self.app_services.insert_student(first_name, last_name, email, cohort_id)
            if student is not None:
                print(f"\tStudent added with Name: {first_name} {last_name}")
            else:
                self._logger.log_error(f"Failed to add student {first_name} {last_name}.")
        except Exception as ex:
            self._logger.log_error(f"Exception occurred: {ex}")

    def update_student(self)->None:
        """ Update an existing student. """
        print("\tUpdating an existing student...")
        try:
            student_id = int(input("\tEnter Student ID to update: "))
            first_name = input("\tEnter New First Name: ")
            last_name = input("\tEnter New Last Name: ")
            email = input("\tEnter New Email: ")
            cohort_id = int(input("\tEnter New Cohort ID: "))
            student = self.app_services.update_student(student_id, first_name, last_name, email, cohort_id)
            if student is not None:
                print(f"\tStudent updated with ID: {student_id}")
            else:
                self._logger.log_error(f"Failed to update student with ID {student_id}.")
        except Exception as ex:
            self._logger.log_error(f"Exception occurred: {ex}")

    def delete_student(self)->None:
        """ Delete a student. """
        print("\tDeleting a student...")
        try:
            student_id = int(input("\tEnter Student ID to delete: "))
            success = self.app_services.delete_student(student_id)
            if success:
                print(f"\tStudent deleted with ID: {student_id}")
            else:
                self._logger.log_error(f"Failed to delete student with ID {student_id}.")
        except Exception as ex:
            self._logger.log_error(f"Exception occurred: {ex}")

    def add_cohort(self)->None:
        """ Add a new cohort. """
        print("\tAdding a new cohort...")
        try:
            cohort_name = input("\tEnter Cohort Name: ")
            start_date = input("\tEnter Start Date (YYYY-MM-DD): ")
            end_date = input("\tEnter End Date (YYYY-MM-DD): ")
            cohort = self.app_services.insert_cohort(cohort_name, start_date, end_date)
            if cohort is not None:
                print(f"\tCohort added with Name: {cohort_name}")
            else:
                self._logger.log_error(f"Failed to add cohort {cohort_name}.")
        except Exception as ex:
            self._logger.log_error(f"Exception occurred: {ex}")

    def add_module(self)->None:
        """ Add a new module. """
        print("\tAdding a new module...")
        try:
            module_name = input("\tEnter Module Name: ")
            description = input("\tEnter Module Description: ")
            module = self.app_services.insert_module(module_name, description)
            if module is not None:
                print(f"\tModule added with Name: {module_name}.")
            else:
                self._logger.log_error(f"Failed to add module {module_name}.")
        except Exception as ex:
            self._logger.log_error(f"Exception occurred: {ex}")

    def record_student_module(self)->None:
        """ Record a student module. """
        print("\tRecording a student module...")
        try:
            student_id = int(input("\tEnter Student ID: "))
            module_id = int(input("\tEnter Module ID: "))
            status = input("\tEnter Status (e.g., Completed, In Progress, Pending): ")
            success = self.app_services.record_student_module_completion(student_id, module_id, status)
            if success:
                print(f"\tRecorded module for student with status '{status}'.")
            else:
                self._logger.log_error(f"Failed to record module for student.")
        except Exception as ex:
            self._logger.log_error(f"Exception occurred: {ex}")

    def start(self)->None:
        while True:
            self.display_menu()
            self.process_menu_choice()