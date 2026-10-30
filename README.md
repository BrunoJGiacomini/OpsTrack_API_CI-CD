![CI](https://github.com/BrunoJGiacomini/OpsTrack_API_CI-CD/actions/workflows/ci.yml/badge.svg)

# OpsTrack API

API em Python com Flask para servir informações de status, dados de exemplo e endpoints de consulta.

## Visão geral

Este projeto foi estruturado para demonstrar:

- criação de uma API REST com Flask;
- organização de rotas e respostas em JSON;
- uso de testes automatizados com `pytest`;
- validações de qualidade com `flake8` e `pre-commit`;
- configuração de cobertura de testes.

## Tecnologias

- Python 3.10+
- Flask
- Pytest
- pytest-cov
- Flake8
- pre-commit

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

- Python 3
- Git
- PowerShell (no Windows)

## Configuração do ambiente

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd OpsTrack_API_CI-CD
```

Crie e ative o ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a execução do script, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Instalação das dependências

Dependências da aplicação:

```bash
pip install -r requirements.txt
```

Dependências de desenvolvimento (inclui testes e qualidade):

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

A aplicação será iniciada em modo de desenvolvimento e pode ser acessada localmente em:

```text
http://127.0.0.1:5000
```

## Endpoints disponíveis

A API possui os seguintes endpoints:

| Método | Rota | Descrição |
| --- | --- | --- |
| GET | `/` | Retorna serviço e status da API |
| GET | `/route` | Retorna uma mensagem fixa (`Vai Corinthians!`) |
| GET | `/status` | Retorna status geral da aplicação |
| GET | `/version` | Retorna a versão da API |
| GET | `/tickets` | Lista de tickets em formato JSON |
| GET | `/usuarios` | Lista de usuários em formato JSON |
| GET | `/sobre` | Informações gerais da API |

Exemplo de resposta da rota `/`:

```json
{
  "servico": "OpsTrack API",
  "status": "online"
}
```

## Testes automatizados

O projeto utiliza `pytest` para validar as rotas e os retornos esperados da API. A suíte está localizada em `tests/test_api.py` e utiliza uma fixture em `tests/conftest.py` para criar um cliente de teste do Flask.

### Estrutura dos testes

```text
tests/
├── conftest.py
└── test_api.py
```

A fixture `client()` configura o aplicativo em modo de teste e fornece um cliente HTTP para executar requisições simuladas com `app.test_client()`.

### Casos de teste implementados

#### 1. `test_raiz_informa_servico_online`
Valida a rota raiz `/`.

- verifica o código HTTP `200`;
- confirma que a resposta em JSON contém:
  - `servico`: `OpsTrack API`
  - `status`: `online`

#### 2. `test_status_retorna_ok`
Valida a rota `/status`.

- garante que a resposta seja `200`;
- verifica que o payload contém `status == "ok"`.

#### 3. `test_version_retorna_versao`
Valida a rota `/version`.

- confirma que o status da resposta é `200`;
- verifica que a chave `version` existe;
- assegura que o valor retornado corresponde à versão esperada da aplicação.

#### 4. `test_tickets_retorna_lista_com_id_e_titulo`
Valida a rota `/tickets`.

- garante que a resposta tenha status `200`;
- acessa o campo `tickets` do JSON;
- verifica que a lista contém pelo menos um item;
- confirma que cada item possui os campos `id` e `titulo`.

#### 5. `test_usuarios_retorna_dois_usuarios`
Valida a rota `/usuarios`.

- verifica que o endpoint responde com `200`;
- garante que o JSON contém a chave `usuarios`;
- assegura que a lista possui exatamente 2 usuários.

#### 6. `test_rota_inexistente_retorna_404`
Valida o comportamento para rotas inexistentes.

- faz uma requisição para uma URL inválida;
- confirma que o status HTTP retorna `404`;
- garante que o sistema trata rotas não cadastradas corretamente.

#### 7. `test_route_retorna_mensagem_do_time`
Valida a rota `/route`.

- garante que a resposta tenha status `200`;
- verifica que o conteúdo retornado é exatamente a mensagem: `Vai Corinthians!`.

#### 8. `test_sobre_retorna_informacoes_da_api`
Valida a rota `/sobre`.

- confirma que o endpoint responde com `200`;
- verifica que o payload contém os dados gerais da API, como:
  - `name`: `API SCCP`
  - `version`: `1.2.0`
  - `status`: `ok`
  - `environment`: `production`
  - `author`: `Equipe SCCP`

### Execução da suíte

Para rodar todos os testes do projeto:

```bash
pytest
```

A configuração do projeto em `pytest.ini` define:

```ini
[pytest]
pythonpath = .
testpaths = tests
addopts = --cov=app --cov=fail-under=85
```

Isso significa que:

- o diretório de testes é `tests`;
- o módulo principal da aplicação é o arquivo `app.py`;
- a cobertura de testes é medida sobre o código da API;
- a execução falha se a cobertura ficar abaixo de 85%.

### Cobertura e qualidade

Os testes têm como objetivo verificar:

- funcionamento correto das rotas;
- presença dos campos esperados nas respostas;
- status HTTP adequados para sucesso e erro;
- consistência dos dados retornados pela API;
- comportamento de endpoints inexistentes.

### Comando recomendado

```bash
pytest -q
```

Esse comando executa a suíte de forma mais enxuta e facilita a leitura do resultado no terminal.

## Qualidade de código

### Flake8

O projeto utiliza `flake8` para verificar estilo e erros comuns em Python.

```bash
flake8
```

### pre-commit

Para instalar os hooks do Git:

```bash
pre-commit install
```

Para executar todas as verificações manualmente:

```bash
pre-commit run --all-files
```

## Fluxo de desenvolvimento

Um fluxo recomendado para desenvolvimento é:

```bash
git status
git add .
git commit -m "tipo: descrição da alteração"
```

Durante o commit, o `pre-commit` executa as validações configuradas antes de permitir a confirmação do código.

## Solução de problemas

### Script do ambiente virtual bloqueado

No Windows, se a execução do script do ambiente for bloqueada:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Flake8 ou pre-commit não encontrados

Verifique se o ambiente virtual está ativo e as dependências de desenvolvimento foram instaladas:

```bash
pip install -r requirements-dev.txt
```

## Resumo rápido

Após clonar o projeto, o passo inicial é:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pre-commit install
pytest
```

Com isso, o ambiente fica pronto para desenvolvimento, testes e validações automáticas.

## Cobertura de testes

A suíte atual cobre os principais cenários de comportamento da API:

- rota raiz;
- rota de status;
- rota de versão;
- listagem de tickets;
- listagem de usuários;
- rota inexistente com `404`;
- mensagem de rota fixa;
- informações gerais da API.

Esse conjunto garante validação dos retornos principais, da estrutura do JSON e da robustez da aplicação frente a endpoints válidos e inválidos.
