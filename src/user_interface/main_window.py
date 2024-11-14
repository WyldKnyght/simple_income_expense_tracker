# src/user_interface/main_window.py

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QStatusBar
from utils.custom_logging import error_handler
import configs.ui_constants as ui_const
from .menu_bar import MenuBar

class MainWindow(QMainWindow):
    @error_handler
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle(ui_const.WINDOW_TITLE)
        self.setGeometry(*ui_const.WINDOW_GEOMETRY)
        self.setup_ui()

    @error_handler
    def setup_ui(self):
        self.setup_central_widget()
        self.setup_menu_bar()
        self.setup_status_bar()

    @error_handler
    def setup_central_widget(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)

        self.add_placeholder_tab(ui_const.TAB_DASHBOARD)
        self.add_placeholder_tab(ui_const.TAB_INCOMES)
        self.add_placeholder_tab(ui_const.TAB_EXPENSES)
        self.add_placeholder_tab(ui_const.TAB_TRANSACTIONS)
        self.add_placeholder_tab(ui_const.TAB_REPORTS)

    @error_handler
    def add_placeholder_tab(self, name):
        tab = QWidget()
        tab_layout = QVBoxLayout()
        label = QLabel(ui_const.PLACEHOLDER_TEXT.format(name))
        tab_layout.addWidget(label)
        tab.setLayout(tab_layout)
        self.tab_widget.addTab(tab, name)

    @error_handler
    def setup_menu_bar(self):
        menu_bar = MenuBar(self, self.controller)
        self.setMenuBar(menu_bar)

    @error_handler
    def setup_status_bar(self):
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage(ui_const.STATUS_READY)