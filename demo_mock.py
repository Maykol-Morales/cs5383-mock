import unittest
from unittest.mock import Mock

class OrderService:
    def __init__(self, email):           # EmailService inyectado
        self.email = email
    def place(self, user, total):
        if total <= 0:                   # pedido inválido: no se envía correo
            return False
        self.email.send(user, f"Pedido de {total} confirmado")
        return True

class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.email = Mock()              # doble de EmailService
        self.svc = OrderService(self.email)

    def test_pedido_valido_envia_correo(self):   # PASA
        self.assertTrue(self.svc.place("ana@x.com", 50))
        self.email.send.assert_called_once_with("ana@x.com", "Pedido de 50 confirmado")
        self.assertEqual(self.email.send.call_count, 1)

    def test_pedido_invalido_no_envia(self):     # PASA
        self.assertFalse(self.svc.place("ana@x.com", 0))
        self.email.send.assert_not_called()

    def test_falla_a_proposito(self):            # FALLA: espera 2 envíos, hubo 1
        self.svc.place("ana@x.com", 50)
        self.assertEqual(self.email.send.call_count, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)

"""Output:
test_falla_a_proposito (__main__.TestOrderService.test_falla_a_proposito) ... FAIL
test_pedido_invalido_no_envia (__main__.TestOrderService.test_pedido_invalido_no_envia) ... ok
test_pedido_valido_envia_correo (__main__.TestOrderService.test_pedido_valido_envia_correo) ... ok

======================================================================
FAIL: test_falla_a_proposito (__main__.TestOrderService.test_falla_a_proposito)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/maykol/Desktop/utec/2026-2/cs5383/td/mock/demo_mock.py", line 29, in test_falla_a_proposito
    self.assertEqual(self.email.send.call_count, 2)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 2

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
"""
