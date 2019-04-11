# encoding=utf-8

from socket import *
import pickle

chave = []
numeros = []
estrelas = []


def main():

    tcp_s = socket(AF_INET, SOCK_STREAM)
    tcp_s.bind(("127.0.0.1", 0))

    tcp_s.connect(("127.0.0.1", 1247))

    print("Boletim Euromilhões\n 5 Números (1-50)")
    for i in range(5):
        num = int(input(str(i+1) + " número: "), 10)
        while num in numeros or num < 1 or num > 50:
            num = int(input(str(i+1) + " número: "), 10)
        numeros.append(num)
    print("2 Estrelas (1-12)")
    for i in range(2):
        num = int(input(str(i+1) + " estrela: "), 10)
        while num in estrelas or num < 1 or num > 12:
            num = int(input(str(i+1) + " estrela: "), 10)
        estrelas.append(str(num) + "*")

    chave.extend(numeros)
    chave.extend(estrelas)

    print("Aposta inserida com sucesso. Aguarde para saber se ganhou...")
    aposta = pickle.dumps(chave)
    tcp_s.send(aposta)



    b_data = tcp_s.recv(4096)
    str_data = b_data.decode("utf-8")
    print(str_data)

    tcp_s.close()

main()
