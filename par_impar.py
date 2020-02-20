class Impar:
    def num(self):
        num = input("Agregue un número: ")
        
        num = int(num)
        if num == 0:
            print ("Es par.")
        elif num%2 == 0:
            print ("Es par")
        else:
            print ("Es impar")

   
par=Impar()
par.num()
