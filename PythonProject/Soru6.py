#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

#Hipotenüs Formülü: a^2 + b^2 = c^2

a = int(input("a:"))

b = int(input("b:"))

c =  (a ** 2 + b ** 2) ** 0.5

print("Hipotenüs: ",c)