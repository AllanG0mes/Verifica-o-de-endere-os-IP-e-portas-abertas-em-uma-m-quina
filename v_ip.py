#Verificação de endereços IP e portas abertas em uma máquina:

import socket

def verificar_porta(ip, porta):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = sock.connect_ex((ip, porta))
        if resultado == 0:
            print(f"A porta {porta} está aberta no IP {ip}.")
        else:
            print(f"A porta {porta} está fechada no IP {ip}.")
        sock.close()
    except socket.error:
        print(f"Erro ao conectar ao IP {ip} na porta {porta}.")

# Exemplo de uso:
endereco_ip = "127.0.0.1"
porta_alvo = 80
verificar_porta(endereco_ip, porta_alvo)
