def total_sum(arr):
    total = 0
    for val in arr:
        total += val

    return total

def avg(arr):
    total = total_sum(arr)
    return total / len(arr)

def val_sort(arr):
    positive = 0
    negative = 0
    zero = 0
    for val in arr:
        if val > 0:
            positive += 1
        if val < 0:
            negative += 1
        else:
            zero += 1
    return positive, negative, zero

def three_mult(arr):
    total = 0
    for i in arr:
        if i % 3 == 0:
            total += 1
    return total

def area_rectangle(a, b):
    return a*b

def perimeter_rectangle(a, b):
    return 2*a+2*b

def prime(val):
    for i in range(round(val/2, 0)):
        if val % i == 0:
            return False
        else:
            return True

def safe_zone(arr):
    total = 0
    for i in arr:
        if i >= 85:
            total += 1
    return total

def risk_zone(arr):
    total = 0
    for i in arr:
        if i <60:
            total += 1
    return total

def max_min(arr):
    maxi = arr[0]
    mini = arr[0]
    for i in arr:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    return maxi, mini

def frecuence(arr):
    repetidos = []
    for i in arr:
        if arr.count(i) > 1 and i not in repetidos:
            repetidos.append(i)
    return len(repetidos)

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b == 0:
        return 0
    else:
        return a/b

while True:
    print("\n--------------------Menú de opciones--------------------\n1. Suma, promedio, contador de positivos/negativos/ceros y filtrador de múltiplos de 3 en una serie numérica\n 2. Área y perímetro de un rectángulo\n3. Verificador de números primos\n4. Promedio de calificaciones y contador de buenas notas/malas notas\n5. Calculador de numero máximo, mínimo y repetición de una serie numérica\n6. Calculadora básica\n7. Salir")
    option = input("Seleccione una opción: ")
    match option:
        case "1":
            while True:
                try:
                    cant1 = int(input("\nIngrese la cantidad de valores a ingresar: "))
                    if cant1 <= 0:
                        print("La cantidad debe ser positiva")
                    elif cant1 >=1:
                        break
                except:
                    print("Debe ingresar un número entero")

                arr1 = []

                for i in range(cant1):
                    while True:
                        try:
                            val = int(input(f"Ingrese el valor {i+1}: "))
                            arr1.append(val)
                        except:
                            print("Debe ingresar un valor entero")

                total1 = total_sum(arr1)
                average1 = avg(arr1)
                positive, negative, zero = val_sort(arr1)
                mult1 = three_mult(arr1)
                print(f"La suma total de los valores es de {total1}\nEl promedio de los valores es de {average1}\nIngresó {positive} números positivos, {negative} números negativos y {zero} ceros\nIngresó {mult1} múltiplos de 3")



        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case _:
            print("Opción inválida, Intente nuevamente")


