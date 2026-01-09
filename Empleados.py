
print("ingrese nombre usuario")
nombre= input()
print("ingrese edad")
edad= int(input())
print("ingrese rol")
rol= input()
if edad>18 and rol=="estudiante" or rol=="docente":
    print("acceso permitido")
elif   edad<18:
    print("acceso denegado")
elif rol!= "estudiante" or rol!= "docente" or rol!= "otro":
    print("revisar rol")
else:
    print("verifique los datos")