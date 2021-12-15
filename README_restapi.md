# Projeto 02 CRUD

# 💡Descrição do projeto
Este programa faz parte do segundo desafio de REST APIs da trilha de IA da Kumulus. Tem como objetivo criar uma API com os métodos CRUD para iterar com um objeto definido como "produto", "descrição" e "preço" e armazenar em um banco de dados.

# 📋Pré-requisitos
Softawares e pacotes necessários:

 - Python <= 3.8 (software)
 - Flask (pacote python)
 - jsonschema (pacote python)
 - pymongo (pacote python)
 - Insomnia (software)


# 🔧Instalação

Instalação do python: 
    - Acessar o link: https://www.python.org/downloads/
    - Baixar a versão mais recente
    - Pode escolher uma IDE a seu critério (Pycharm, VSCode, etc...)
    - Instalar o pip para instalar os pacotes que serão usados (https://pypi.org/project/pip/)

Instalação dos pacotes python:
    - `pip install flask`
    - `pip install jsonschema`
    - `pip install pymongo`

Instalação do insomnia:
    - Acessar o link: https://insomnia.rest/download
    - Seguir o passo a passo da instalação


# ⚙️Execução
1) Rode o arquivo python `projeto-02-crud.py`
    - Ele vai gerar um link que será necessário para colar no Insomnia ex: `Running on http://127.0.0.1:10/ (Press CTRL+C to quit)`

2) Deixe rodando o programa, abra o Insomnia e cole o link na barra http

*OBS: O programa tem as seguintes propriedades possíveis: POST(inserir), GET(retornar), PUT(atualizar) e DELETE(deletar), vamos utilizar o POST como exemplo mas todos seguem o mesmo padrão*

3) No link colado na barra do Insomnia você deve inserir o diretório `products`, deve ficar assim: `http://127.0.0.1:10/products`

4) Selecionar o método POST ao lado da barra

5) Clique em `Body` e selecione a opção `JSON`

6) O objeto que você vai inserir deve seguir o seguinte schema: 
`{"product": "nome_do_produto",
"description": "definição_do_produto",
"price": 999}`

7) Clique em `Send` e ele vai retornar o ObjectId criado e vai armazenar no banco de dados do MongoDB
 

# 📊Resultados
A API foi criada com sucesso utilizando Orientação a Objetos e manipulação de JSON conectado ao banco de dados

# 💻Tecnologias utilizadas
Python: https://www.python.org/about/
Insomnia: https://insomnia.rest/
MongoDB: https://www.mongodb.com/

# 📅Status do Projeto: :heavy_check_mark:Concluído e Entregue (Termo de Aceite assinado).

# ✒️Autores
WilliamSMendes - Desenvolvedor