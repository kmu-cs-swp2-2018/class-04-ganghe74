class Observer:
    def __init__(self):
        pass

    # View를 통해 출력해야 하지만
    # 편의상 직접 print함
    def notify(self, information):
        print(information)