import numpy as np
from chuyen_doi import Conversion


class Inverted_Index:
    def __init__(self, path_dictionary, path_documents, skip = 1, optimal = False):
        # skip = 1: giao (intersect)
        # skip > 1: giao + bước nhảy = skip (intersectWithSkips)
        # optimal = True: tối ưu
        self.dictionary = np.load(path_dictionary, allow_pickle=True).item()
        self.documents = np.load(path_documents, allow_pickle=True)

        if skip < 1:
            raise ValueError("skip >= 1") 
        self.skip = skip
    
        self.operator = {
            # AND
            "and": self.intersect if self.skip == 1 else self.intersectWithSkips,

            #OR
            "or": None,
            
            #NOT
            "not": None,
        }
        self.optimal = optimal

    def df(self, word):
        return len(self.dictionary[word])

    def get_posting_list(self, word):
        return self.dictionary[word]   

    def get_documents(self, listDocID):
        results = []
        for docID in listDocID: 
            results.append([docID, self.documents[docID-1]])
        return results

    def val_skip(self, p, i):
        return p[i + self.skip] 

    def hasSkip(self, p, i):
        return False if i + self.skip >= len(p) else True

    def intersect(self, p1, p2):
        i = 0
        j = 0
        answer = []
        while i < len(p1) and j < len(p2):
            if p1[i] == p2[j]:
                answer.append(p1[i])
                i += 1
                j += 1
            elif p1[i] < p2[j]:
                i += 1
            else:
                j +=1       

        return answer    

    def intersectWithSkips(self, p1, p2):
        i = 0
        j = 0
        answer = []
        while i < len(p1) and j < len(p2):
            if p1[i] == p2[j]:
                answer.append(p1[i])
                i += 1
                j += 1
            elif p1[i] < p2[j]:
                if self.hasSkip(p1, i) and self.val_skip(p1, i) <= p2[j]:
                    while self.hasSkip(p1, i) and self.val_skip(p1, i) <= p2[j]:
                        i += self.skip
                else:
                    i += 1
            else:
                if self.hasSkip(p2, j) and self.val_skip(p2, j) <= p1[i]:
                    while self.hasSkip(p2, j) and self.val_skip(p2, j) <= p1[i]:
                        j += self.skip
                else:
                    j += 1    
        return answer
    
    # tối ưu câu truy vấn AND & AND of OR's
    def optimize(self, tokens): 
        
        # lấy các biểu thức OR
        or_exps = []
        or_exp = []
        for word in tokens:
            if word == "and":
                or_exps.append(or_exp)
                or_exp= []
            else:
                or_exp.append(word)
        or_exps.append(or_exp)
               
        # ước lượng số kết quả trả về của OR's
        n_ouputs = []
        for or_exp in or_exps:
            n = 0
            for tok in or_exp:
                if(tok[0] == '"'):
                    n += self.df(tok[1:-1])
            n_ouputs.append(n)      

        # xếp theo thứ tự kết quả trả về tăng dần
        nOutput_orExp = sorted(zip(n_ouputs, or_exps), key = lambda x: x[0])       

        # tạo lại thứ tự của câu truy vấn
        query_exp = nOutput_orExp.pop(0)[1]
        for exp in nOutput_orExp:
            query_exp.append("and")
            query_exp.extend(exp[1])    

        return query_exp 
    
    def query(self, str_query):

        # tách các thành phần trong câu query 
        tokens= []
        for word in str_query.split():
            tmp = ''
            for i in word:
                if i != ')' and i != '(':
                    tmp += i
                else:
                    if tmp != '':
                        tokens.append(tmp)
                        tmp = ''
                    tokens.append(i)
            if tmp != '':
                tokens.append(tmp)

        if self.optimal == True:
            tokens = self.optimize(tokens)
            

        # chuyển biểu thức trung tố sang biểu thức hậu tố
        convert = Conversion()
        output = convert.infixToPostfix(tokens)
    
        # Thực hiện câu query từ biểu thức hậu tố
        result = []
        while(len(output) != 0):
            x = output.pop(0)
            if x[0] == '"':
                result.append(self.get_posting_list(x[1:-1]))
            else:    
                a = result.pop()
                if x == "not":
                    result.append(self.operator[x](a))
                else:
                    b = result.pop()    
                    result.append(self.operator[x](a, b))
           
        return result[0]

