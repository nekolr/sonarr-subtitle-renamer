from PySide6.QtCore import (QCoreApplication, QRect, QMetaObject)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QFormLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox,
                               QToolButton, QWidget, QListWidget, QFileDialog, QMessageBox)

import renamer


class MainDialogUi(object):

    def __init__(self):
        # 选中的番剧 ID
        self.selectedSeriesId = None

        self.selectArchiveFileButton = None
        self.selectArchiveFileInput = None
        self.selectArchiveFileLabel = None
        self.selectArchiveFileLayout = None
        self.selectArchiveFileWidget = None

        self.executeButton = None

        self.selectSeasonLabel = None
        self.selectSeasonSpin = None
        self.selectSeasonLayout = None
        self.selectSeasonWidget = None

        self.outputDriveInput = None
        self.outputDriveLabel = None
        self.outputDriveLayout = None
        self.outputDriveWidget = None

        self.selectSeriesList = None
        self.selectSeriesLabel = None
        self.selectSeriesLayout = None
        self.selectSeriesWidget = None

        self.searchSeriesWidget = None
        self.searchSeriesButton = None
        self.searchSeriesInput = None
        self.searchSeriesLabel = None
        self.searchSeriesLayout = None

    def setup_ui(self, main_window):
        if main_window.objectName():
            main_window.setObjectName(u"main_window")
        # 禁止调整窗口大小
        main_window.setFixedSize(640, 480)
        main_window.setWindowIcon(QIcon('resource/tools.png'))

        self.setup_search_series_widget(main_window)
        self.setup_select_series_widget(main_window)
        self.setup_output_drive_widget(main_window)
        self.setup_select_archive_file_widget(main_window)
        self.setup_select_season_widget(main_window)
        self.setup_execute_button(main_window)

        self.re_translate_ui(main_window)

        QMetaObject.connectSlotsByName(main_window)

    def setup_search_series_widget(self, main_window):
        self.searchSeriesWidget = QWidget(main_window)
        self.searchSeriesWidget.setObjectName(u"searchSeriesWidget")
        self.searchSeriesWidget.setGeometry(QRect(50, 20, 540, 50))

        self.searchSeriesLayout = QHBoxLayout(self.searchSeriesWidget)
        self.searchSeriesLayout.setObjectName(u"searchSeriesLayout")
        self.searchSeriesLayout.setContentsMargins(0, 0, 0, 0)

        self.searchSeriesLabel = QLabel(self.searchSeriesWidget)
        self.searchSeriesLabel.setObjectName(u"searchSeriesLabel")
        self.searchSeriesLayout.addWidget(self.searchSeriesLabel)

        self.searchSeriesInput = QLineEdit(self.searchSeriesWidget)
        self.searchSeriesInput.setObjectName(u"searchSeriesInput")
        self.searchSeriesInput.setClearButtonEnabled(True)
        self.searchSeriesLayout.addWidget(self.searchSeriesInput)

        self.searchSeriesButton = QPushButton(self.searchSeriesWidget)
        self.searchSeriesButton.setObjectName(u"searchSeriesButton")
        self.searchSeriesButton.clicked.connect(self.handle_search_series)
        self.searchSeriesLayout.addWidget(self.searchSeriesButton)

    def setup_select_series_widget(self, main_window):
        self.selectSeriesWidget = QWidget(main_window)
        self.selectSeriesWidget.setObjectName(u"selectSeriesWidget")
        self.selectSeriesWidget.setGeometry(QRect(50, 90, 540, 120))

        self.selectSeriesLayout = QFormLayout(self.selectSeriesWidget)
        self.selectSeriesLayout.setObjectName(u"selectSeriesLayout")
        self.selectSeriesLayout.setContentsMargins(0, 0, 0, 0)

        self.selectSeriesLabel = QLabel(self.selectSeriesWidget)
        self.selectSeriesLabel.setObjectName(u"selectSeriesLabel")
        self.selectSeriesLayout.setWidget(0, QFormLayout.LabelRole, self.selectSeriesLabel)

        self.selectSeriesList = QListWidget(self.selectSeriesWidget)
        self.selectSeriesList.setObjectName(u"selectSeriesList")
        self.selectSeriesList.itemClicked.connect(self.handle_click_series)
        self.selectSeriesLayout.setWidget(0, QFormLayout.FieldRole, self.selectSeriesList)

    def setup_output_drive_widget(self, main_window):
        self.outputDriveWidget = QWidget(main_window)
        self.outputDriveWidget.setObjectName(u"outputDriveWidget")
        self.outputDriveWidget.setGeometry(QRect(50, 340, 540, 30))

        self.outputDriveLayout = QFormLayout(self.outputDriveWidget)
        self.outputDriveLayout.setObjectName(u"outputDriveLayout")
        self.outputDriveLayout.setContentsMargins(0, 0, 0, 0)

        self.outputDriveLabel = QLabel(self.outputDriveWidget)
        self.outputDriveLabel.setObjectName(u"outputDriveLabel")
        self.outputDriveLayout.setWidget(0, QFormLayout.LabelRole, self.outputDriveLabel)

        self.outputDriveInput = QLineEdit(self.outputDriveWidget)
        self.outputDriveInput.setObjectName(u"outputDriveInput")
        self.outputDriveLayout.setWidget(0, QFormLayout.FieldRole, self.outputDriveInput)

    def setup_select_season_widget(self, main_window):
        self.selectSeasonWidget = QWidget(main_window)
        self.selectSeasonWidget.setObjectName(u"selectSeasonWidget")
        self.selectSeasonWidget.setGeometry(QRect(50, 290, 540, 30))

        self.selectSeasonLayout = QFormLayout(self.selectSeasonWidget)
        self.selectSeasonLayout.setObjectName(u"select_season_layout")
        self.selectSeasonLayout.setContentsMargins(0, 0, 0, 0)

        self.selectSeasonSpin = QSpinBox(self.selectSeasonWidget)
        self.selectSeasonSpin.setObjectName(u"selectSeasonSpin")
        self.selectSeasonSpin.setValue(1)
        self.selectSeasonLayout.setWidget(0, QFormLayout.FieldRole, self.selectSeasonSpin)

        self.selectSeasonLabel = QLabel(self.selectSeasonWidget)
        self.selectSeasonLabel.setObjectName(u"selectSeasonLabel")
        self.selectSeasonLayout.setWidget(0, QFormLayout.LabelRole, self.selectSeasonLabel)

    def setup_select_archive_file_widget(self, main_window):
        self.selectArchiveFileWidget = QWidget(main_window)
        self.selectArchiveFileWidget.setObjectName(u"selectArchiveFileWidget")
        self.selectArchiveFileWidget.setGeometry(QRect(50, 230, 540, 40))

        self.selectArchiveFileLayout = QHBoxLayout(self.selectArchiveFileWidget)
        self.selectArchiveFileLayout.setObjectName(u"selectArchiveFileLayout")
        self.selectArchiveFileLayout.setContentsMargins(0, 0, 0, 0)

        self.selectArchiveFileLabel = QLabel(self.selectArchiveFileWidget)
        self.selectArchiveFileLabel.setObjectName(u"selectArchiveFileLabel")
        self.selectArchiveFileLayout.addWidget(self.selectArchiveFileLabel)

        self.selectArchiveFileInput = QLineEdit(self.selectArchiveFileWidget)
        self.selectArchiveFileInput.setObjectName(u"selectArchiveFileInput")
        self.selectArchiveFileInput.setReadOnly(True)
        self.selectArchiveFileLayout.addWidget(self.selectArchiveFileInput)

        self.selectArchiveFileButton = QToolButton(self.selectArchiveFileWidget)
        self.selectArchiveFileButton.setObjectName(u"selectArchiveFileButton")
        self.selectArchiveFileButton.clicked.connect(self.browse)
        self.selectArchiveFileLayout.addWidget(self.selectArchiveFileButton)

    def setup_execute_button(self, main_window):
        self.executeButton = QPushButton(main_window)
        self.executeButton.setObjectName(u"executeButton")
        self.executeButton.setGeometry(QRect(500, 390, 90, 40))
        self.executeButton.clicked.connect(self.handle_execute)

    def re_translate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"sonarr-subtitle-renamer", None))
        self.searchSeriesLabel.setText(QCoreApplication.translate("main_window", u"番剧名称", None))
        self.searchSeriesButton.setText(QCoreApplication.translate("main_window", u"搜索", None))
        self.selectSeriesLabel.setText(QCoreApplication.translate("main_window", u"选择番剧", None))
        self.outputDriveLabel.setText(QCoreApplication.translate("main_window", u"输出盘符", None))
        self.outputDriveInput.setText(QCoreApplication.translate("main_window", u"Z:\\\\", None))
        self.selectSeasonLabel.setText(QCoreApplication.translate("main_window", u"选择季度", None))
        self.executeButton.setText(QCoreApplication.translate("main_window", u"执行", None))
        self.selectArchiveFileLabel.setText(QCoreApplication.translate("main_window", u"选择文件", None))
        self.selectArchiveFileButton.setText(QCoreApplication.translate("main_window", u"浏览文件", None))

    def browse(self):
        # 路径设置为 None 下次打开会自动定位到上次打开的路径
        filename = QFileDialog.getOpenFileName(None, "选择字幕压缩文件", None, "zip files(*.zip)")[0]
        self.selectArchiveFileInput.setText(filename)

    def handle_search_series(self):
        series_list = renamer.find_series(self.searchSeriesInput.text())
        self.selectSeriesList.clear()
        for series in series_list:
            self.selectSeriesList.addItem(" ".join([series['seriesId'], series['name']]))

    def handle_click_series(self, item):
        self.selectedSeriesId = item.text().split(' ')[0]

    def handle_execute(self):
        series_id = int(self.selectedSeriesId)
        season = int(self.selectSeasonSpin.text())
        zip_file = self.selectArchiveFileInput.text()
        drive = self.outputDriveInput.text()
        # noinspection PyBroadException
        try:
            renamer.rename(series_id, season, zip_file, drive)
            QMessageBox.information(None, '成功', '执行成功')
        except BaseException as e:
            QMessageBox.critical(None, '失败', str(e))
