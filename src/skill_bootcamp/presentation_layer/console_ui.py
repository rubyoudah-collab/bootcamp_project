from skill_bootcamp.service_layer.app_services import AppServices
from skill_bootcamp.application_base import ApplicationBase


class ConsoleUI(ApplicationBase):
    def __init__(self, config: dict)-> None:
        self._config_dic = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, logfile_prefix_name=self.META["log_prefix"])
        self.app_services = AppServices(config)

    def display_menu(self):
        """Display the main menu to the user."""
        print("Welcome to the Skill Bootcamp Application!")
        print("\t1. List Students")
        print("\t2. List Cohorts")
        print("\t3. List Modules")
        print("\t4. Add Student")
        print("\t5. Add Cohort")
        print("\t6. Add Modules")
        print("\t7. Record Student Module")
        print("\t8. Exit")

    def run(self):
        self.display_menu()