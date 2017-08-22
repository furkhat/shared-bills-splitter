import unittest
from splitter import Splitter


class TestSplitter(unittest.TestCase):

    def setUp(self):
        self.splitter = Splitter()

    def test_split_lonely_payment(self):
        self.splitter.register_payment("Ann", 1000)
        self.assertEqual(self.splitter.split(), {"Ann": []})

    def test_split_person_payment(self):
        self.splitter.register_payment("Ann", 1000, "Bob")
        self.assertEqual(self.splitter.split(), {"Ann": [], "Bob": [("Ann", 500)]})

    def test_split_reciprocal_payment(self):
        self.splitter.register_payment("Ann", 1000, "Bob")
        self.splitter.register_payment("Bob", 100, "Ann")
        self.assertEqual(self.splitter.split(), {"Ann": [], "Bob": [("Ann", 450)]})

    def test_split_many_person_payments(self):
        self.splitter.register_payment("Ann", 100, "Bob")
        self.splitter.register_payment("Ann", 300, "Bob", "Jane")
        self.assertEqual(self.splitter.split(), {
            "Ann": [],
            "Bob": [("Ann", 150)], "Jane": [("Ann", 100)]
        })

    def test_split(self):
        self.splitter.register_payment("Dina", 1687, "Adilet", "Furkhat", "Ainura", "Nickita")
        self.splitter.register_payment("Dina", 975, "Adilet", "Furkhat", "Ainura", "Nickita")
        self.splitter.register_payment("Adilet", 767, "Dina", "Furkhat", "Ainura", "Nickita")
        self.splitter.register_payment("Adilet", 1554, "Dina", "Furkhat", "Ainura", "Nickita")
        self.splitter.register_payment("Dina", 406, "Adilet", "Furkhat", "Ainura", "Nickita")
        self.splitter.register_payment("Dina", 1700, "Adilet", "Furkhat", "Ainura", "Nickita")
        self.splitter.register_payment("Adilet", 1050, "Dina", "Furkhat", "Ainura", "Nickita")
        self.splitter.register_payment("Adilet", 1200, "Furkhat", "Nickita")
        self.splitter.register_payment("Furkhat", 9000, "Adilet", "Dina", "Ainura", "Nickita")
        split = self.splitter.split()
        self.assertEqual(
            sorted(split["Adilet"]),
            sorted([("Furkhat", 725.8), ("Dina", 279.4)])
        )
        self.assertEqual(
            sorted(split["Ainura"]),
            sorted([("Adilet", 674.2), ("Dina", 953.6), ("Furkhat", 1800)])
        )
        self.assertEqual(
            split["Dina"],
            [("Furkhat", 846.4)]
        )
        self.assertEqual(split["Furkhat"], [])
        self.assertEqual(
            sorted(split["Nickita"]),
            sorted([("Adilet", 1074.2), ("Furkhat", 1800), ("Dina", 953.6)])
        )
