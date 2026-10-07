# cs5383-mock

> Tarea del curso **CS5383 – Verificación y Pruebas de Software** · UTEC

Material sobre el **Test Double Mock**: un doble de prueba con expectativas que verifica *comportamiento* (qué métodos se llaman, con qué argumentos y cuántas veces) en lugar de estado.

## Contenido

| Archivo | Descripción |
|---|---|
| [`teoria.md`](teoria.md) | Definición, problema que resuelve, cuándo se usa y comparación con Stub, Fake, Spy y Dummy |
| [`ejemplos.md`](ejemplos.md) | Ejemplo cotidiano (restaurante) y ejemplo práctico en software (`OrderService` + `EmailService`) |
| [`demo_mock.py`](demo_mock.py) | Demo ejecutable con `unittest.mock`: dos tests que pasan y uno que falla a propósito |
| [`slides.html`](slides.html) | Presentación (variantes: [`A`](slides_A.html), [`B`](slides_B.html), [`C`](slides_C.html)) |

## Ejecutar la demo

Requiere Python 3.8+ (solo biblioteca estándar, sin dependencias).

```bash
python demo_mock.py
```

Resultado esperado: 2 tests `ok` y 1 `FAIL` (`test_falla_a_proposito` espera 2 envíos y hubo 1, lo que muestra cómo el Mock detecta una interacción incorrecta).

## Idea clave

```python
email = Mock()
service = OrderService(email)

service.place("ana@x.com", 50)

email.send.assert_called_once_with("ana@x.com", "Pedido de 50 confirmado")
```

El test no revisa un valor de retorno: comprueba que la colaboración con `EmailService` ocurrió exactamente una vez y con los datos correctos, sin enviar correos reales.
