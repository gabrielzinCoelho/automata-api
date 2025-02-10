# Automata API

Esta API fornece funcionalidades para criar, recuperar, atualizar, validar e salvar uma representação gráfica de autômatos finitos determinísticos (DFA), Autômatos com Pilha Não Determinísticos (NPDA) e Máquinas de Turing Determinísticas (DMT).

## Configuração e Execução

### Passos para configuração

1. Clone o repositório:
   ```sh
   git clone https://github.com/gabrielzinCoelho/automata-api
   cd automata-api
   ```

2. Crie um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Execute o servidor FastAPI:
   ```sh
   fastapi dev src/main.py
   ```

5. Acesse a documentação interativa da API em:
   - [Swagger UI](http://127.0.0.1:8000/docs)

## Sobre o projeto

A arquitetura do projeto foi estruturada de forma a garantir uma organização clara e eficiente no tratamento das requisições e na gestão dos automatos. 

Foram utilizados controllers para tratar e validar as requisições HTTP, cada um responsável por uma funcionalidade específica da aplicação, como criação, atualização, obtenção e validação de autômatos. 

A lógica de negócios foi implementada em services, que interagem com os dados por meio de repositórios, os quais armazenam as informações na memória principal.

Os dados são representados por models, que definem as entidades da aplicação, garantindo uma estrutura clara e consistente para o armazenamento e manipulação das informações

## Funcionalidades

* Autômatos Finitos Determinísticos (DFA):  
  * Permitir a criação, manipulação e visualização de DFA's, com suporte para grandes entradas.
  * Salvar uma representação gráfica de DFA.
  * Validar strings

* Autômatos com Pilha: 
  * Criar e visualizar autômatos que utilizam pilha, possibilitando operações mais complexas.
  * Salvar uma representação gráfica de NPDA.
  * Validar strings

* Máquinas de Turing: 
  * Fornecer suporte para criar e representar graficamente máquinas de Turing, explorando sua capacidade de resolver problemas computacionais gerais.
  * Validar strings

## Testes

Para testar os endpoints da API e validar a funcionalidade das operações com os autômatos, foram utilizados casos de teste teóricos, baseados em entradas de exemplo. 

A ferramenta Insomnia foi empregada para realizar as requisições e simular testes de ponta a ponta (E2E), permitindo verificar se os endpoints estão respondendo corretamente às operações, como criação, atualização e verificação de aceitação de strings. 

Com o Insomnia, foi possível simular diferentes cenários de uso, garantindo que os autômatos funcionassem conforme o esperado em situações reais e atendendo às condições estabelecidas pelos modelos teóricos. Isso assegura que a implementação esteja correta e que a API seja robusta para lidar com os diversos casos previstos.

## Limitações

Neste projeto, foram construídos apenas os endpoints para as máquinas de maior poder computacional para cada um dos casos abordados. Ou seja, os endpoints estão implementados para o modelo de Máquina de Turing Determinística, o Autômato de Pilha Não Determinístico e o Autômato Finito Determinístico (DFA), que são os modelos mais complexos e com maior capacidade de processamento entre os tipos de autômatos considerados. 

Isso implica que, para modelos de menor poder computacional ou outras variantes de autômatos, como os autômatos finitos não determinísticos ou os autômatos de pilha determinísticos, não há endpoints implementados no momento. Portanto, a abordagem adotada foca nas estruturas de autômatos mais avançadas para possibilitar a construção de funcionalidades mais robustas e performáticas.

## Exemplos de Uso

### Obter DFA por ID

**Requisição:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/dfa/435dd07d-2374-4e47-814f-de1b1d2abc33'
```

**Resposta:**
```json
{
  "id": "435dd07d-2374-4e47-814f-de1b1d2abc33",
  "inputParameters": {
    "states": ["q2", "q0", "q1"],
    "input_symbols": ["1", "0"],
    "transitions": {
      "q0": {"0": "q1", "1": "q2"},
      "q1": {"0": "q2", "1": "q1"},
      "q2": {"0": "q1", "1": "q2"}
    },
    "initial_state": "q0",
    "final_states": ["q2"],
    "allow_partial": false
  }
}
```

### Verificar se o DFA aceita uma string

**Requisição:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/dfa/435dd07d-2374-4e47-814f-de1b1d2abc33/accept/0000001111111'
```

**Resposta:**
```json
{
  "string": "0000001111111",
  "isValid": false
}
```

### Listar todos os DTMs

**Endpoint:** `GET /dtm`

**Descrição:** Retorna uma lista de todos os DTMs armazenados.

**Exemplo de resposta:**
```json
[
    {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "inputParameters": {
            "states": ["q0", "q1", "q2"],
            "input_symbols": ["0", "1"],
            "tape_symbols": ["0", "1", "_"],
            "transitions": {
                "q0": {"0": ["q1", "1", "R"]},
                "q1": {"1": ["q2", "0", "L"]}
            },
            "initial_state": "q0",
            "blank_symbol": "_",
            "final_states": ["q2"]
        }
    }
]
```

---

### Verificar se o DTM aceita uma string

**Endpoint:** `GET /dtm/{id}/accept/{string}`

**Descrição:** Verifica se o DTM com o ID fornecido aceita a string de entrada.

**Exemplo de requisição:**
```
GET /dtm/123e4567-e89b-12d3-a456-426614174000/accept/01
```

**Exemplo de resposta:**
```json
{
    "string": "01",
    "isValid": true
}
```

### Salvar imagem do NPDA

**Endpoint:** `POST /npda/{id}/image`

**Descrição:** Gera e salva uma imagem do NPDA identificado pelo ID.

**Exemplo de requisição:**
```
POST http://127.0.0.1:8000/npda/3af1cda7-75f4-4c83-9d6c-d07c6c28c90d/image
```

**Exemplo de resposta:**
```json
{
  "success": "Image saved with success in images/2754c2ce-fead-4f65-b9b3-8b983a80d660.png"
}
```
