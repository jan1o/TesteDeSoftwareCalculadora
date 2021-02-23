## Rodando os testes
A nossa ordem para executar esta esta etapa se deu da seguite forma:
- Navegue até a pasta onde estão os arquivos ```testeIntegracao.py``` e ```testeUnitario.py``` e execute o seguinte comando:
```bash
$ python -m unittest -v
```
A saída deverá ser a seguinte:
```bash
$ python3 -m unittest -v

test_areaQuadrado (testeIntegracao.TestCalcAreas) ... ok
test_areaRetangulo (testeIntegracao.TestCalcAreas) ... ok
test_areaTriangulo (testeIntegracao.TestCalcAreas) ... ok
test_bhaskara (testeIntegracao.TestCalculos) ... ok
test_distEspaco (testeIntegracao.TestDistancia) ... ok
test_distReta (testeIntegracao.TestDistancia) ... ok
test_divisao (testeUnitario.TestCalculadora) ... ok
test_multiplicacao (testeUnitario.TestCalculadora) ... ok
test_soma (testeUnitario.TestCalculadora) ... ok
test_subtracao (testeUnitario.TestCalculadora) ... ok
test_deltaCalc (testeUnitario.TestCalculos) ... ok

-----------------------------------------------------------
Ran 11 tests in 0.003s

OK