# Mock: ejemplos

## 4. Ejemplo cotidiano

En un restaurante, el mesero toma tu pedido y debe pasarlo a cocina. No nos interesa cocinar de verdad: solo comprobar que el mesero entregó la comanda a cocina **exactamente una vez** y con el pedido correcto (si la entrega dos veces, se prepara doble; si ninguna, nunca llega tu comida). La "cocina" es un actor de utilería que solo registra qué le llegó.

**Qué verificamos:** que la comanda se entregó a cocina una sola vez y con el contenido correcto, no el resultado del plato.

## 5. Ejemplo práctico en software

`OrderService` debe notificar al cliente cuando se confirma una compra, llamando a `EmailService.send()`. En el test se reemplaza `EmailService` por un mock:

```python
from unittest.mock import Mock

def test_confirmar_orden_envia_un_correo():
    email = Mock()                              # mock, no envía nada real
    service = OrderService(email_service=email)

    service.confirm(Order(id=1, customer="ana@mail.com"))

    email.send.assert_called_once_with(
        to="ana@mail.com", subject="Pedido 1 confirmado"
    )
```

**Problema que evita:** sin el mock, cada ejecución de los tests enviaría correos reales (spam a clientes, costos, tests lentos y dependientes de la red/SMTP). Con el mock, el test es rápido, determinista y aislado.

**Qué verificamos:** que `OrderService` llamó a `EmailService.send()` exactamente una vez y con el correo y destinatario correctos (verificación de comportamiento/interacción, no de un valor de retorno).
