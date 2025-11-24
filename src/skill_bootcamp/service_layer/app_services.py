"""Implements AppServices Class."""

from skill_bootcamp.application_base import ApplicationBase
from skill_bootcamp.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
import inspect

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