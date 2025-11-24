"""Defines the MySQLPersistenceWrapper class."""

from skill_bootcamp.application_base import ApplicationBase
from mysql import connector
from mysql.connector.pooling import (MySQLConnectionPool)
import inspect
import json
from typing import List
from skill_bootcamp.infrastructure_layer.student import Student
from skill_bootcamp.infrastructure_layer.cohort import Cohort
from skill_bootcamp.infrastructure_layer.module import Module
from enum import Enum

class MySQLPersistenceWrapper(ApplicationBase):
	"""Implements the MySQLPersistenceWrapper class."""

	def __init__(self, config:dict)->None:
		"""Initializes object. """
		self._config_dict = config
		self.META = config["meta"]
		self.DATABASE = config["database"]
		super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = \
			self.DATABASE["connection"]["config"]["database"]
		self.DB_CONFIG['user'] = self.DATABASE["connection"]["config"]["user"]
		self.DB_CONFIG['password'] = self.DATABASE["connection"]["config"]["password"]
		self.DB_CONFIG['host'] = self.DATABASE["connection"]["config"]["host"]
		self.DB_CONFIG['port'] = self.DATABASE["connection"]["config"]["port"]

		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: DB Connection Config Dict: {self.DB_CONFIG}')

		# Database Connection
		self._connection_pool = \
			self._initialize_database_connection_pool(self.DB_CONFIG)
		
		# Module Column ENUMS
		self.ModuleColumns = \
			Enum('ModuleColumns', [('id', 0), ('module_name', 1), ('description', 2), ('status', 3)])
		
		# Cohort Column ENUMS
		self.CohortColumns = \
			Enum('CohortColumns', [('id', 0), ('cohort_name', 1), ('start_date', 2), ('end_date', 3)])
		
		# Student Column ENUMS
		self.StudentColumns = \
			Enum('StudentColumns', [('id', 0), ('first_name', 1), ('last_name', 2), ('email', 3),
				('cohort_name', 4), ('start_date', 5), ('end_date', 6)])


		# SQL String Constants
		self.SELECT_ALL_STUDENTS = \
			"SELECT id, first_name, last_name, email " \
			"FROM students;" \
		
		self.SELECT_ALL_COHORTS = \
			"SELECT id, cohort_name, start_date, end_date " \
			"FROM cohorts;"
		
		self.SELECT_ALL_MODULES = \
			"SELECT id, module_name, description " \
			"FROM modules;"
		
		self.SELECT_STUDENTS_WITH_COHORTS = \
			"SELECT students.id, first_name, last_name, email, cohort_name, start_date, end_date " \
			"FROM students, cohorts " \
			"WHERE students.cohort_id = cohorts.id;"
		
		self.SELECT_MODULES_FOR_STUDENT_ID = \
			"SELECT modules.id, modules.module_name, modules.description, student_module_xref.status " \
			"FROM modules, student_module_xref " \
			"WHERE student_module_xref.module_id = modules.id AND student_module_xref.student_id = %s;"





	# MySQLPersistenceWrapper Methods
	def select_all_students(self)->List[Student]:
		"""Selects all students from the database."""
		cursor = None
		results = None
		students_list = []
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_STUDENTS_WITH_COHORTS)
					results = cursor.fetchall()
				students_list = self._pupulate_student_objects(results)
			for student in students_list:
				modules_list = self.select_all_modules_for_student_id(student.id) or []
				student.modules = self._populate_module_objects(modules_list)
				self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Retrieved student')

			return students_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem selecting all students: {e}')
			return []
	
	def select_all_cohorts(self)->List[Cohort]:
		"""Selects all cohorts from the database."""
		cursor = None
		results = None
		cohorts_list = []
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_COHORTS)
					results = cursor.fetchall()
				cohorts_list = self._populate_cohort_objects(results)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Retrieved all cohorts')
			return cohorts_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem selecting all cohorts: {e}')

	def select_all_modules(self)->List[Module]:
		"""Selects all modules from the database."""
		cursor = None
		results = None
		modules_list = []
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_MODULES)
					results = cursor.fetchall()
				modules_list = self._populate_module_objects(results)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Retrieved all modules')
			return modules_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem selecting all modules: {e}')
			return []

	def select_all_modules_for_student_id(self, student_id:int)->List[Module]:
		"""Selects all modules for a given student ID from the database."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_MODULES_FOR_STUDENT_ID, (student_id,))
					results = cursor.fetchall()
			return results
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem selecting all modules for student ID {student_id}: {e}')
			return []





		##### Private Utility Methods #####

	def _initialize_database_connection_pool(self, config:dict)->MySQLConnectionPool:
		"""Initializes database connection pool."""
		try:
			self._logger.log_debug(f'Creating connection pool...')
			cnx_pool = \
				MySQLConnectionPool(pool_name = self.DATABASE["pool"]["name"],
					pool_size=self.DATABASE["pool"]["size"],
					pool_reset_session=self.DATABASE["pool"]["reset_session"],
					use_pure=self.DATABASE["pool"]["use_pure"],
					**config)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Connection pool successfully created!')
			return cnx_pool
		except connector.Error as err:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem creating connection pool: {err}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Check DB cnfg:\n{json.dumps(self.DATABASE)}')
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Problem creating connection pool: {e}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Check DB conf:\n{json.dumps(self.DATABASE)}')


	def _pupulate_student_objects(self, results:List)->List[Student]:
		"""Populates and returns a list of student objects."""
		students_list = []
		try:
			for row in results:
				student = Student()
				student.id = row[self.StudentColumns['id'].value]
				student.first_name = row[self.StudentColumns['first_name'].value]
				student.last_name = row[self.StudentColumns['last_name'].value]
				student.email = row[self.StudentColumns['email'].value]
				if row[self.StudentColumns['cohort_name'].value] is not None:
					cohort = Cohort()
					cohort.id = None
					cohort.cohort_name = row[self.StudentColumns['cohort_name'].value]
					cohort.start_date = row[self.StudentColumns['start_date'].value]
					cohort.end_date = row[self.StudentColumns['end_date'].value]
					student.cohort = cohort
				students_list.append(student)
			return students_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem populating student objects: {e}')
			return []

	def _populate_cohort_objects(self, results:List)->List[Cohort]:
		"""Populates and returns a list of cohort objects."""
		cohorts_list = []
		try:
			if results is None:
				return []
			for row in results:
				cohort = Cohort()
				cohort.id = row[self.CohortColumns['id'].value]
				cohort.cohort_name = row[self.CohortColumns['cohort_name'].value]
				cohort.start_date = row[self.CohortColumns['start_date'].value]
				cohort.end_date = row[self.CohortColumns['end_date'].value]
				cohorts_list.append(cohort)
			return cohorts_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem populating cohort objects: {e}')
			return []
		
	def _populate_module_objects(self, results:List)->List[Module]:
		"""Populates and returns a list of module objects."""
		modules_list = []
		try:
			if results is None:
				return []
			for row in results:
				module = Module()
				module.id = row[self.ModuleColumns['id'].value]
				module.module_name = row[self.ModuleColumns['module_name'].value]
				module.description = row[self.ModuleColumns['description'].value]
				if len(row) > 3:
					module.status = row[self.ModuleColumns['status'].value]
				modules_list.append(module)
			return modules_list
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem populating module objects: {e}')
			return []
