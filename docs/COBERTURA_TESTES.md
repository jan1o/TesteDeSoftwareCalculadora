# Cobertura de testes

Para realizar os teste de cobertura, bem como os seus relatórios, foi usado o pacote [Coverage](https://pypi.org/project/coverage/) versão 5.4 (neste exemplo), pacote built-in do python, unido ao [Unittest](https://docs.python.org/3/library/unittest.html).

## Instalando as ferramentas
Para instalar o Unittest:  
```bash
$ pip install unittest
```
Para instalar o Coverage (caso não apareça na sua instalação).
```bash
$ pip install coverage
```
Ou volte para a raiz do projeto e execute o comando:
```bash
$ pip install -r requirements.txt
```
Com esse comando todos pacotes gerados durante a construção desse exemplo serão instalados.  

## Verificando a cobertura dos testes

No métido tradicional, executa-se um ```python -m unittest -v``` ou  ```python3 -m unittest -v``` (caso tenha duas versões do python na máquina/ambiente).  

Usando o ```Coverage```, para que possamos medir a nossa cobertura de código, usa-se o comando:
```bash
$ coverage run -m unittest discover
```
após isso, para checar os resultados gerados, execute:
```bash
$ coverage report --omit=main.py
```
Obs.: usamos a flag ```--omit=main.py``` pois o arquivo main.py é onde está concentrado todas as funções que testamos, a fim de de diminuir a complexidade com imports e etc.  

Para visualizar e/compartilhar os resultados obtidos, execute:
```bash
$ coverage html
```
Esse comando gera em uma pasta arquivos html js e etc para serem visualizados no navegador.