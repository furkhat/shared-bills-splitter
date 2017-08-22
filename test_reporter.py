import unittest
from reporter import Reporter


class TestReporter(unittest.TestCase):
    def test_report_of_empty_debts(self):
        reporter = Reporter()
        self.assertEqual(reporter.report({}), "")

    def test_report_of_single_debt(self):
        reporter = Reporter()
        debts = {"Ann": [], "Bob": [("Ann", 100)]}
        self.assertEqual(
            reporter.report(debts),
            "Ann has no debts.\n\n" \
            "Bob owes 100 to Ann\n" \
            "Bob owes 100 in total."
        )

    def test_report_of_multiple_debts(self):
        reporter = Reporter()
        debts = {"Ann": [], "Bob": [], "Jane": [("Bob", 100), ("Ann", 200)]}
        self.assertEqual(
            reporter.report(debts),
            "Ann has no debts.\n\n" \
            "Bob has no debts.\n\n" \
            "Jane owes 100 to Bob\n" \
            "Jane owes 200 to Ann\n" \
            "Jane owes 300 in total."
        )
