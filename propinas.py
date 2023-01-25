print("Bienvenido a la calculadora de personas")

total_de_la_cuenta= input("Cual es el resultado de la cuenta total ?\n")

personas = input("numero de personas de la cuenta a dividir si no se dividira escribir 1\n") 

propina = input("escriba el porcentaje de propina por favor\n") 

resultado_porcentaje=(float(total_de_la_cuenta)*float(propina)/100)


resultado_sinPorcentaje=float(total_de_la_cuenta)+ float(resultado_porcentaje)



resultado=float(resultado_sinPorcentaje)/float(personas)

print("cada persona deberia pagar ")
print(resultado)


#[02:29 p. m.] Viveros, Irving
#Input de costo totalInput de personas en la mesaInput de propina a pagar 

#[02:29 p. m.] Viveros, Irving
#Output:

#[02:30 p. m.] Viveros, Irving
#La total de propina que se va a pagarLa cantidad que le corresponde a cada persona en la mesa a pagar

