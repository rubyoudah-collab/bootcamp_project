"""Persistence Layer Unit Tests."""

from tests.context import MySQLPersistenceWrapper
import pytest
import json
import os


@pytest.fixture(scope="class")
def mysql_persistence_wrapper():
    """Create one MySQLPersistenceWrapper instance for all tests in this class."""
    # نرجع لمجلد المشروع الرئيسي
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # مسار ملف الإعدادات
    config_file = os.path.join(project_root, "config", "skill_bootcamp_app_config.json")

    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)

    db = MySQLPersistenceWrapper(config)
    yield db   # نرجع الكائن للاختبارات


class TestPersistenceLayer:
    """Defines a group of related unit tests."""

    def test_select_all_employees(self, mysql_persistence_wrapper):
        """Ensure select_all_employees runs without crashing."""
        employees = mysql_persistence_wrapper.select_all_employees()
        assert employees is not None