def primo():
    a=input("Dime un numero: ")
    primo=True
    for i in range(2,a):
        if (a%i==0):
            primo=False
    if  (primo==True):
        print "Es primo"
    else:
        print "No es primo"

         
primo()
