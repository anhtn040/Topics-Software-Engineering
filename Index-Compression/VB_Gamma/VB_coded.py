def get_VB_coded(lst):
    code = ""
    for i in range(len(lst)):
        if len(lst[i]) < 8:
            temp = "1"
            for j in range(8-len(lst[i])-1):
                temp = temp + "0"
            temp = temp + lst[i]
            code = code + temp
        elif lst[i][0] == "0":
            code = code + lst[i].replace("0", "1")
        else:
            temp = ""
            for j in range(16-len(lst[i])-1):
                temp = temp + "0"
            code = code + temp + lst[i][:len(lst[i])-7] + "1" + lst[i][len(lst[i])-7:]
    return code


if __name__ == "__main__":
    split_lst = [int(i) for i in input("Type the text list: ").split(" ")]
    to_byte_lst = []
    for i in range(len(split_lst)-1):
        if i == 0:
            to_byte_lst.append(str(bin(split_lst[i]))[2::])
        to_byte_lst.append(str(bin(split_lst[i+1] - split_lst[i]))[2::])
    print("The VB code of the above text list is:", get_VB_coded(to_byte_lst))
