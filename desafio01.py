num1= int(input("Informe a primeira hora"))
num2= int(input("Informe a primeira minutos"))
num3= int(input("Informe a segunda hora"))
num4= int(input("Informe a segunda minutos"))

somahora = (num1 + num3)
somaminuto = (num2 + num4)
if somaminuto >= 60:
    somahora +=1




print(somahora, somaminuto)
