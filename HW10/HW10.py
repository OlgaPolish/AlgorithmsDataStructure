def change_bill(small, bill):
    change_bills = []
    for i in small:
        while bill >= i:
            change_bills.append(i)
            bill -= i
    return change_bills


small_bills = [10, 5, 2, 1]

banknote1 = 100
banknote2 = 23
print(change_bill(small_bills, banknote1))
print(change_bill(small_bills, banknote2))
