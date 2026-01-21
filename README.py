# Problem-1877A---Goals-of-Victory
for _ in range(int(input())):
    n = int(input())
    count_positive = 0
    count_negative = 0
    lst = [x for x in map(int, input().split())]
    for i in lst:
        if i >= 0:
            count_positive += i
        else:
            count_negative += i
    if abs(count_negative) < count_positive:
        print(abs(count_negative) - count_positive)
    else:
        tot = count_negative + count_positive
        print(abs(tot))
