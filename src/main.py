# src/main.py

import sys
from PyQt6.QtWidgets import QApplication
from controllers.main_window_controller import MainWindowController
from user_interface.main_window import MainWindow
from utils.custom_logging import setup_logging, logger

def main():
    setup_logging()  # Initialize logging
    logger.info("Starting Simple Income/Expense Tracker")
    
    app = QApplication(sys.argv)
    controller = MainWindowController()
    window = MainWindow(controller)
    window.show()
    
    logger.info("Application UI loaded and displayed")
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()