# from statistics import mean
def mean(nums):
    if len(nums) == 0:
        return None
    return sum(nums)/len(nums)


def percentage(marks, student):
    return mean(marks[student])


# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(percentage(student_marks, query_name))
