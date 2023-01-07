# Python
# Versão utilizada: Python 3.8.10
# Data: 07/01/2023
# Autor: Lucas Amarante - lucas.amarante42@gmail.com

## Como rodar os testes

No terminal, execute os comandos:

```bash
cd python
python3 -m unittest RDChallengeTest.py
```

## Funções:
# customer_success_balancing
Algoritmo principal que retorna o css com maior número de clientes.

Etapas:
-verificações das premissas;
-filtragem do array customer_success sem os id's de abstenções;
-ordenação do array pelo campo 'score';
-iteração do novo array sorted_customer_success;
-iteração da cópia do array de customers;
-verificação do 'score' do cliente em relação ao 'score' do css de acordo com o indíce 0 ou > pois quando for > é verificado o range do 'score' anterior com o atual, é feito a remoção do customer já utilizado no css (objetivo na performance do loop) e a contagem de customer do css;
-adição do contador de customer ao css;
-verificação do maior contador de customer e se existe empate;

# build_scores
Criação da lista de objetos de 'id' e 'score'

# sum_customer_and_remove_used_object_from_list
Contador de customer e remoção do customer já utilizado pelo css

# create_list_norepeated_by_field
Criação de lista com elementos não repetidos