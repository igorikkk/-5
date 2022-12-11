import random

def get_unique_list_numbers(min_ = -10, max_ = 10, total = 15) -> list[int]:
    list_ = []
    while len(list_) != total:
        num = random.randint(min_, max_)
        if num not in list_:
            list_.append(num)
    return list_




list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
