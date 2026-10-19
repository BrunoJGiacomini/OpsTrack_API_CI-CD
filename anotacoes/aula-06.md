Oq eu usei na aula:

antes colar 3 arquivos q o professor disponibilizou na rede

git checkout -b feature/testes
pip install pytest pytest-cov
pytest --version


Rodar o teste:
pytest

Eu vejo o quanto do arquivo eu estou cobrindo/"oq esta certo"
pytest --cov=app --cov-report=term-missing