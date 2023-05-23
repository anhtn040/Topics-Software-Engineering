def get_length(unary_code):
    length = 0
    for num in unary_code:
        if num == "1":
            length = length + 1
        else:
            return length


def get_text_lst(gamma_code):
    test_lst = []
    unary = ""
    offset = ""
    count = 0
    count_offset = 0
    is_count_length = True
    check_one_gap = False
    for char in gamma_code:
        count = count + 1
        if len(test_lst) != 0 and check_one_gap:
            test_lst.append(test_lst[len(test_lst) - 1] + 1)
            if count < len(gamma_code) - 1:
                if gamma_code[count-1] == "0":
                    check_one_gap = True
                else:
                    unary = gamma_code[count-1]
                    check_one_gap = False
                continue
        if is_count_length:
            unary = unary + char
            if char == "0":
                is_count_length = False
        else:
            if count_offset == get_length(unary):
                if len(test_lst) == 0:
                    test_lst.append(int("1" + offset, 2))
                else:
                    test_lst.append(test_lst[len(test_lst) - 1] + int("1" + offset, 2))
                if count < len(gamma_code) - 1:
                    if gamma_code[count-1] == "0":
                        check_one_gap = True
                unary = char
                offset = ""
                is_count_length = True
                count_offset = 0
            else:
                offset = offset + char
                count_offset = count_offset + 1
    if len(test_lst) != 0 and check_one_gap:
        test_lst.append(test_lst[len(test_lst) - 1] + 1)
    else:
        test_lst.append(test_lst[len(test_lst) - 1] + int("1" + offset, 2))
    print(gamma_code)
    return test_lst


if __name__ == "__main__":
    lst = get_text_lst(input("Type the Gamma code: "))
    print("The text list of the above Gamma code is:", end=" ")
    for j in range(len(lst)):
        if j != len(lst) - 1:
            print(str(lst[j]) + " ", end="")
        else:
            print(lst[j])
