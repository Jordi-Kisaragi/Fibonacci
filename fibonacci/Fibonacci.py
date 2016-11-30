'''
Created on 23 nov. 2016

@author: usuario
'''
def fibonacci(numero1):
    if numero1==1:
        return 1
    if numero1==0:
        return 0
    else:
        return fibonacci(numero1-1)+fibonacci(numero1-2)
    if __name__ =="__main__":
        numero1=int(input("Introduce un número:"))
        print(numero1)