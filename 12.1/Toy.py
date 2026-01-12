# מבחן מה״ט 2024 אביב ב` שאלה 7:
class Toy:
    def __init__(self,code,age,price,is_possible):
        self.code = code
        self.age = age
        self.price = price
        self.is_possible = is_possible
def special_toy(code,price):
    return Toy(code,10,price,True)
      

        