class FizzBuzz:
    def read_file_and_fizzbuzz(self, line):
        vals = map(int, line.split())
        if len(vals) != 3:
            return False
        for i in range(vals[2]):
            temp = ''
            if (i+1) % vals[0] == 0:
                temp += 'F'
            if (i+1) % vals[1] == 0:
                temp += 'B'
            print temp if temp else i+1,
        print
        return True

import sys
def main():
    success = True
    test_cases = open(sys.argv[1], 'r')
    fizzbuzz = FizzBuzz()
    for test in test_cases:
        if not fizzbuzz.read_file_and_fizzbuzz(test):
            success = False
    return 0 if success else 1    
    
    
if __name__ == '__main__':
    main()
