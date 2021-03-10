# input("Hi: ")
def three_elements_sum(numbers):
    valid_subject = list()
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 0:
                    sorted_el = sorted([i,j,k])
                    if sorted_el not in valid_subject:
                        valid_subject.append(sorted_el)
    return valid_subject
