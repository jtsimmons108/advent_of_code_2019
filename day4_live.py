with open('inputs/day4.in') as f:
    low, high = map(int, f.read().strip().split('-'))


def is_valid_password(num):
    num = str(num)
    return ''.join(sorted(num)) == num and len(set(num)) != len(num)

def is_more_valid_password(num):
    num = str(num)
    return ''.join(sorted(num)) == num and 2 in [num.count(d) for d in '0123456789']


print(len([password for password in range(low, high) if is_valid_password(password)]))
print(len([password for password in range(low, high) if is_more_valid_password(password)]))