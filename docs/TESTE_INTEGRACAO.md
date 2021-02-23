## Rodando os testes de integração
A nossa ordem para executar esta etapa se deu da seguite forma:
- Navegue até a pasta ```tests\``` onde esta o arquivo ```testeIntegracao.py``` e ```testeUnitario.py``` e execute o seguinte comando:
```bash
$ python3 -m unittest -v  testeIntegracao.py
```
A saída deverá ser a seguinte:
```bash
test_quadradoBhaskara (testeIntegracao.TestBaseIntegracao) ... ok
test_bhaskara (testeIntegracao.TestCalculos) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```