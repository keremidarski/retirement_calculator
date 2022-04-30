from PyQt5.QtWidgets import QMainWindow, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
from retirement_calculator import RetirementCalculator

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("window.ui", self)

        self.app_label = self.findChild(QLabel, "app_label")
        self.current_age_label = self.findChild(QLabel, "current_age_label")
        self.yearly_contribution_label = self.findChild(
            QLabel, "yearly_contribution_label"
        )
        self.current_savings_label = self.findChild(QLabel, "current_savings_label")
        self.retirement_age_label = self.findChild(QLabel, "retirement_age_label")
        self.avg_annual_return_label = self.findChild(
            QLabel, "avg_annual_return_label"
        )
        self.result_label = self.findChild(QLabel, "result_label")
        self.result_number_label = self.findChild(QLabel, "result_number_label")
        self.current_age_text_edit = self.findChild(
            QTextEdit, "current_age_text_edit"
        )
        self.yearly_contribution_text_edit = self.findChild(
            QTextEdit, "yearly_contribution_text_edit"
        )
        self.current_savings_text_edit = self.findChild(
            QTextEdit, "current_savings_text_edit"
        )
        self.retirement_age_text_edit = self.findChild(
            QTextEdit, "retirement_age_text_edit"
        )
        self.avg_annual_return_text_edit = self.findChild(
            QTextEdit, "avg_annual_return_text_edit"
        )

        self.calculate_button = self.findChild(QPushButton, "calculate_button")
        self.calculate_button.clicked.connect(self.clicker)
        self.show()

    def clicker(self):
        self.result = RetirementCalculator(
            int(self.current_age_text_edit.toPlainText()),
            int(self.yearly_contribution_text_edit.toPlainText()),
            int(self.current_savings_text_edit.toPlainText()),
            int(self.retirement_age_text_edit.toPlainText()),
            int(self.avg_annual_return_text_edit.toPlainText()),
        )
        self.result_number_label.setText(f"{self.result}")
