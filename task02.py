import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    
    num_set = set()
    while len(num_set) < quantity:
        num_set.add(random.randint(min, max))
    return sorted(list(num_set))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
