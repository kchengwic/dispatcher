import sys

n = 1000000
try:
    for count in range(10):
        l = [i for i in range(n)]
        for k in l:
            i = k ** 2
            if k == n - 1:
                raise Exception('manual error..........')
except Exception as e:
    print 'Something went wrong: %s' % e.message
    raise Exception('Something went wrong: %s' % e.message)



f = open('C:\Users\kcheng\PycharmProjects\\first_project\Task1.txt', 'w')
f.write("Task1 DONE")
f.close()