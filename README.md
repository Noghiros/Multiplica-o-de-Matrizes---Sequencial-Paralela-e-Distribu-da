# Multiplicação de Matrizes - Sequencial, Paralela e Distribuída

Este projeto implementa três abordagens diferentes para multiplicação de matrizes:
- Sequencial
- Paralela (usando multiprocessing)
- Distribuída (usando arquitetura Cliente/Servidor via TCP)

## Estrutura do Projeto

- `client.py`: Implementação do cliente e comparação dos tempos
- `server.py`: Servidor para processamento distribuído
- `matrix_mul.py`: Implementações das multiplicações sequencial e paralela

## Como Executar

1. Inicie o servidor:
```bash
python server.py
```

2. Em outro terminal, execute o cliente:
```bash
python client.py
```

## Resultados

Os resultados das execuções são salvos no arquivo `tempoAlgoritmos.txt`, comparando os tempos de execução das três abordagens para diferentes tamanhos de matriz.
