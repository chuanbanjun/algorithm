def digitatindex(index):
    if not index or index < 0:
        return False
    digits = 1
    while True:
        numbers = countofintegers(digits)
        if index < numbers*digits:
            return digitatindex2(index,digits)
        index -= digits*numbers
        digits += 1

def countofintegers(digits):
    '''�õ�digitsλ�������ܸ���'''
    if digits == 1:
        return 10
    count = 10 ** (digits-1)
    return 9*count

def beginnumber(digits):
    '''digitλ���ֵĵ�һ����'''
    if digits == 1:
        return 0
    return 10 ** (digits-1)

def digitatindex2(index,digits):
    '''�ҳ�����'''
    number = beginnumber(digits) + index / digits
    indexfromright = digits - index % digits
    for _ in range(1,indexfromright):
        number /= 10
    return number % 10

if __name__ == '__main__':
    digitatindex(12)