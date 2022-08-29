if __name__ == '__main__':
    from statistics import mean
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks_name = list(student_marks[query_name])
    avg = sum(marks_name) / len(marks_name)
    print("%.2f"%avg)
