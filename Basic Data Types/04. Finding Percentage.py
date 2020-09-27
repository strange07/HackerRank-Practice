  
# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score: 10


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x = student_marks.get(query_name)
    result = (x[0] + x[1] + x[2]) / 3
    print('%.2f' % result)
