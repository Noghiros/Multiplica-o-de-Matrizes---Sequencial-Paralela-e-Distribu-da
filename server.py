# Atividade de Código distribuído
# Aluno: Stefano Calheiros Stringhini R.A.: 2312123

import socket
import pickle
import time
import numpy as np
import struct

HOST = "127.0.0.1"
PORT = 5000

def receive_data(conn):
    # Recebe o tamanho dos dados
    raw_msglen = conn.recv(4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    
    # Recebe os dados
    data = b""
    while len(data) < msglen:
        packet = conn.recv(min(msglen - len(data), 4096))
        if not packet:
            return None
        data += packet
    return data

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Servidor aguardando conexão...")

while True:
    conn, addr = server.accept()
    print(f"Conectado por {addr}")

    try:
        # Recebe os dados
        data = receive_data(conn)
        if data is None:
            continue
            
        # Desserializa matrizes
        A, B = pickle.loads(data)
        
        # Multiplica as matrizes
        start_time = time.time()
        result = np.dot(A, B)
        end_time = time.time()
        
        dist_time = (end_time - start_time) * 1000
        
        # Prepara resposta
        response = pickle.dumps((result, dist_time))
        
        conn.sendall(struct.pack('>I', len(response)))
        conn.sendall(response)
        
        print("Cálculo concluído e enviado ao cliente.")
    
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()
