from PyQt5.QtWidgets import QApplication
from ui import UI
import sys


def main():
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()


if __name__ == "__main__":
    main()
