
pr = [[50, 'Незамерзайка', 23], [59009, 'Молоко', 99]]
def key(product):
    dis =product[0] / 100 * product[2]
    return product[0] - dis
print(max(pr, key = key))
print(min(pr, key = key))