"""Persistence Layer Unit Tests."""
from tests.context import MySQLPersistenceWrapper
from tests.context import Student
from tests.context import Module
from tests.context import Cohort
import pytest
import json
import os

@pytest.fixture(scope="class")
def mysql_persistence_wrapper():
    print(f'\nSetting up mysql_persistence_wrapper_fixture...')
    working_dir = os.getcwd()
    config_dir = 'config'
    config_file_name = 'skill_bootcamp_app_config.json'
    config_dir_path = os.path.join(working_dir, config_dir, config_file_name )
    config_dict = None
    with open(config_dir_path, 'r') as f:
        config_dict = json.loads(f.read())
    db = MySQLPersistenceWrapper(config_dict)
    yield db
    print(f'\nTearing down mysql_persistence_wrapper_fixture...')

class TestPersistenceLayer:
    """Persistence Layer Unit Tests."""

    # Happy Path Tests

    def test_select_all_students(self, mysql_persistence_wrapper):
        """Test: select_all_students"""
        students = mysql_persistence_wrapper.select_all_students()
        assert len(students) > 0

    def test_select_all_cohorts(self, mysql_persistence_wrapper):
        """Test: select_all_cohorts"""
        cohorts = mysql_persistence_wrapper.select_all_cohorts()
        assert len(cohorts) > 0

    def test_select_all_modules(self, mysql_persistence_wrapper):
        """Test: select_all_modules"""
        modules = mysql_persistence_wrapper.select_all_modules()
        assert len(modules) > 0

    def test_select_student_by_id(self, mysql_persistence_wrapper):
        """Test: select_student_by_id"""
        student = mysql_persistence_wrapper.select_a_student_by_id(1)
        assert student is not None

    def test_insert_student(self, mysql_persistence_wrapper):
        """Test: insert_student"""
        student = Student()
        student.first_name = 'Test'
        student.last_name = 'Student'
        student.email = 'test-student@example.com'
        cohort = mysql_persistence_wrapper.select_all_cohorts()[0]
        student.cohort = cohort
        inserted_student = mysql_persistence_wrapper.insert_student(student)
        assert inserted_student is not None

    def test_insert_cohort(self, mysql_persistence_wrapper):
        """Test: insert_cohort"""
        cohort = Cohort()
        cohort.cohort_name = 'Test Cohort'
        inserted_cohort = mysql_persistence_wrapper.insert_cohort(cohort)
        assert inserted_cohort is not None

    def test_insert_module(self, mysql_persistence_wrapper):
        """Test: insert_module"""
        module = Module()
        module.module_name = 'Test Module'
        module.description = 'This is a test module.'
        inserted_module = mysql_persistence_wrapper.insert_module(module)
        assert inserted_module is not None

    def test_update_student(self, mysql_persistence_wrapper):
        """Test: update_student"""
        student = mysql_persistence_wrapper.select_a_student_by_id(1)
        student.first_name = 'Updated'
        student.last_name = 'student Name'
        student.cohort = mysql_persistence_wrapper.select_all_cohorts()[0]
        
        mysql_persistence_wrapper.update_student(student)
        updated_student = mysql_persistence_wrapper.select_a_student_by_id(1)
        assert updated_student.first_name == 'Updated'

    def test_delete_student(self, mysql_persistence_wrapper):
        """Test: delete_student"""
        student = Student()
        student.first_name = 'Delete'
        student.last_name = 'Me'
        student.email = 'delete-me@example.com'
        cohort = mysql_persistence_wrapper.select_all_cohorts()[0]
        student.cohort = cohort
        inserted_student = mysql_persistence_wrapper.insert_student(student)
        mysql_persistence_wrapper.delete_student(inserted_student.id)
        deleted_student = mysql_persistence_wrapper.select_a_student_by_id(inserted_student.id)
        assert deleted_student is None

    # Edge Case Tests
    def test_select_student_by_invalid_id(self, mysql_persistence_wrapper):
        """Test: select_student_by_invalid_id"""
        student = mysql_persistence_wrapper.select_a_student_by_id(0)
        assert student is None

    def test_delete_nonexistent_student(self, mysql_persistence_wrapper):
        """Test: delete_nonexistent_student"""
        mysql_persistence_wrapper.delete_student(99999)
        assert True  # No exception means pass