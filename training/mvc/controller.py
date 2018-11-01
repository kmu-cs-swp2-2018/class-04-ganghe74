import pickle

from model import Model

class Controller:
    def __init__(self, model, fileName):
        self.model = model
        self.dbfilename = fileName

    def addRecord(self, record): # MVC 패턴의 잘못된 예 / Controller에서 직접 데이터를 수정함, model에서 수정해야됨, Exception 처리를 위한 데이터 접근은 가능
        db = self.model.getScoreDB()
        db += [record]

    def findScoreDB(self, keyname):
        db = self.model.getScoreDB()        
        msg = ""        
        for p in db:
          if p['Name'] != keyname:
              continue          
          for attr in sorted(p):
               msg += attr + "=" + str(p[attr]) + "    \t"
          msg += "\n"

        return msg
        
    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            return

        # Unmarshalling 
        try:
            db =  pickle.load(fH)
            self.model.setScoreDB(db)
            return
        except:
            pass
        else:
            pass
        
        # Close handle
        fH.close()

    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        db = self.model.getScoreDB()
        pickle.dump(db, fH)
        fH.close()
