StableIncome = True
NoLoans = True

if StableIncome and NoLoans:
    print("eligible")




StableIncome = True
NoLoans = False

if StableIncome or NoLoans:
    print("eligible")




StableIncome = True
CriminalRecord = False

if StableIncome and not CriminalRecord:
    print("eligible")