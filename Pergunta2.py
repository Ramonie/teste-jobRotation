numero = int(input("Digite um número: "))

fibonacci_anterior = 0
fibonacci_atual = 1
pertence_sequencia = False

while fibonacci_atual <= numero:
    if fibonacci_atual == numero:
        pertence_sequencia = True
        break
    fibonacci_proximo = fibonacci_anterior + fibonacci_atual
    fibonacci_anterior = fibonacci_atual
    fibonacci_atual = fibonacci_proximo

if pertence_sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
