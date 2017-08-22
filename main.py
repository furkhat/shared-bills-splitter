import sys
from splitter import Splitter
from reporter import Reporter


if __name__ == '__main__':
    splitter = Splitter()
    for line in sys.stdin:
        person, amount, *debtors = line.split()
        splitter.register_payment(person, float(amount), *debtors)

    print("\n\nReport:\n")
    print(Reporter().report(splitter.split()))
