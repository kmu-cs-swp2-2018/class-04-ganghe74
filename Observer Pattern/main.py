# main.py
from Observer import Observer
from Observable import Observable

observer = Observer()
observable = Observable()

observable.registerObserver(observer)
observable.updateInformation("올해는 2018년")
