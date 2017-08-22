class Splitter(object):
    """Shows what amount each person need to compensate to some other person in order to have
    equally paid amount for shared bills.
    """

    def __init__(self):
        """Initializes graph representing debt relations."""
        self.graph = {}

    def register_payment(self, person, amount, *debtors):
        """Registers a peyment

        Args:
            person: Name of the person who paid the bill of group of people and himself.
            amount: Total paid amount.
            debtors: Names of people sharing bill.
        """
        debt_amount = amount / (len(debtors) + 1)
        if not person in self.graph:
            self.graph[person] = {}
        for debtor in debtors:
            if debtor in self.graph[person]:
                if self.graph[person][debtor] == debt_amount:
                    del self.graph[person][debtor]
                elif self.graph[person][debtor] > debt_amount:
                    self.graph[person][debtor] -= debt_amount
                else:
                    self.graph[debtor][person] = debt_amount - self.graph[person][debtor]
                    del self.graph[person][debtor]
            else:
                if not debtor in self.graph:
                    self.graph[debtor] = {}
                self.graph[debtor][person] = self.graph[debtor].get(person, 0) + debt_amount

    def split(self):
        """Returns all debts of each person

        Returns:
            Dict where key is a person, value is an array of debts of kind tuple(name, amount)
        """
        result = {}
        for person, person_debts in self.graph.items():
            result[person] = []
            for debt_recipient, amount in person_debts.items():
                result[person].append((debt_recipient, amount))
        return result
