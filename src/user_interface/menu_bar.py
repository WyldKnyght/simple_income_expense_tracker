# src/user_interface/menu_bar.py
from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction
from configs.config_manager import ConfigurationManager

class MenuBar(QMenuBar):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config_manager = ConfigurationManager()  # Initialize ConfigurationManager
        self.setup_menus()

    def setup_menus(self):
        self.setup_file_menu()
        self.setup_database_menu()
        # Add more menus as needed

    def setup_file_menu(self):
        file_menu = QMenu(self.config_manager.get_ui_constants()["MENU_FILE"], self)  # Access menu name through config manager
        self.addMenu(file_menu)

        exit_action = QAction(self.config_manager.get_ui_constants()["MENU_ITEM_EXIT"], self)  # Access exit action name through config manager
        exit_action.triggered.connect(self.parent().close)
        file_menu.addAction(exit_action)

    def setup_database_menu(self):
        database_menu = QMenu(self.config_manager.get_ui_constants()["MENU_DATABASE"], self)  # Access menu name through config manager
        self.addMenu(database_menu)

        reset_action = QAction(self.config_manager.get_ui_constants()["MENU_ITEM_RESET_DB"], self)  # Access reset action name through config manager
        reset_action.triggered.connect(self.controller.reset_database)
        database_menu.addAction(reset_action)

        populate_action = QAction(self.config_manager.get_ui_constants()["MENU_ITEM_POPULATE_DEFAULT"], self)  # Access populate action name through config manager
        populate_action.triggered.connect(self.controller.populate_default_data)
        database_menu.addAction(populate_action)