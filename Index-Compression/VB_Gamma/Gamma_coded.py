def get_Gamma_coded(lst):
    code = ""
    for i in range(len(lst)):
        length = ""
        offset = str(bin(lst[i]))[3::]
        for j in range(len(offset)):
            length = length + "1"
        length = length + "0"
        code = code + length + offset
    return code


if __name__ == "__main__":
    split_lst = [int(i) for i in input("Type the text list: ").split(" ")]
    gap_lst = []
    for i in range(len(split_lst)-1):
        if i == 0:
            gap_lst.append(split_lst[i])
        gap_lst.append(split_lst[i+1] - split_lst[i])
    print("List of distance after replacement:",gap_lst)    
    print("The Gamma code of the above text is:",get_Gamma_coded(split_lst)) if len(split_lst)==1 else          print("The Gamma code of the above text list is:",get_Gamma_coded(gap_lst))

    
