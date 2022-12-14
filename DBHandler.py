import sqlite3
import datetime


class sqlDB:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):         # Foo 클래스 객체에 _instance 속성이 없다면
            cls._instance = super().__new__(cls)  # Foo 클래스의 객체를 생성하고 Foo._instance로 바인딩
        return cls._instance                      # Foo._instance를 리턴

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init") or cls._init is False:             # Foo 클래스 객체에 _init 속성이 없다면
            self.con = sqlite3.connect('./disaster.db')
            self.cur = self.con.cursor()
            cls._init = True

    def createTabele(self):
        # Create table
        self.cur.execute('pragma foreign_key = on')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS tag
                (TagID INTEGER PRIMARY KEY AUTOINCREMENT, TagName TEXT NOT NULL, StartDate DATE, EndDate DATE)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS program
                (ProgramName TEXT NOT NULL, ProgramID INTEGER PRIMARY KEY AUTOINCREMENT, TagID INTEGER NOT NULL REFERENCES tag(tagID) ON UPDATE CASCADE ON DELETE RESTRICT, Location INTEGER, Weekend INTEGER)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS disaster
               (ProgramID INTEGER NOT NULL REFERENCES tag(ProgramID) ON UPDATE CASCADE ON DELETE RESTRICT, BroadcastDate DATE, Type TEXT,
               Detail TEXT, Speaker TEXT, StartTime DATE, EndTime DATE)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS spot
                (SpotName TEXT, Type Text)''')

    def insertTag(self, tagName, startDate, endDate):
        data = self.searchTag(tagName)

        if data is not None:
            return

        # Insert a row of data
        self.cur.execute('INSERT INTO tag(TagName, StartDate, EndDate) VALUES (:tagName, :startDate, :endDate)', \
            {"tagName":tagName, "startDate": startDate, "endDate":endDate})
        # Save (commit) the changes
        self.con.commit()

        return self.searchTags()

    def searchTags(self):
        self.cur.execute('SELECT * FROM tag')
        rows = self.cur.fetchall()
        return rows

    def searchTag(self, tagName):
        self.cur.execute('SELECT * FROM tag where TagName=:tagName', {"tagName":tagName})
        data = self.cur.fetchone()
        return data

    def searchTagFromDate(self, tagDate):
        self.cur.execute('SELECT TagName FROM tag WHERE date(:tagDate) BETWEEN StartDate AND EndDate', {"tagDate":tagDate})
        data = self.cur.fetchone()
        if data is None:
            return None
        else:
            return (tagDate,)+data

    def modifyTag(self, tagName, startDate, endDate, oldTagName):
        self.cur.execute('UPDATE tag SET TagName=:tagName, startDate = :startDate, endDate = :endDate where TagName = :oldTagName', {"tagName":tagName,"startDate":startDate,"endDate":endDate,"oldTagName":oldTagName})
        self.con.commit()

        return self.searchTags()

    def deleteTag(self, tagName):
        self.cur.execute('DELETE FROM tag where TagName=:tagName', {"tagName":tagName})
        self.con.commit()

        return self.searchTags()

    def searchProgramNameList(self, tagName):
        self.cur.execute('SELECT ProgramName, StartDate, EndDate, Weekend, Location FROM program NATURAL JOIN tag where TagName=:tagName', {"tagName":tagName})
        rows = self.cur.fetchall()
        return rows

    def searchProgramNameWeekList(self, tagName):
        self.cur.execute('SELECT ProgramName, StartDate, EndDate FROM program NATURAL JOIN tag where TagName=:tagName AND Weekend=0', {"tagName":tagName})
        rows = self.cur.fetchall()
        return rows

    def searchProgramNameWeekendList(self, tagName):
        self.cur.execute('SELECT ProgramName, StartDate, EndDate FROM program NATURAL JOIN tag where TagName=:tagName AND Weekend=1', {"tagName":tagName})
        rows = self.cur.fetchall()
        return rows

    def searchProgram(self, tagName, programName, isWeekend):
        self.cur.execute('SELECT ProgramName FROM program NATURAL JOIN tag where TagName=:tagName and ProgramName=:programName AND Weekend=:isWeekend', {"tagName":tagName, "programName":programName, "isWeekend":int(isWeekend)})
        data = self.cur.fetchone()
        return data

    def insertProgram(self, tagName, programName, location, isWeekend):
        programNameList = self.searchProgram(tagName, programName, int(isWeekend))
        
        if programNameList is not None:
            # 프로그램 이름 중복
            return

        self.cur.execute('SELECT TagID FROM tag WHERE TagName=:tagName', {"tagName":tagName})
        tagID = self.cur.fetchone()
        # Insert a row of data
        self.cur.execute('INSERT INTO program(ProgramName, TagID, Location, Weekend) VALUES (:programName, :tagID, :location, :isWeekend)', \
            {"programName":programName, "tagID": tagID[0], "location": int(location), "isWeekend":int(isWeekend)})
        # Save (commit) the changes
        self.con.commit()

    def modifyProgram(self, tagName, programName, oldProgramName, oldIsWeekend, location, isWeekend):
        
        self.cur.execute('SELECT TagID FROM tag WHERE TagName=:tagName', {"tagName":tagName})
        tagID = self.cur.fetchone()
        if tagID is None:
            return

        self.cur.execute('SELECT rowID FROM program WHERE ProgramName=:oldProgramName AND Weekend=:oldIsWeekend AND TagID=:tagID', {"oldProgramName":oldProgramName, "oldIsWeekend":int(oldIsWeekend), "tagID":tagID[0]})
        rawID = self.cur.fetchone()
        
        if rawID is None:
            return
        
        self.cur.execute('UPDATE program SET ProgramName =:programName, Location=:location, Weekend=:isWeekend where rowID=:rowID', {"programName":programName,"rowID":rawID[0], "location":int(location), "isWeekend":int(isWeekend)})
        self.con.commit()

    def deleteProgram(self, tagName, programName, oldIsWeekend):
        self.cur.execute('SELECT TagID FROM tag WHERE TagName=:tagName', {"tagName":tagName})
        tagID = self.cur.fetchone()
        if tagID is None:
            return
        
        self.cur.execute('DELETE FROM program where ProgramName=:programName AND tagID=:tagID AND Weekend=:oldIsWeekend', {"tagID":tagID[0], "programName":programName, "oldIsWeekend":int(oldIsWeekend)})
        self.con.commit()

    def searchSpotNameList(self):
        self.cur.execute('SELECT * FROM spot')
        rows = self.cur.fetchall()
        return rows

    def searchSpot(self, spotName):
        self.cur.execute('SELECT SpotName, Type FROM spot where SpotName=:spotName', {"spotName":spotName})
        data = self.cur.fetchone()
        return data

    def insertSpot(self, spotName, spotType):
        name = self.searchSpot(spotName)
        if name is not None:
            # 태그명이 중복될 경우
            return
        self.cur.execute('INSERT INTO spot(SpotName, Type) VALUES (:spotName, :type)', \
            {"spotName":spotName, "type":spotType})
        # Save (commit) the changes
        self.con.commit()

        return self.searchSpotNameList()

    def modifySpot(self, spotName, oldSpotName, type):
        self.cur.execute('UPDATE spot SET SpotName =:spotName, Type=:type where SpotName =:oldSpotName', {"spotName":spotName,"oldSpotName":oldSpotName, "type":type})
        self.con.commit()

        return self.searchSpotNameList()

    def deleteSpot(self, spotName):
        self.cur.execute('DELETE FROM spot where SpotName=:spotName', {"spotName":spotName})
        self.con.commit()

        return self.searchSpotNameList()

    def searchBroadcastDate(self, broadcastDate):
        self.cur.execute('SELECT ProgramName, Type, Detail, Speaker, StartTime, EndTime, location FROM disaster NATURAL JOIN program WHERE BroadcastDate=:broadcastDate ORDER BY StartTime', {"broadcastDate":broadcastDate})
        rows = self.cur.fetchall()
        return [broadcastDate]+rows

    def searchBroadcastDateWithProgram(self, broadcastDate, programName):
        self.cur.execute('SELECT ProgramName, Type, Detail, Speaker, StartTime, EndTime, location FROM disaster NATURAL JOIN program WHERE BroadcastDate=:broadcastDate AND ProgramName=:programName ORDER BY StartTime', {"broadcastDate":broadcastDate, "programName":programName})
        rows = self.cur.fetchall()
        return [broadcastDate]+rows

    def searchBroadcastList(self, startDate, endDate, programName):
        if programName is None:
            self.cur.execute('SELECT BroadcastDate, ProgramName, Type, Detail, Speaker, StartTime, EndTime FROM disaster NATURAL JOIN program WHERE BroadcastDate BETWEEN :startDate AND :endDate', {"startDate":startDate, "endDate":endDate})
        else:
            self.cur.execute('SELECT BroadcastDate, ProgramName, Type, Detail, Speaker, StartTime, EndTime FROM disaster NATURAL JOIN program WHERE BroadcastDate BETWEEN :startDate AND :endDate AND ProgramName=:programName', {"startDate":startDate, "endDate":endDate, "programName":programName})
        rows = self.cur.fetchall()
        return rows

    def insertDisaster(self, broadcastDate, programName, type, detail, speaker, startTime, endTime):
        self.cur.execute('SELECT ProgramID FROM program NATURAL JOIN tag WHERE ProgramName=:programName AND date(:broadcastDate) BETWEEN StartDate AND EndDate', {"programName":programName, "broadcastDate":broadcastDate})
        programID = self.cur.fetchone()[0]

        if speaker == 'SPOT':
            self.cur.execute('SELECT Type FROM spot WHERE SpotName=:spotName', {"spotName":detail})
            type = self.cur.fetchone()[0]

        self.cur.execute('INSERT INTO disaster(ProgramID, BroadcastDate, Type, Detail, Speaker, StartTime, EndTime) VALUES (:programID, :broadcastDate, :type, :detail, :speaker, :startTime, :endTime)', {"programID":programID, "broadcastDate":broadcastDate, "type":type, "detail":detail, "speaker":speaker, "startTime":startTime, "endTime":endTime})
        self.con.commit()

        return self.searchBroadcastDate(broadcastDate)

    def searchDisaster(self, broadcastDate, startTime, endTime):
        
        self.cur.execute('SELECT rowID From disaster where BroadcastDate=:broadcastDate AND StartTime=:startTime AND EndTime=:endTime', {"broadcastDate":broadcastDate, "startTime":startTime, "endTime":endTime})
        row = self.cur.fetchone()
        
        return row

    def modifyDisaster(self, rowId, broadcastDate, programName, inputType, detail, speaker, startTime, endTime):
        
        curDate = datetime.date.fromisoformat(broadcastDate)
        dayNum = curDate.isoweekday()
        if dayNum == 6 or dayNum == 7:
            isWeekend = 1
        else:
            isWeekend = 0
        
        self.cur.execute('SELECT ProgramID FROM program NATURAL JOIN tag WHERE ProgramName=:programName AND Weekend=:isWeekend AND date(:broadcastDate) BETWEEN StartDate AND EndDate', {"programName":programName, "broadcastDate":broadcastDate, "isWeekend":isWeekend})
        rawProgramID=self.cur.fetchone()

        if rawProgramID is None:
            return
        programID = rawProgramID[0]

        if speaker == 'SPOT':
            self.cur.execute('SELECT Type FROM spot WHERE SpotName=:spotName', {"spotName":detail})
            inputType = self.cur.fetchone()[0]
        self.cur.execute('UPDATE disaster SET ProgramID=:programID, BroadcastDate=:broadcastDate, Type=:type, Detail=:detail, Speaker=:speaker, StartTime=:startTime, EndTime=:endTime WHERE rowID=:rowId', {"programID":programID, "broadcastDate":broadcastDate, "type":inputType, "detail":detail, "speaker":speaker, "startTime":startTime, "endTime":endTime, "rowId":int(rowId)})
        self.con.commit()

        return self.searchBroadcastDate(broadcastDate)

    def deleteDisaster(self, rowId, broadcastDate):
        self.cur.execute('DELETE FROM disaster where rowID=:rowId', {"rowId":rowId})
        self.con.commit()

        return self.searchBroadcastDate(broadcastDate)

    def closeDB(self):
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.con.close()
        cls = type(self)
        cls._init = False