cost = int(input())
card1 = cost // 100
left = cost % 100
card1 += left // 20
left %= 20
card1 += left // 10
left %= 10
card1 += left // 5
left %= 5
card1 += left
print(card1)