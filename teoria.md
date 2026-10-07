# Test Double: MOCK

## 1. Definición

Un **Mock** es un doble de prueba preprogramado con *expectativas*: qué métodos deben llamarse, con qué argumentos y cuántas veces. Si recibe una llamada inesperada, o no recibe una esperada, el test falla. Verifica **comportamiento** (interacciones), no estado.

## 2. Problema que resuelve y cuándo se usa

- **Problema:** algunos efectos del código bajo prueba no dejan rastro en su valor de retorno (enviar un email, cobrar un pago, escribir un log). Un `assert` sobre el resultado no los detecta.
- **Se usa cuando:** lo que importa es *que se llame* a una colaboración (`gateway.cobrar(100)` una sola vez), la dependencia es lenta, no determinista o tiene efectos reales (red, BD, correo), y no hay estado observable que revisar.
- **Cuidado:** acopla el test a la implementación; no abusar si basta verificar estado.

## 3. Comparación

**Clave:** el Mock **verifica comportamiento** (llamadas, argumentos, veces); el Stub **solo devuelve datos**.

| Doble | Qué hace | Qué verifica | Ejemplo (una línea) |
|---|---|---|---|
| **Dummy** | Rellena un parámetro; nunca se usa | Nada | `new Servicio(null, dummyLogger)` |
| **Stub** | Devuelve respuestas enlatadas | Nada (se verifica el estado/resultado del SUT) | `when(repo.buscar(1)).thenReturn(user)` |
| **Fake** | Implementación real simplificada | Nada (se verifica estado) | `repo = new RepoEnMemoria()` |
| **Spy** | Stub que además registra cómo lo llamaron | Llamadas, después de ejecutar (`assert` posterior) | `verify(spy).enviar("hola")` tras la ejecución |
| **Mock** | Preprogramado con expectativas | Llamadas, argumentos y veces; falla si no se cumplen | `verify(gateway, times(1)).cobrar(100)` |

Jerarquía según Fowler: un Mock es un tipo de Spy, un Spy es un Stub, un Stub es un Dummy; el Fake es distinto.

## Fuentes

- Fowler, M. *Mocks Aren't Stubs* / [Test Double](https://martinfowler.com/bliki/TestDouble.html)
- Martin, R. [The Little Mocker](https://blog.cleancoder.com/uncle-bob/2014/05/14/TheLittleMocker.html)
