import random

def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    
    # Gere os dígitos verificadores
    for i in range(2):
        soma = 0
        for j in range(9 + i):
            soma += cpf[j] * (10 + i - j)
        cpf.append((soma * 10) % 11 % 10)
    
    return ''.join(map(str, cpf))

if __name__ == '__main__':
    cpf = gerar_cpf()
    print("CPF Gerado:", cpf)
