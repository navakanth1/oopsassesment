class government:
    def __init__(self):
        self.__sale = 100

    def viewsale(self):
        print(self.__sale)
    def increasesale(self,sale):
        self.__sale = sale

centralgov=government()
centralgov.viewsale()

centralgov.__sale = 130
centralgov.viewsale()

centralgov.increasesale(120)
centralgov.viewsale()