# src/user_interface/menu_bar.py

from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction
import configs.ui_constants as ui_const

class MenuBar(QMenuBar):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.setup_menus()

    def setup_menus(self):
        self.setup_file_menu()
        self.setup_database_menu()
        # Add more menus as needed

    def setup_file_menu(self):
        file_menu = QMenu(ui_const.MENU_FILE, self)
        self.addMenu(file_menu)

        exit_action = QAction(ui_const.MENU_ITEM_EXIT, self)
        exit_action.triggered.connect(self.parent().close)
        file_menu.addAction(exit_action)

    def setup_database_menu(self):
        database_menu = QMenu(ui_const.MENU_DATABASE, self)
        self.addMenu(database_menu)

        reset_action = QAction(ui_const.MENU_ITEM_RESET_DB, self)
        reset_action.triggered.connect(self.controller.reset_database)
        database_menu.addAction(reset_action)

        populate_action = QAction(ui_const.MENU_ITEM_POPULATE_DEFAULT, self)
        populate_action.triggered.connect(self.controller.populate_default_data)
        database_menu.addAction(populate_action)