# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(641, 744)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 321, 31))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 471, 31))
        self.lineEdit.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 320, 351, 41))
        self.pushButton.setFont(font)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 670, 601, 23))
        self.progressBar.setValue(0)
        self.label_book_value = QLabel(self.centralwidget)
        self.label_book_value.setObjectName(u"label_book_value")
        self.label_book_value.setGeometry(QRect(100, 110, 281, 16))
        self.label_book_value.setFont(font)
        self.label_author = QLabel(self.centralwidget)
        self.label_author.setObjectName(u"label_author")
        self.label_author.setGeometry(QRect(20, 140, 51, 20))
        self.label_author.setFont(font)
        self.label_author_value = QLabel(self.centralwidget)
        self.label_author_value.setObjectName(u"label_author_value")
        self.label_author_value.setGeometry(QRect(100, 140, 281, 20))
        self.label_author_value.setFont(font)
        self.label_reads = QLabel(self.centralwidget)
        self.label_reads.setObjectName(u"label_reads")
        self.label_reads.setGeometry(QRect(20, 170, 61, 21))
        self.label_reads.setFont(font)
        self.label_reads_value = QLabel(self.centralwidget)
        self.label_reads_value.setObjectName(u"label_reads_value")
        self.label_reads_value.setGeometry(QRect(100, 170, 281, 21))
        self.label_reads_value.setFont(font)
        self.label_Book = QLabel(self.centralwidget)
        self.label_Book.setObjectName(u"label_Book")
        self.label_Book.setGeometry(QRect(20, 110, 61, 16))
        self.label_Book.setFont(font)
        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(20, 230, 121, 20))
        self.label_time.setFont(font)
        self.label_time_value = QLabel(self.centralwidget)
        self.label_time_value.setObjectName(u"label_time_value")
        self.label_time_value.setGeometry(QRect(160, 230, 221, 21))
        self.label_time_value.setFont(font)
        self.lineEdit_way = QLineEdit(self.centralwidget)
        self.lineEdit_way.setObjectName(u"lineEdit_way")
        self.lineEdit_way.setGeometry(QRect(20, 270, 281, 31))
        self.lineEdit_way.setFont(font)
        self.toolButton_way = QToolButton(self.centralwidget)
        self.toolButton_way.setObjectName(u"toolButton_way")
        self.toolButton_way.setGeometry(QRect(310, 270, 61, 31))
        self.toolButton_way.setFont(font)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(390, 120, 231, 241))
        font1 = QFont()
        font1.setPointSize(10)
        self.textBrowser.setFont(font1)
        self.pushButton_info = QPushButton(self.centralwidget)
        self.pushButton_info.setObjectName(u"pushButton_info")
        self.pushButton_info.setGeometry(QRect(500, 50, 121, 31))
        self.pushButton_info.setFont(font)
        self.label_reads_2 = QLabel(self.centralwidget)
        self.label_reads_2.setObjectName(u"label_reads_2")
        self.label_reads_2.setGeometry(QRect(20, 200, 151, 21))
        self.label_reads_2.setFont(font)
        self.label_tracks = QLabel(self.centralwidget)
        self.label_tracks.setObjectName(u"label_tracks")
        self.label_tracks.setGeometry(QRect(180, 200, 201, 21))
        self.label_tracks.setFont(font)
        self.textBrowser_progress = QTextBrowser(self.centralwidget)
        self.textBrowser_progress.setObjectName(u"textBrowser_progress")
        self.textBrowser_progress.setGeometry(QRect(20, 390, 601, 251))
        self.textBrowser_progress.setFont(font1)
        self.label_Book_2 = QLabel(self.centralwidget)
        self.label_Book_2.setObjectName(u"label_Book_2")
        self.label_Book_2.setGeometry(QRect(470, 90, 91, 21))
        self.label_Book_2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 641, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0442\u0435 \u0441\u0441\u044b\u043b\u043a\u0443 \u0441 \u0441\u0430\u0439\u0442\u0430 www.knigavuhe.org", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label_book_value.setText("")
        self.label_author.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440:", None))
        self.label_author_value.setText("")
        self.label_reads.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0442\u0430\u0435\u0442:", None))
        self.label_reads_value.setText("")
        self.label_Book.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043d\u0438\u0433\u0430:", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0432\u0443\u0447\u0430\u043d\u0438\u044f:", None))
        self.label_time_value.setText("")
        self.lineEdit_way.setText("")
        self.toolButton_way.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.pushButton_info.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.label_reads_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0440\u0435\u043a\u043e\u0432:", None))
        self.label_tracks.setText("")
        self.textBrowser_progress.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.label_Book_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
    # retranslateUi

