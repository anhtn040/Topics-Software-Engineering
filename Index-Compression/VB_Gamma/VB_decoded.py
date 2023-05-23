def get_text_lst(vb_code):
    test_lst = []
    prefix = ""
    step = 8
    count = 0
    for i in range(0, len(vb_code), step):
        if vb_code[i] == "1":
            if count == 0:
                test_lst.append(int(prefix + vb_code[i+1:i+step], 2))
            else:
                test_lst.append(test_lst[count-1] + int(prefix + vb_code[i+1:i+step], 2))
            prefix = ""
            count = count + 1
        else:
            for j in range(len(vb_code[i:i+step])):
                if vb_code[i:i+step][j] == "1":
                    prefix = vb_code[i:i+step][j:i+step]
                    break
        print(vb_code)     
        print(test_lst)   
    return test_lst


if __name__ == "__main__":
    lst = get_text_lst(input("Type the VB code: "))
    print("The text list of the above VB code is:", end=" ")
    for k in range(len(lst)):
        if k != len(lst)-1:
            print(str(lst[k]) + " ", end="")
        else:
            print(lst[k])
