# Atividade de Código distribuído
# Aluno: Stefano Calheiros Stringhini R.A.: 2312123

import socket
import pickle
import numpy as np
import struct
from matrix_mul import sequential_matrix_multiply, parallel_matrix_multiply

HOST = '127.0.0.1'
PORT = 5000

def send_data(sock, data):
    # Envia o tamanho dos dados
    sock.sendall(struct.pack('>I', len(data)))
    # Envia os dados
    sock.sendall(data)

def receive_data(sock):
    # Recebe o tamanho dos dados
    raw_msglen = sock.recv(4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    
    # Recebe os dados
    data = b""
    while len(data) < msglen:
        packet = sock.recv(min(msglen - len(data), 4096))
        if not packet:
            return None
        data += packet
    return data

# MATRIZES ALEATÓRIAS
N = 300  
A = np.random.randint(0, 10, (N, N))
B = np.random.randint(0, 10, (N, N))

if __name__ == "__main__":
    print("Iniciando testes...")
    
    # SEQUENCIAL
    print("Executando multiplicação sequencial...")
    _, seq_time = sequential_matrix_multiply(A, B)

    # PARALELO
    print("Executando multiplicação paralela...")
    _, par_time = parallel_matrix_multiply(A, B)

    print("Executando multiplicação distribuída...")
    # DISTRIBUÍDO VIA TCP
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            
            # Envia as matrizes
            data = pickle.dumps((A, B))
            send_data(s, data)
            
            # Recebe o resultado
            result_data = receive_data(s)
            if result_data is None:
                raise Exception("Conexão perdida")
                
            C, dist_time = pickle.loads(result_data)
            
        # ARQUIVO DE TEMPO
        with open("tempoAlgoritmos.txt", "a") as file:
            file.write("\n" + "-"*24 + "\\" + "-"*24 + "\n")
            file.write("Tamanhos das matrizes: {}x{}\n".format(N, N))
            file.write(f"Tempo Sequencial: {seq_time:.2f} ms\n")
            file.write(f"Tempo Paralelo: {par_time:.2f} ms\n")
            file.write(f"Tempo Distribuído: {dist_time:.2f} ms\n")

        print("\nResultados:")
        print(f"Tempo Sequencial: {seq_time:.2f} ms")
        print(f"Tempo Paralelo: {par_time:.2f} ms")
        print(f"Tempo Distribuído: {dist_time:.2f} ms")
        print("\nResultados salvos em tempoAlgoritmos.txt ✅")
        
    except Exception as e:
        print(f"Erro na execução distribuída: {e}")
