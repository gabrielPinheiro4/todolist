# Case Técnico - Desenvolvedor(a) de Software

## ToDoList
Projeto ToDoList para processo seletivo da AvanteTech.

>**Não foi possível colocar o projeto em produção**


## Ferramentas utilizadas
- Flask
- VueJS
- PostgreSQL

### Bibliotecas usadas em VueJS
- PrimeVue(componentes) e Tailwind
- VueRouter
- Axios
- Pinia
- Cookie-JS

### Bibliotecas usadas em Flask
- SqlAlchemy
- Flask-Cors
- Bcrypt
- Flask-jwt-extended

## Funcionalidades
- Criar Projeto e Tarefa
- Editar Projeto e Tarefa
- Deletar Projeto e Tarefa
- Cadastrar Usuário e fazer Login


## Modelagem
<img src="./imgs_readme/modelagem.png"/>

## Como executar o projeto

#### Ferramentas necessárias:
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [npm](https://nodejs.org/en/download)

### 1. Configure o Postgres ou qualquer DB de sua preferência.
Configure seu Banco de dados. Crie exatamente as mesmas tabelas que aparecem
na modelagem.

> **Aviso**: o projeto necessita que as tabelas Status e Prioridades já estejam
populadas.

### 2. Adicionar .env no backend
Dentro da pasta backend, adicione um arquivo .env com os seguintes valores:

```
SQLALCHEMY_DATABASE_URI = <nome_sgbd>://<usuario>:<senha>@<endereco>:<porta>/<nome_do_banco>

Exemplo:
SQLALCHEMY_DATABASE_URI = postgresql://postgres:admin@localhost:5432/todolist

SECRET_KEY = <caracteres_aleatórios>

JWT_SECRET_KEY = <caracteres_aleatórios>

JWT_TOKEN_LOCATION = cookies

```

Digite o seguinte código no terminal para gerar uma combinação aleatória de 
caracteres

```shell
$ python3 -c 'import secrets; print(secrets.token_hex())'
```

### 3. Adicionar .env no frontend
Dentro da pasta frontend, adicione um arquivo .env com os seguintes valores:

```
VITE_API_URL=<endereco_da_aplicação_python>
```

### 4. Instale as dependencias do frontend.
Dentro da pasta frontend digite o seguinte comando:

```shell
$ npm i
```

### 5. Instale as dependencias do backend.
Dentro da pasta frontend digite o seguinte comando:

```shell
$ pipenv install
```

### 6. Executar backend
Após feita a instalação das dependências, abra o ambiente virtual python e execute
o aquivo `main.py`.

```shell
$ pipenv shell
$ python main.py
```

### 7. Executar frontend
Após feita a instalação das dependências, execute o comando abaixo para executar
o projeto em modo de desenvolvimento.

```shell
$ npm run dev -- --host
```

> **Aviso**: Antes de executar o projeto, certifique-se de que seu banco de dados
está devidamente configurado.


## Decisões tomadas
- Uma tarefa deve pertencer à um, e somente um, projeto.
- Ao deletar um projeto, todas as suas tarefas vinculadas tabém serão deletadas.
- Um projeto está vinculado à um único usuário.
- Um usuário não pode ter mais de um projeto com o mesmo nome.


## Dificuldades enfrentadas
A minha principal dificuldade foi gerenciar o tempo disponível para
fazer o projeto. Eu tive que retirar diversas idéias do projeto por conta da
falta de tempo.

## Possíveis melhorias
Além da melhoria na estrutura do código, pretendo adicionar as funcionalidades
que não puderam ser implementadas. Como a filtragem de tarefas por status e prioridade. 
