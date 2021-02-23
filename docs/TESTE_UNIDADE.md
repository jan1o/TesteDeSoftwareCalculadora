## Rodando os testes de unidade
A nossa ordem para executar esta etapa se deu da seguite forma:
- Navegue até a pasta ```tests\``` onde esta o arquivo ```testeUnitario.py``` e ```testeUnitario.py``` e execute o seguinte comando:
```bash
$ python3 -m unittest -v testeUnitario.py
```
A saída deverá ser a seguinte:
```bash
test_areaQuadrado (testeIntegracao.TestCalcAreas) ... ok 
test_areaRetangulo (testeIntegracao.TestCalcAreas) ... ok
test_areaTriangulo (testeIntegracao.TestCalcAreas) ... ok
test_bhaskara (testeIntegracao.TestCalculos) ... ok
test_distEspaco (testeIntegracao.TestDistancia) ... ok
test_distReta (testeIntegracao.TestDistancia) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.023s

```