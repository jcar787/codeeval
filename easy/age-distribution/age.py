import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    i = int(test.strip())
    if i < 0 or i > 100:
        print 'This program is for humans'
    elif i < 3:
        print 'Still in Mama\'s arms'
    elif i < 5:
        print 'Preschool Maniac'
    elif i < 12:
        print 'Elementary school'
    elif i < 15:
        print 'Middle school'
    elif i < 19:
        print 'High school'
    elif i < 23:
        print 'College'
    elif i < 66:
        print 'Working for the man'
    else:
        print 'The Golden Years'
test_cases.close()
