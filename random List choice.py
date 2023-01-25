import random
 


#partners=['Fernanda' ,'Melisa del Carmen','José','Miriam Janet','Natalia','Tamara','Jasive ','Gabriel',
#'Jonathan Palacios (Emmanuel)','Kenia','Rodrigo','Luis','Yamil','Cinthia Melisa','Miguel']
file=open("Lista_20_Enero.txt")
partners=file.read()
partners=partners.split("\n")


limit=len(partners)-1

random_choice=int(random.randint(0,limit))


print(partners[random_choice])