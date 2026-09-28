OpsTrack API

API do projeto OpsTrack, desenvolvida em Python com Flask.

Pré-requisitos

Antes de começar, tenha instalado:

Python 3.14 ou compatível

Git

PowerShell (Windows)

Configuração do ambiente

Clone o repositório e entre na pasta do projeto:

git clone <URL_DO_REPOSITORIO>
cd OpsTrack_API_CI-CD

1. Criar o ambiente virtual

No Windows:

python -m venv venv


Ative o ambiente virtual:

.\venv\Scripts\Activate.ps1


Se o PowerShell bloquear a execução do script, execute:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


Depois tente novamente:

.\venv\Scripts\Activate.ps1


Quando o ambiente estiver ativo, o terminal deverá mostrar:

(venv) PS C:\...\OpsTrack_API_CI-CD>

2. Instalar as dependências

Para instalar somente as dependências necessárias para executar a API:

pip install -r requirements.txt


Para configurar o ambiente completo de desenvolvimento, incluindo Flake8 e pre-commit:

pip install -r requirements-dev.txt


O arquivo requirements-dev.txt utiliza:

-r requirements.txt
flake8==7.3.0
pre-commit==4.6.2


Assim, um único comando instala as dependências da aplicação e as ferramentas utilizadas durante o desenvolvimento.

Pre-commit e Flake8

O projeto utiliza o pre-commit para executar verificações automaticamente antes de cada commit.

O Flake8 é utilizado para verificar problemas de estilo e possíveis erros no código Python.

A configuração está no arquivo:

.pre-commit-config.yaml

3. Instalar o hook do pre-commit

Depois de instalar as dependências de desenvolvimento, execute:

pre-commit install


Esse comando instala o hook no repositório Git local.

A partir desse momento, ao executar:

git commit


o pre-commit executará o Flake8 nos arquivos modificados.

4. Testar o pre-commit

Para verificar todos os arquivos do projeto manualmente:

pre-commit run --all-files


Se não houver problemas, o resultado esperado será semelhante a:

flake8........................................................Passed


Também é possível verificar diretamente as versões instaladas:

flake8 --version
pre-commit --version

Fluxo de desenvolvimento

Depois de configurar o ambiente, o fluxo normal é:

git status
git add .
git commit -m "tipo: descrição da alteração"


Durante o git commit, o pre-commit executará as verificações configuradas.

Se o Flake8 encontrar algum problema, o commit será interrompido. Corrija os problemas indicados e tente novamente:

git add .
git commit -m "tipo: descrição da alteração"

Executando a API

Com o ambiente virtual ativado, execute a aplicação conforme a configuração do projeto.

Exemplo:

python app.py


Caso o projeto utilize outro ponto de entrada, consulte os arquivos da aplicação para identificar o comando correto.

Estrutura das dependências

O projeto possui dois arquivos de dependências:

requirements.txt
requirements-dev.txt

requirements.txt

Contém somente as dependências necessárias para executar a aplicação.

requirements-dev.txt

Contém as dependências da aplicação e as ferramentas necessárias para desenvolvimento:

Flake8

pre-commit

Isso permite que um ambiente de produção instale somente:

pip install -r requirements.txt


Enquanto um ambiente de desenvolvimento pode instalar tudo com:

pip install -r requirements-dev.txt

Solução de problemas
PowerShell bloqueando o Activate.ps1

Se aparecer uma mensagem informando que a execução de scripts está desabilitada, execute:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


Depois:

.\venv\Scripts\Activate.ps1

O pre-commit não está executando

Verifique se o hook foi instalado:

pre-commit install


Depois teste:

pre-commit run --all-files

Flake8 não encontrado

Certifique-se de que o ambiente virtual está ativo:

(venv)


Depois instale as dependências de desenvolvimento:

pip install -r requirements-dev.txt


E verifique:

flake8 --version

Resumo para novos integrantes

Após clonar o projeto, execute:

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files


Depois disso, o ambiente estará configurado para desenvolvimento e o hook do pre-commit estará ativo na máquina local.
