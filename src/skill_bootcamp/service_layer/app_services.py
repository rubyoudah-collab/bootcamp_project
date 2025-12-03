"""Implements AppServices Class."""

from skill_bootcamp.application_base import ApplicationBase
from skill_bootcamp.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
import inspect
from skill_bootcamp.infrastructure_layer.student import Student
from skill_bootcamp.infrastructure_layer.cohort import Cohort
from skill_bootcamp.infrastructure_layer.module import Module

class AppServices(ApplicationBase):
    """AppServices Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = MySQLPersistenceWrapper(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

    def get_all_students(self):
        """ Return a list of student objects. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Retrieving all students from database.")
        student_dict = {}
        student_dict['students'] = []

        try:
            results = self.DB.select_all_students()
            return results
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")

    def get_all_cohorts(self):
        """ Return a list of cohort objects. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Retrieving all cohorts from database.")
        cohort_dict = {}
        cohort_dict['cohorts'] = []

        try:
            results = self.DB.select_all_cohorts()
            return results
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")

    def get_all_modules(self):
        """ Return a list of module objects. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Retrieving all modules from database.")
        module_dict = {}
        module_dict['modules'] = []

        try:
            results = self.DB.select_all_modules()
            return results
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")

    def insert_student(self, first_name:str, last_name:str, email:str, cohort_id:int)->Student:
        """ Insert a student object into the database. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Inserting student into database.")

        try:
            student = Student()
            student.first_name = first_name
            student.last_name = last_name
            student.email = email
            cohort = self.DB.select_a_cohort_by_id(cohort_id)
            if cohort is None:
                self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Cohort ID {cohort_id} does not exist.")
                return None
            student.cohort = cohort
            student = self.DB.insert_student(student)
            return student
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")

    def update_student(self, student_id:int, first_name:str, last_name:str, email:str, cohort_id:int)->Student:
        """ Update a student object in the database. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Updating student in database.")

        try:
            student = self.DB.select_a_student_by_id(student_id)
            if student is None:
                self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Student ID {student_id} does not exist.")
                return None
            student.first_name = first_name
            student.last_name = last_name
            student.email = email
            cohort = self.DB.select_a_cohort_by_id(cohort_id)
            if cohort is None:
                self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Cohort ID {cohort_id} does not exist.")
                return None
            student.cohort = cohort
            student = self.DB.update_student(student)
            return student
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")

    def delete_student(self, student_id:int)->bool:
        """ Delete a student object from the database. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Deleting student with id {student_id} from database.")

        try:
            student = self.DB.select_a_student_by_id(student_id)
            if student is None:
                self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Student ID {student_id} does not exist.")
                return False
            result = self.DB.delete_student(student_id)
            return result
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")

    def insert_cohort(self, cohort_name:str, start_date:str, end_date:str)->Cohort:
        """ Insert a cohort object into the database. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Inserting cohort into database.")

        try:
            cohort = Cohort()
            cohort.cohort_name = cohort_name
            cohort.start_date = start_date
            cohort.end_date = end_date
            cohort = self.DB.insert_cohort(cohort)
            return cohort
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")

    def insert_module(self, module_name:str, description:str)->Module:
        """ Insert a module object into the database. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Inserting module into database.")

        try:
            module = Module()
            module.module_name = module_name
            module.description = description
            module = self.DB.insert_module(module)
            return module
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")

    def record_student_module_completion(self, student_id:int, module_id:int, status:str)->bool:
        """ Record the completion status of a module for a student. """

        self._logger.log_debug(f"{inspect.currentframe().f_code.co_name}: Recording module completion for student ID {student_id} and module ID {module_id}.")

        try:
            student = self.DB.select_a_student_by_id(student_id)
            if student is None:
                self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Student ID {student_id} does not exist.")
                return False
            module = self.DB.select_a_module_by_id(module_id)
            if module is None:
                self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Module ID {module_id} does not exist.")
                return False
            result = self.DB.record_student_module_completion(student, module, status)
            return result
        except Exception as ex:
            self._logger.log_error(f"{inspect.currentframe().f_code.co_name}: Exception occurred: {ex}")
            return False