from PyQt6.QtWidgets import QTableView

class TransactionTableView(QTableView):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setModel(self.controller.get_transaction_model())
        self.setup_ui()

    def setup_ui(self):
        self.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.horizontalHeader().setStretchLastSection(True)