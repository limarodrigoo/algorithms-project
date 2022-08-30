def quick_sort(string, start, end):
    if start < end:
        p = partition(string, start, end)
        quick_sort(string, start, p - 1)
        quick_sort(string, p + 1, end)


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):
        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = string[delimiter], string[index]

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    first_string = list(first_string)
    second_string = list(second_string)

    quick_sort(first_string, 0, len(first_string) - 1)
    quick_sort(second_string, 0, len(second_string) - 1)
    if first_string == second_string:
        return True
    return False
