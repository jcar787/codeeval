import sys
def multiples_of_a_number(x, n):
    y = n
    while y < x:
        y += n
    return y

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        nums = map(int, test.split(','))
        print multiples_of_a_number(nums[0], nums[1])

if __name__ == '__main__':
    main() 
