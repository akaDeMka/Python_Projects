from decimal import Decimal
user_weight=input("Введите ваш вес, кг: ")
user_height=input("Введите ваш рост, см: ")
user_height=Decimal(user_height)/100
user_weight=Decimal(user_weight)
imt=user_weight/(user_height*user_height)
print("Ваш индекс тела -",imt.quantize(Decimal("1.00")))
