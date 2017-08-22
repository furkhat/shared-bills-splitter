class Reporter(object):

    def report(self, people_debts):
        keys_sorted = sorted(people_debts.keys())
        report = []
        for person in keys_sorted:
            debts = people_debts[person]
            person_messages = []
            total_debt = 0
            if debts:
                for recipient, amount in debts:
                    person_messages.append(self.owe_message(person, amount, recipient)) 
                    total_debt += amount
            else:
                person_messages.append(self.no_debts_message(person))
            if total_debt > 0:
                person_messages.append(self.total_debt_message(person, total_debt))
            report.append("\n".join(person_messages))
        return "\n\n".join(report)

    def owe_message(self, person, amount, recipient):
        return "%s owes %s to %s" % (person, amount, recipient)

    def no_debts_message(self, person):
        return "%s has no debts." % person

    def total_debt_message(self, person, total_debt):
        return "%s owes %s in total." % (person, total_debt)
