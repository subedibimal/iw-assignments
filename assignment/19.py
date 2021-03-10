
def validate_brackets(para):
    stack_brackets = []
    candidates = [["{", "[", "("], ["}", "]", ")"]]
    for i in para:
        if i in candidates[0]:
            stack_brackets.append(i)
        else:
            cand_idx = candidates[1].index(i)
            if stack_brackets[-1] == candidates[0][cand_idx]:
                stack_brackets.pop()
            else:
                return False
    if stack_brackets == []:
        return True
    return False 