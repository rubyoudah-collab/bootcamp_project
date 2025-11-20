import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from skill_bootcamp.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
from skill_bootcamp.application_base import ApplicationBase
from skill_bootcamp.presentation_layer.console_ui import ConsoleUI