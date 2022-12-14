import openpyxl
from openpyxl import Workbook
import datetime

class excelHandler:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):         # Foo 클래스 객체에 _instance 속성이 없다면
            cls._instance = super().__new__(cls)  # Foo 클래스의 객체를 생성하고 Foo._instance로 바인딩
        return cls._instance                      # Foo._instance를 리턴

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):             # Foo 클래스 객체에 _init 속성이 없다면
            self.workBook = Workbook()
            cls._init = True

    def createSheet(self):
        pass
    

    def saveFile(self, fileName):
        self.wb.save(fileName)