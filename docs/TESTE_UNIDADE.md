## Rodando os testes de unidade
A nossa ordem para executar esta etapa se deu da seguite forma:
- Navegue até a pasta ```tests\``` onde esta o arquivo ```testeUnitario.py``` e ```testeUnitario.py``` e execute o seguinte comando:
```bash
$ python3 -m unittest -v testeUnitario.py
```
A saída deverá ser a seguinte:
```bash
test_areaQuadrado (testeUnitario.TestCalcAreas) ... ok
test_areaRetangulo (testeUnitario.TestCalcAreas) ... ok
test_areaTriangulo (testeUnitario.TestCalcAreas) ... ok
test_divisao (testeUnitario.TestCalculadora) ... ok
test_multiplicacao (testeUnitario.TestCalculadora) ... ok
test_soma (testeUnitario.TestCalculadora) ... ok
test_subtracao (testeUnitario.TestCalculadora) ... ok
test_bhaskara (testeUnitario.TestCalculos) ... ok
test_deltaCalc (testeUnitario.TestCalculos) ... ok
test_distEspaco (testeUnitario.TestDistancia) ... ok
test_distReta (testeUnitario.TestDistancia) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.002s

OK
```