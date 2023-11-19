def linear_search(sequence, element):
    """Ищет элемент"""
    for i in range(len(sequence)):
        if sequence[i] == element:
            return i
if __name__ == '__main__':
    print(linear_search([3, 6, 78, 1], 1))