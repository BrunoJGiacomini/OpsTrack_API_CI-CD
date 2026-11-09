![CI](https://github.com/BrunoJGiacomini/OpsTrack_API_CI-CD/actions/workflows/ci.yml/badge.svg)

# OpsTrack API

API REST desenvolvida em Python com Flask para disponibilizar informações de status, dados de exemplo e endpoints de consulta.

## Visão geral

Este projeto foi estruturado para demonstrar:

- Criação de uma API REST com Flask;
- Organização de rotas e respostas em JSON;
- Implementação de testes automatizados com pytest;
- Validações de qualidade de código com flake8 e pre-commit;
- Configuração e análise de cobertura de testes.

## Tecnologias utilizadas

- Python 3.10+
- Flask
- Pytest
- Pytest-cov
- Flake8
- Pre-commit
- Docker

## Estrutura do projeto

```text
OpsTrack_API_CI-CD/
├── app.py
├── README.md
├── LEIA-ME.txt
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── .flake8
├── .pre-commit-config.yaml
├── tests/
│   ├── conftest.py
│   └── test_api.py
├── anotacoes/
│   └── materiais de aula
└── venv/
```

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3;
- Git;
- PowerShell (Windows);
- Docker (opcional, para execução em containers).

## Configuração do ambiente

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd OpsTrack_API_CI-CD
```

### 2. Crie e ative o ambiente virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a execução do script, utilize:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Instale as dependências

**Dependências da aplicação:**

```bash
pip install -r requirements.txt
```

**Dependências de desenvolvimento:**

```bash
pip install -r requirements-dev.txt
```

O arquivo `requirements-dev.txt` inclui:

```text
-r requirements.txt
flake8==7.3.0
pre-commit==4.6.2
pytest==9.1.1
pytest-cov==7.1.0
```

## Executando a API

Com o ambiente virtual ativado, inicie a aplicação:

```bash
python app.py
```

A aplicação será iniciada em modo de desenvolvimento e poderá ser acessada em:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Rodando com Docker

A aplicação também pode ser executada em um container Docker.

### 1. Build da imagem

```bash
docker build -t opstrack:latest .
```

### 2. Execute o container

```bash
docker run -d --rm -p 8000:8000 --name opstrack-api opstrack:latest
```

A API ficará disponível em:

[http://localhost:8000/status](http://localhost:8000/status)

### 3. Parar o container

```bash
docker stop opstrack-api
```

### Exemplo de resposta — `/status`

```json
{
    "status": "ok"
}
```

## Endpoints disponíveis

A API disponibiliza os seguintes endpoints:

| Método | Rota | Descrição |
|:---:|---|---|
| GET | `/` | Retorna o nome do serviço e o status da API. |
| GET | `/route` | Retorna uma mensagem fixa: "Vai Corinthians!". |
| GET | `/status` | Retorna o status geral da aplicação. |
| GET | `/version` | Retorna a versão da API. |
| GET | `/tickets` | Retorna uma lista de tickets em formato JSON. |
| GET | `/usuarios` | Retorna uma lista de usuários em formato JSON. |
| GET | `/sobre` | Retorna informações gerais sobre a API. |

### Exemplos de respostas

**Rota `/`**

```json
{
    "servico": "OpsTrack API",
    "status": "online"
}
```

**Rota `/status`**

```json
{
    "status": "ok"
}
```

## Testes automatizados

O projeto utiliza **pytest** para validar as rotas e os retornos esperados da API.

A suíte de testes está localizada no diretório `tests/` e utiliza uma fixture definida em `conftest.py` para criar um cliente de testes do Flask.

### Estrutura dos testes

```text
tests/
├── conftest.py
└── test_api.py
```

A fixture `client()` configura a aplicação em modo de teste e disponibiliza um cliente HTTP para executar requisições simuladas por meio de:

```python
app.test_client()
```

### Casos de teste implementados

| Teste | Descrição |
|---|---|
| `test_raiz_informa_servico_online` | Valida a rota `/`, o status HTTP 200 e os campos `servico` e `status`. |
| `test_status_retorna_ok` | Verifica se `/status` retorna HTTP 200 e `status == "ok"`. |
| `test_version_retorna_versao` | Confirma a existência da chave `version` e o valor esperado. |
| `test_tickets_retorna_lista_com_id_e_titulo` | Verifica se `/tickets` retorna uma lista com pelo menos um item e se cada ticket possui `id` e `titulo`. |
| `test_usuarios_retorna_dois_usuarios` | Confirma se `/usuarios` retorna exatamente dois usuários. |
| `test_rota_inexistente_retorna_404` | Verifica se uma rota não cadastrada retorna HTTP 404. |
| `test_route_retorna_mensagem_do_time` | Confirma se `/route` retorna exatamente a mensagem "Vai Corinthians!". |
| `test_sobre_retorna_informacoes_da_api` | Valida as informações gerais retornadas pela rota `/sobre`. |

### Execução da suíte de testes

Para executar todos os testes:

```bash
pytest
```

Para uma saída mais enxuta no terminal:

```bash
pytest -q
```

### Configuração do pytest

O arquivo `pytest.ini` possui a seguinte configuração:

```ini
[pytest]
pythonpath = .
testpaths = tests
addopts = --cov=app --cov-fail-under=85
```

Essa configuração define:

- `pythonpath = .`: adiciona o diretório raiz ao caminho de importação;
- `testpaths = tests`: indica onde estão localizados os testes;
- `--cov=app`: mede a cobertura de testes do módulo `app`;
- `--cov-fail-under=85`: faz a execução falhar caso a cobertura fique abaixo de 85%.

## Cobertura de testes

A suíte atual contempla os principais cenários de comportamento da API:

- Rota raiz;
- Rota de status;
- Rota de versão;
- Listagem de tickets;
- Listagem de usuários;
- Tratamento de rotas inexistentes (HTTP 404);
- Retorno de mensagem fixa;
- Informações gerais da API.

O objetivo é verificar o funcionamento das rotas, a estrutura dos dados retornados, os códigos HTTP e a consistência das respostas.

## Qualidade de código

### Flake8

O projeto utiliza Flake8 para verificar padrões de estilo e identificar possíveis problemas no código Python.

Para executar a análise:

```bash
flake8
```

### Pre-commit

O Pre-commit automatiza a execução de verificações antes de cada commit.

Para instalar os hooks do Git:

```bash
pre-commit install
```

Para executar todas as verificações manualmente:

```bash
pre-commit run --all-files
```

## Fluxo de desenvolvimento

Um fluxo recomendado para trabalhar no projeto é:

```bash
git status
git add .
git commit -m "tipo: descrição da alteração"
```

Durante o commit, o Pre-commit executa as validações configuradas antes de permitir a confirmação das alterações.

## Solução de problemas

### Script do ambiente virtual bloqueado

Caso o PowerShell impeça a ativação do ambiente virtual:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Flake8 ou Pre-commit não encontrados

Verifique se o ambiente virtual está ativado e instale as dependências de desenvolvimento:

```bash
pip install -r requirements-dev.txt
```

## Resumo rápido

Após clonar o repositório, execute os seguintes comandos:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pre-commit install
pytest
```

Com isso, o ambiente estará preparado para desenvolvimento, execução de testes automatizados e validações de qualidade de código.

---

**OpsTrack API** — Projeto desenvolvido para demonstrar conceitos de desenvolvimento de APIs REST, testes automatizados, qualidade de código e integração com ferramentas de CI/CD.

