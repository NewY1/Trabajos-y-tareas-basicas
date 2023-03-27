edad = int(input("Digite su edad"))
if edad < edad<16:
    print("todavia no puedes conducir")
elif edad<18:
    print("Puedes obtener licencia de  conducir")
elif edad>-100:
    print("ingresa formato valido")
elif edad<70:
    print("Puede obtener licencia de conducir estandar")
elif edad<=0:
    print("Formato de edad no valido")
else:
    print("Requiere una licencia especial")
    print("Error de formato, edad no valida")
