import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = []; words = []; final_string = ''
    map(lambda x: nums.append(x) if x.isdigit() else words.append(x), test.strip().split(','))
    final_string = ','.join(words) if words else ''
    final_string += '|' if words and nums else ''
    final_string += ','.join(nums) if nums else ''
    if final_string:
        print final_string
test_cases.close()
