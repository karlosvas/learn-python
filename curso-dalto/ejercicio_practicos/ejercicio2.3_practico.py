#Sucesión de Fibonacci a mi manera
def fibonacci(num):
    resultado = [1]
    for i in range(num):
        num_actual = resultado[i]
        num_anterior = resultado[i-1]
        resultado.append(num_actual + num_anterior)
           
    return resultado

print(fibonacci(20))
