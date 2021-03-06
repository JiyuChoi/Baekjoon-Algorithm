# # python 풀이
# card = [i+1 for i in range(20)]
# for _ in range(10):
#     a, b = map(int, input().split())
#     card[a-1:b] = card[a-1:b][::-1]
# print(card)
#
# # 손코딩 풀이
# card = [i for i in range(21)]
# for _ in range(10):
#     a, b = map(int, input().split())
#     l = (b-a+1)//2
#     for i in range(l):
#         card[a+i], card[b-i] = card[b-i], card[a+i]
# card.pop(0)
# print(card)


card = [(i+1) for i in range(20)]
for _ in range(10):
    s, e = map(int, input().split())
#     card[s-1:e] = card[s-1:e][::-1]
    l = (e-s+1)//2
    for i in range(l):
        card[s+i-1], card[e-(i+1)] = card[e-(i+1)], card[s+i-1]
print(card)