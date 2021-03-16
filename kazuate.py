# Number guessing
# sample input
# 4
# 2 1 32614
# 1 2 84256
# 1 2 74823
# 0 2 72364

def check_num(num_s, data):
    '''
    num_s: string
    data: 2d list of [int, int, str]
    return: True/False
    '''
    for guess in data:
        both_good, num_good, str_num = guess

        b_good = n_good = 0
        for idx, ch in enumerate(num_s):
            if ch == str_num[idx]:
                b_good += 1
            elif ch in str_num:
                n_good += 1
        if b_good != both_good or n_good != num_good:
            return False
        else:
            pass
            # print(num_s, str_num, both_good, b_good, num_good, n_good)
    return True


num_input = int(input())
data = []

for i in range(num_input):
    good_pos, good_num, number = input().split()
    good_pos = int(good_pos)
    good_num = int(good_num)
    data.append([good_pos, good_num, number])

num_digit = len(number)

start = 10**(num_digit-1)
end = 10**num_digit

for num in range(start,end):
    str_num = str(num)
    if len(set(str_num)) == num_digit:  # all number is different
        if check_num(str_num, data):
            print(str_num)