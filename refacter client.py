import sys
from ui_main import *
import settingHandler
import datetime
from pytimekr import pytimekr
from openpyxl import Workbook
from openpyxl.styles import Alignment, PatternFill, Border, Side
from openpyxl.styles.fonts import Font
from emit import setMessageSig
from communicationClient import *
import ui_IPSettings
import time
import ui_confirm

class myApplication(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("재난취합클라이언트")

        self.initCommunication()


        self.initParameters()
        self.initUI()

#######################################################################################
#                                    init Func                                        #
#######################################################################################

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F2:
            settingWindow = Settings()
            settingWindow.exec()

    def initCommunication(self):
        try:
            Info = settingHandler.loadSettings()
            bridge = setMessageSig()
            self.communication = Client()
            self.communication.bridge = bridge
            bridge.DBmessageSig.connect(self.receiveDBData)
            bridge.socketStateSig.connect(self.alertSocketState)
            self.communication.connect(Info,9080)
            self.communication.start()
            time.sleep(1)
        except:
            pass

    def initParameters(self):
        self.ui.dataTable.setFocus()
        self.ui.disasterInputButton.clicked.connect(self.disasterAdd)
        self.ui.spotInputButton.clicked.connect(self.spotAdd)
        self.ui.programInputButton.clicked.connect(self.programAdd)

        self.tagListIndex = -1
        self.modifyDisastorType = -1
        today = str(datetime.date.today())
        self.ui.reportDate.setDate(QDate.fromString(today, 'yyyy-MM-dd'))
        self.ui.tagStartDate.setDate(QDate.fromString(today, 'yyyy-MM-dd'))
        self.ui.tagEndDate.setDate(QDate.fromString(today, 'yyyy-MM-dd'))
        self.ui.dataSearchEdit.setDate(QDate.fromString(today, 'yyyy-MM-dd'))

    def initUI(self):
        self.ui.tabWidget.setTabVisible(2, False)
        # tab 숨기기 
        self.ui.tabWidget.setTabVisible(1, False)
        #
        self.ui.tagTable.setColumnCount(3)
        self.communication.requestDBFunc(client=None, context=1, request=1,data=None)
        
        self.communication.requestDBFunc(client=None, context=2, request=13,data=None)
        
        self.ui.dataSearchButton.clicked.connect(self.searchData)
        self.ui.nextDate.clicked.connect(self.nextDate)
        self.ui.preDate.clicked.connect(self.preDate)
        
        self.ui.tagTable.itemDoubleClicked.connect(self.tagModify)

        self.ui.tagAddButton.clicked.connect(self.tagAdd)
        self.ui.tagDelButton.clicked.connect(self.tagDel)

        self.ui.findTaggedProgram.clicked.connect(self.searchProgramName)
        self.ui.programNameAddButton.clicked.connect(self.programNameAdd)
        self.ui.programNameTable.itemDoubleClicked.connect(self.programModify)
        self.ui.programNameDelButton.clicked.connect(self.programDel)

        self.ui.spotAddButton.clicked.connect(self.spotNameAdd)
        self.ui.spotDelButton.clicked.connect(self.spotNameDel)
        self.ui.spotTable.itemDoubleClicked.connect(self.spotNameModify)

        self.ui.reportDate.dateChanged.connect(lambda: self.communication.requestDBFunc(client=None, context=3,request=3,data=(self.ui.reportDate.date().toString('yyyy-MM-dd'),)))
        
        self.ui.dataTable.itemDoubleClicked.connect(self.findDisasterToModify)
        
        self.ui.delDisasterButton.clicked.connect(self.deleteDisaster)

        self.ui.tagModifyButton.clicked.connect(self.modifyTag)
        self.ui.programModifyButton.clicked.connect(self.modifyProgram)
        self.ui.spotModifyButton.clicked.connect(self.modifySpot)

        self.ui.reportStartTime.timeChanged.connect(self.updateEndTime)

        self.ui.modifyDisasterButton.clicked.connect(self.modifyDisaster)

    def closeEvent(self, e):
        self.communication.stop()
        e.accept()

#######################################################################################
#                                Communication Func                                   #
#######################################################################################

    @Slot(str)
    def alertSocketState(self, err):
        if self.communication.getStatus() != 2:
            msgBox = QMessageBox.critical(self, '통신 에러!', err)

    @Slot(int, list)
    def receiveDBData(self, requestContext, recData):
        if requestContext == 0:
            # CreateDB
            pass
        elif requestContext == 1:
            #searchTags
            self.searchTags(recData)
        elif requestContext == 2:
            self.searchSpotNameList(recData)
        elif requestContext == 3:
            self.searchTagToUpdateProgramList(recData)
        elif requestContext == 4:
            # searchData, nextDate, preDate
            self.addToMainTable(recData[1:])
        elif requestContext == 5:
            # disastor add
            self.addToMainTable(recData[1:])
        elif requestContext == 6:
            self.updateProgramList(recData)
        elif requestContext == 7:
            self.addProgramNameList(recData)
        elif requestContext == 9:
            self.communication.requestDBFunc(client=None, context=2, request=13,data=None)
        elif requestContext == 13:
            self.disasterModifyState = int(recData[0])
            self.modifyDisasterLoad()

#######################################################################################
#                                   Search Func                                       #
#######################################################################################

    def searchData(self):
        date = self.ui.dataSearchEdit.date()
        self.communication.requestDBFunc(client=None, context=4, request=18, data=(date.toString('yyyy-MM-dd'),))

    def nextDate(self):
        date = self.ui.dataSearchEdit.date().addDays(1)
        self.ui.dataSearchEdit.setDate(date)
        self.communication.requestDBFunc(client=None, context=4, request=18, data=(date.toString('yyyy-MM-dd'),))

    def preDate(self):
        date = self.ui.dataSearchEdit.date().addDays(-1)
        self.ui.dataSearchEdit.setDate(date)
        self.communication.requestDBFunc(client=None, context=4, request=18, data=(date.toString('yyyy-MM-dd'),))

    def addToMainTable(self, disasterList):
        self.ui.dataTable.clearContents()
        self.clearDisasterArea()
        self.clearSpotArea()
        self.clearProgramArea()
        self.ui.dataTable.setRowCount(len(disasterList))
        for index, disaster in enumerate(disasterList):
            self.ui.dataTable.setItem(index, 0, QTableWidgetItem(disaster[0])) # 프로그램 명
            self.ui.dataTable.setItem(index, 1, QTableWidgetItem(disaster[1])) # 재난유형
            self.ui.dataTable.setItem(index, 2, QTableWidgetItem(disaster[2])) # 세부내용
            self.ui.dataTable.setItem(index, 3, QTableWidgetItem(disaster[3])) # 출연자명
            self.ui.dataTable.setItem(index, 4, QTableWidgetItem(disaster[4]+'~'+disaster[5]))# 방송시간
            if (QTime().fromString(disaster[4],'hh:mm:ss').secsTo(QTime().fromString(disaster[5],'hh:mm:ss'))) % 60 == 0:
                duration = (QTime().fromString(disaster[4],'hh:mm:ss').secsTo(QTime().fromString(disaster[5],'hh:mm:ss')))//60
            else:
                duration = (QTime().fromString(disaster[4],'hh:mm:ss').secsTo(QTime().fromString(disaster[5],'hh:mm:ss')))//60 + 1
            self.ui.dataTable.setItem(index, 5,QTableWidgetItem(str(duration)))
        self.disasterModifyState = -1


#######################################################################################
#                                       Tab#1                                         #
#######################################################################################

    def searchTagToUpdateProgramList(self, recData):
        self.ui.reportProgram.clear()

        if recData is None:
            return
        isWeekend = datetime.date.fromisoformat(recData[0]).isoweekday()
        if isWeekend == 6 or isWeekend ==7:
            self.communication.requestDBFunc(client=None, context=6,request=8,data=(recData[1],))
        else:
            self.communication.requestDBFunc(client=None, context=6,request=7,data=(recData[1],))
        
    def updateProgramList(self, recData):
        programNameList = list(map(convertToList, recData))
        self.ui.reportProgram.addItems(programNameList)
        self.ui.reportProgram.setCurrentIndex(-1)

    def updateEndTime(self):
        self.ui.reportEndTime.setTime(self.ui.reportStartTime.time())

#######################################################################################
#                                    Clear Func                                       #
#######################################################################################

    def clearDisasterArea(self):
        self.ui.disasterType.clear()
        self.ui.disasterDetail.clear()

    def clearSpotArea(self):
        self.ui.spotDetail.setCurrentIndex(-1)

    def clearProgramArea(self):
        self.ui.programDetail.clear()
        self.ui.programSpeaker.clear()
        self.ui.programType.clear()

#######################################################################################
#                                      Add Func                                       #
#######################################################################################

    def disasterAdd(self):
        confirmWindow = Confirm()
        returnData = confirmWindow.exec()
        if returnData == 0:
            return
        
        date = self.ui.reportDate.date()
        programName = self.ui.reportProgram.currentText()
        type = self.ui.disasterType.text()
        detail = self.ui.disasterDetail.text()
        startTime = self.ui.reportStartTime.time()
        endTime = self.ui.reportEndTime.time()

        if type == '' or detail == '':
            return

        self.communication.requestDBFunc(client=None, context=5, request=20, data=(date.toString('yyyy-MM-dd'), programName, type, detail, '재난수신클라이언트', startTime.toString('hh:mm:ss'), endTime.toString('hh:mm:ss')))
        self.ui.dataSearchEdit.setDate(date)
        self.clearDisasterArea()

    def spotAdd(self):
        confirmWindow = Confirm()
        returnData = confirmWindow.exec()
        if returnData == 0:
            return

        
        date = self.ui.reportDate.date()
        programName = self.ui.reportProgram.currentText()
        detail = self.ui.spotDetail.currentText()
        startTime = self.ui.reportStartTime.time()
        endTime = self.ui.reportEndTime.time()

        if detail == '':
            return

        self.communication.requestDBFunc(client=None, context=5, request=20, data=(date.toString('yyyy-MM-dd'), programName, '', detail, 'SPOT', startTime.toString('hh:mm:ss'), endTime.toString('hh:mm:ss')))
        self.ui.dataSearchEdit.setDate(date)
        self.clearSpotArea()

    def programAdd(self):
        confirmWindow = Confirm()
        returnData = confirmWindow.exec()
        if returnData == 0:
            return

        
        date = self.ui.reportDate.date()
        programName = self.ui.reportProgram.currentText()
        type = self.ui.programType.text()
        detail = self.ui.programDetail.text()
        speaker = self.ui.programSpeaker.text()
        startTime = self.ui.reportStartTime.time()
        endTime = self.ui.reportEndTime.time()

        if type == '' or detail == '':
            return
        if speaker == '':
            speaker = '-'

        self.communication.requestDBFunc(client=None, context=5, request=20, data=(date.toString('yyyy-MM-dd'), programName, type, detail, speaker, startTime.toString('hh:mm:ss'), endTime.toString('hh:mm:ss')))
        self.ui.dataSearchEdit.setDate(date)
        self.clearProgramArea()

#######################################################################################
#                                      Modify Func                                    #
#######################################################################################

    def findDisasterToModify(self):
        self.clearDisasterArea()
        self.clearSpotArea()
        self.clearProgramArea()
        self.ui.spotDetail.setCurrentIndex(-1)
        selectedRowIndex = self.ui.dataTable.currentRow()
        oldStartTime, oldEndTime = self.ui.dataTable.item(selectedRowIndex, 4).text().split('~')
        self.communication.requestDBFunc(client=None, context=13, request=22, data=(self.ui.dataSearchEdit.date().toString('yyyy-MM-dd'), oldStartTime, oldEndTime))

    def modifyDisasterLoad(self):
        selectedRowIndex = self.ui.dataTable.currentRow()
        programName = self.ui.dataTable.item(selectedRowIndex, 0).text()
        self.ui.reportDate.setDate(self.ui.dataSearchEdit.date())
        self.ui.reportProgram.setCurrentIndex(self.ui.reportProgram.findText(programName))
        oldStartTime, oldEndTime = self.ui.dataTable.item(selectedRowIndex, 4).text().split('~')
        self.ui.reportStartTime.setTime(QTime().fromString(oldStartTime,"hh:mm:ss"))
        self.ui.reportEndTime.setTime(QTime().fromString(oldEndTime,"hh:mm:ss"))
        if self.ui.dataTable.item(selectedRowIndex, 3).text() == 'SPOT':
            # 스팟
            self.ui.spotDetail.setCurrentIndex(self.ui.spotDetail.findText(self.ui.dataTable.item(selectedRowIndex, 2).text()))
            self.modifyDisastorType = 1
        elif self.ui.dataTable.item(selectedRowIndex, 3).text() == '재난수신클라이언트':
            # 재난
            self.ui.disasterDetail.setText(self.ui.dataTable.item(selectedRowIndex, 2).text())
            self.ui.disasterType.setText(self.ui.dataTable.item(selectedRowIndex, 1).text())
            self.modifyDisastorType = 2
        else:
            self.ui.programDetail.setText(self.ui.dataTable.item(selectedRowIndex, 2).text())
            self.ui.programType.setText(self.ui.dataTable.item(selectedRowIndex, 1).text())
            self.ui.programSpeaker.setText(self.ui.dataTable.item(selectedRowIndex, 3).text())
            self.modifyDisastorType = 3

    def modifyDisaster(self):
        confirmWindow = Confirm()
        confirmWindow.setValue('수정하시겠습니까?')
        returnData = confirmWindow.exec()
        if returnData == 0:
            return
        date = self.ui.reportDate.date()
        programName = self.ui.reportProgram.currentText()
        startTime = self.ui.reportStartTime.time()
        endTime = self.ui.reportEndTime.time()
        
        if self.modifyDisastorType == 2:
            #재난
            inputType = self.ui.disasterType.text()
            detail = self.ui.disasterDetail.text()
            self.communication.requestDBFunc(client=None, context=5, request=23, data=(str(self.disasterModifyState), date.toString('yyyy-MM-dd'), programName, inputType, detail, '재난수신클라이언트', startTime.toString('hh:mm:ss'), endTime.toString('hh:mm:ss')))
        elif self.modifyDisastorType == 1:
            #SPOT
            detail = self.ui.spotDetail.currentText()
            self.communication.requestDBFunc(client=None, context=5, request=23, data=(str(self.disasterModifyState), date.toString('yyyy-MM-dd'), programName, '', detail, 'SPOT', startTime.toString('hh:mm:ss'), endTime.toString('hh:mm:ss')))
        elif self.modifyDisastorType == 3:
            #멘트
            inputType = self.ui.programType.text()
            detail = self.ui.programDetail.text()
            speaker = self.ui.programSpeaker.text()
            self.communication.requestDBFunc(client=None, context=5, request=23, data=(str(self.disasterModifyState), date.toString('yyyy-MM-dd'), programName, inputType, detail, speaker, startTime.toString('hh:mm:ss'), endTime.toString('hh:mm:ss')))
        self.modifyDisastorType = -1
        self.disasterModifyState = -1

#######################################################################################
#                                      Delete Func                                    #
#######################################################################################

    def deleteDisaster(self):
        self.communication.requestDBFunc(client=None, context=5, request=24, data=(str(self.disasterModifyState), self.ui.dataSearchEdit.date().toString('yyyy-MM-dd')))

#######################################################################################
#                                       Tab#2                                         #
#######################################################################################

#######################################################################################
#                                       Tag Area                                      #
#######################################################################################

    def tagAdd(self):
        newTag = self.ui.tagInput.text()
        if newTag == '':
            # 입력이 없을 경우
            return
        startDate = self.ui.tagStartDate.date()
        endDate = self.ui.tagEndDate.date()
        if startDate > endDate:
            # 기간이 이상할 경우 
            return
        startDate = startDate.toString('yyyy-MM-dd')
        endDate = endDate.toString('yyyy-MM-dd')
        self.communication.requestDBFunc(client=None, context=1, request=0,data=(newTag,startDate,endDate))

    def tagDel(self):
        if self.tagModifyState < 0:
            # 선택되지 않았을 경우
            return
        self.communication.requestDBFunc(client=None, context=1, request=5,data=(self.ui.tagTable.item(self.tagModifyState, 0).text(),))

    def tagModify(self):
        selectedRowIndex = self.ui.tagTable.currentRow()
        self.ui.tagInput.setText(self.ui.tagTable.item(selectedRowIndex, 0).text())
        self.ui.tagStartDate.setDate(QDate.fromString(self.ui.tagTable.item(selectedRowIndex, 1).text(), "yyyy-MM-dd"))
        self.ui.tagEndDate.setDate(QDate.fromString(self.ui.tagTable.item(selectedRowIndex, 2).text(), "yyyy-MM-dd"))
        self.tagModifyState = selectedRowIndex

    def modifyTag(self):
        newTag = self.ui.tagInput.text()
        if newTag == '':
            # 입력이 없을 경우
            return
        startDate = self.ui.tagStartDate.date()
        endDate = self.ui.tagEndDate.date()
        if startDate > endDate:
            # 기간이 이상할 경우 
            return
        startDate = startDate.toString('yyyy-MM-dd')
        endDate = endDate.toString('yyyy-MM-dd')
        self.communication.requestDBFunc(client=None, context=1, request=4,data=(newTag,startDate,endDate, self.ui.tagTable.item(self.tagModifyState, 0).text()))
        


#######################################################################################
#                                  Tag&Program Area                                   #
#######################################################################################

    def searchTags(self, recData):
        self.ui.tagInput.clear()
        self.ui.tagList.clear()
        self.ui.tagTable.setSortingEnabled(False)
        self.ui.tagTable.setRowCount(len(recData))
        for rowIndex, tag in enumerate(recData):
            for columnIndex, data in enumerate(tag):
                if columnIndex == 0:
                    continue
                self.ui.tagTable.setItem(rowIndex, columnIndex-1,QTableWidgetItem(data))
                if columnIndex == 1:
                    self.ui.tagList.addItem(data)
                    self.ui.createTagNameList.addItem(data)
        self.ui.tagTable.setSortingEnabled(True)
        self.tagModifyState = -1
        self.ui.tagTable.setCurrentCell(-1,1,QItemSelectionModel.Clear)
        self.ui.tagList.setCurrentIndex(-1)
        self.ui.createTagNameList.setCurrentIndex(-1)

#######################################################################################
#                                    Program Area                                     #
#######################################################################################

    def searchProgramName(self):
        self.tagListIndex = self.ui.tagList.currentIndex()
        if self.tagListIndex < 0:
            return
        self.ui.programNameTable.clearContents()
        self.ui.programNameInput.clear()
        self.ui.locationBox.setCheckState(Qt.CheckState.Unchecked)
        self.ui.weekendBox.setCheckState(Qt.CheckState.Unchecked)
        tagName = self.ui.tagList.itemText(self.tagListIndex)
        self.communication.requestDBFunc(client=None, context=7, request=6,data=(tagName,))
        
    def addProgramNameList(self,recData):
        self.ui.programNameTable.setRowCount(len(recData))
        for index, row in enumerate(recData):
            self.ui.programNameTable.setItem(index, 0, QTableWidgetItem(row[0]))
            if row[3] == '1':
                self.ui.programNameTable.setItem(index, 1, QTableWidgetItem('주말'))
            if row[4] == '1':
                self.ui.programNameTable.setItem(index, 2, QTableWidgetItem('로컬'))
        self.ui.programNameTable.setCurrentCell(-1,1,QItemSelectionModel.Clear)
        self.programModifyState = -1

    def programNameAdd(self):
        if self.tagListIndex < 0:
            return
        programName = self.ui.programNameInput.text()
        tagName = self.ui.tagList.itemText(self.tagListIndex)
        location = self.ui.locationBox.checkState()
        isWeekend = self.ui.weekendBox.checkState()
        
        if location == Qt.CheckState.Checked:
            location = True
        else:
            location = False
        if isWeekend == Qt.CheckState.Checked:
            isWeekend = True
        else:
            isWeekend = False

        self.communication.requestDBFunc(client=None, context=8, request=10, data=(tagName, programName, str(int(location)), str(int(isWeekend))))
        
        self.ui.tagList.setCurrentIndex(self.tagListIndex)
        self.searchProgramName()

    def modifyProgram(self):

        if self.programModifyState < 0:
            return

        programName = self.ui.programNameInput.text()
        tagName = self.ui.tagList.itemText(self.tagListIndex)
        location = self.ui.locationBox.checkState()
        isWeekend = self.ui.weekendBox.checkState()

        if location is Qt.CheckState.Checked:
            location = True
        else:
            location = False

        if isWeekend is Qt.CheckState.Checked:
            isWeekend = True
        else:
            isWeekend = False

        oldIsWeekend = self.ui.programNameTable.item(self.programModifyState, 1)
        if oldIsWeekend is None:
            oldIsWeekend = 0
        else:
            oldIsWeekend = 1
        
        self.communication.requestDBFunc(client=None, context=8, request=11, data=(tagName, programName, self.ui.programNameTable.item(self.programModifyState, 0).text(), str(oldIsWeekend), str(int(location)), str(int(isWeekend))))
        self.ui.tagList.setCurrentIndex(self.tagListIndex)
        self.searchProgramName()

    def programModify(self):
        selectedRowIndex = self.ui.programNameTable.currentRow()
        self.ui.weekendBox.setChecked(Qt.CheckState.Unchecked)
        self.ui.locationBox.setChecked(Qt.CheckState.Unchecked)
        self.ui.programNameInput.setText(self.ui.programNameTable.item(selectedRowIndex, 0).text())
        if self.ui.programNameTable.item(selectedRowIndex, 1) is not None:
            self.ui.weekendBox.setChecked(Qt.CheckState.Checked)
        if self.ui.programNameTable.item(selectedRowIndex, 2) is not None:
            self.ui.locationBox.setChecked(Qt.CheckState.Checked)
        self.programModifyState = selectedRowIndex

    def programDel(self):
        if self.programModifyState < 0:
            # 선택되지 않았을 경우
            return
        tagName = self.ui.tagList.itemText(self.tagListIndex)
        oldIsWeekend = self.ui.programNameTable.item(self.programModifyState, 1)
        if oldIsWeekend is None:
            oldIsWeekend = 0
        else:
            oldIsWeekend = 1
        self.communication.requestDBFunc(client=None, context=8, request=12, data=(tagName, self.ui.programNameTable.item(self.programModifyState, 0).text(), str(oldIsWeekend)))
        self.searchProgramName()

#######################################################################################
#                                      SPOT Area                                      #
#######################################################################################

    def spotNameAdd(self):
        newSpot = self.ui.spotInput.text()
        newSpotType = self.ui.spotTypeInput.text()
        if newSpot == '':
            # 입력이 없을 경우
            return
        self.communication.requestDBFunc(client=None, context=2, request=15,data=(newSpot,newSpotType))
        
    def spotNameDel(self):
        if self.spotModifyState < 0:
            # 선택되지 않았을 경우
            return
        self.communication.requestDBFunc(client=None, context=2, request=17, data=(self.ui.spotTable.item(self.spotModifyState, 0).text(),))

    def modifySpot(self):
        newSpot = self.ui.spotInput.text()
        newSpotType = self.ui.spotTypeInput.text()
        if newSpot == '':
            # 입력이 없을 경우
            return
        self.communication.requestDBFunc(client=None, context=2, request=16,data=(newSpot, self.ui.spotTable.item(self.spotModifyState, 0).text(), newSpotType))

    def spotNameModify(self):
        selectedRowIndex = self.ui.spotTable.currentRow()
        self.ui.spotInput.setText(self.ui.spotTable.item(selectedRowIndex, 0).text())
        self.ui.spotTypeInput.setText(self.ui.spotTable.item(selectedRowIndex, 1).text())
        self.spotModifyState = selectedRowIndex

    def searchSpotNameList(self, recData):
        self.ui.spotTable.clearContents()
        self.ui.spotInput.clear()
        self.ui.spotTypeInput.clear()
        self.ui.spotDetail.clear()
        self.ui.spotTable.setRowCount(len(recData))
        for index, row in enumerate(recData):
            self.ui.spotTable.setItem(index, 0, QTableWidgetItem(row[0]))
            self.ui.spotTable.setItem(index, 1, QTableWidgetItem(row[1]))
        spotList = list(map(convertToList,recData))
        self.ui.spotDetail.addItems(spotList)
        self.ui.spotDetail.setCurrentIndex(-1)
        self.ui.spotTable.setCurrentCell(-1,1,QItemSelectionModel.Clear)
        self.spotModifyState = -1

#######################################################################################
#                                     Sub Func                                        #
#######################################################################################

def convertToList(dataRows):
    return(dataRows[0])

#######################################################################################
#                                     Setting                                         #
#######################################################################################
class Settings(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_IPSettings.Ui_Dialog()
        self.ui.setupUi(self)
        Settings = settingHandler.loadSettings()
        self.ui.lineEdit.setText(Settings)
        self.show()

    def saveSettings(self):
        settingHandler.saveSettings(self.ui.lineEdit.text())

    def accept(self):
        self.saveSettings()
        super().accept()

class Confirm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_confirm.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

    def setValue(self, stringData):
        self.ui.label.setText(stringData)

#######################################################################################
#                                        Main                                        #
#######################################################################################

if __name__ == '__main__':
    app = QApplication()
    window = myApplication()
    window.show()

    sys.exit(app.exec_())