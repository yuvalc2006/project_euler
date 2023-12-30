currency = [200, 100, 50, 20, 10, 5, 2, 1]

requested_money = 200


def find_all_ways(money, min_currency_used):
    if money > requested_money:
        return 0
    if money == requested_money:
        return 1
    ways_from_here = 0
    index = min_currency_used
    while index < len(currency):
        ways_from_here += find_all_ways(money + currency[index], index)
        index += 1
    return ways_from_here


print(find_all_ways(0, 0))
