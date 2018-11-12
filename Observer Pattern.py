# 옵저버 패턴 보고서 예제코드

class Observer:
    def __init__(self):
        pass

    # View를 통해 출력해야 하지만
    # 편의상 옵저버 안에 포함시킴
    def notify(self, information):
        print(information)

class Observable:
    def __init__(self):
        self.observerCollection = []
    
    def registerObserver(self, observer):
        self.observerCollection.append(observer)

    def unregisterObserver(self, observer):
        if observer in self.observerCollection:
            self.observerCollection.remove(observer)
    
    def notifyObservers(self, information):
        for ob in self.observerCollection:
            ob.notify(information)


    # 관찰대상(모델) 의 정보를 변화시키는 함수
    # 편의상 옵저버블 안에 포함시킴
    def updateInformation(self, information):
        self.data = information
        self.notifyObservers(self.data)

observer = Observer()
observable = Observable()

observable.registerObserver(observer)
observable.updateInformation("올해는 2018년")