
def main():
    numero1 = int(input("Introdueix el primer enter: "))
    numero2 = int(input("Introdueix el segon enter: "))
    aux = numero1
    if numero1 < numero2:
        while aux < numero2+1:
            print(aux)
            aux+=1
    else:
        while numero1 > numero2:
            print("***ERROR***")
            numero1 = int(input("Introdueix el primer enter: "))
            numero2 = int(input("Introdueix el segon enter: "))
            aux = numero1
            while aux < numero2+1:
                print(aux)
                aux += 1
if __name__ == '__main__':
    main()
