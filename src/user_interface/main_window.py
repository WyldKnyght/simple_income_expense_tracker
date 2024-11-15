# src\User_interface\main_window.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QStatusBar, QHBoxLayout
from utils.custom_logging import error_handler
from configs.config_manager import ConfigurationManager
from .menu_bar import MenuBar

class MainWindow(QMainWindow):
    @error_handler
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.config_manager = ConfigurationManager()  # Initialize ConfigurationManager
        
        # Access UI constants through ConfigurationManager
        self.setWindowTitle(self.config_manager.get_ui_constants()["WINDOW_TITLE"])
        self.setGeometry(*self.config_manager.get_ui_constants()["WINDOW_GEOMETRY"])
        
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

        main_layout = QVBoxLayout()  # Main vertical layout
        central_widget.setLayout(main_layout)

        # Top section with summary widgets
        top_layout = QHBoxLayout()  # Horizontal layout for summary widgets
        main_layout.addLayout(top_layout)

        # Add summary widgets (e.g., total income, total expenses, balance)
        top_layout.addWidget(self.create_summary_widget("Total Income"))
        top_layout.addWidget(self.create_summary_widget("Total Expenses"))
        top_layout.addWidget(self.create_summary_widget("Balance"))

        # Tab widget for different sections
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        # Setup tabs for different functionalities
        self.add_placeholder_tab("Dashboard")
        self.add_placeholder_tab("Incomes")
        self.add_placeholder_tab("Expenses")
        self.add_placeholder_tab("Transactions")
        self.add_placeholder_tab("Reports")

    @error_handler
    def create_summary_widget(self, title):
        """Create a summary widget with a title and placeholder value."""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        # Title label
        title_label = QLabel(title)
        
        # Placeholder value (you can later replace this with actual data)
        value_label = QLabel("$0.00")  
        
        layout.addWidget(title_label)
        layout.addWidget(value_label)
        
        return widget

    @error_handler
    def add_placeholder_tab(self, name):
        """Add a placeholder tab to the tab widget."""
        tab = QWidget()
        tab_layout = QVBoxLayout()
        
        label = QLabel(self.config_manager.get_ui_constants()["PLACEHOLDER_TEXT"].format(name))  # Access placeholder text through config manager
        
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
        
        status_bar.showMessage(self.config_manager.get_ui_constants()["STATUS_READY"])  # Access status message through config manager