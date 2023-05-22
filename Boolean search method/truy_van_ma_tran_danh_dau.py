import numpy as np
from chuyen_doi import Conversion


class Incidence_Matrix:
    def __init__(self, path_matrix, path_documents, path_vocabs):
        self.matrix = np.load(path_matrix, allow_pickle=True)
        self.vocabs = np.load(path_vocabs, allow_pickle=True)
        self.documents = np.load(path_documents, allow_pickle=True)
        self.operator = {
            # operator AND
            "and": lambda vectorA, vectorB: [a and b for a, b in zip(vectorA, vectorB)],

            # operator OR
            "or": lambda vectorA, vectorB: [a or b for a, b in zip(vectorA, vectorB)],

            # operator NOT
            "not": lambda vector: [1 - x for x in vector]
        }

    # lấy các docID và doc từ vector bit
    def get_documents(self, vectorResult):
        results = []
        for i in range(len(vectorResult)):
            if vectorResult[i] == 1:
                results.append([i + 1, self.documents[i]])
        return results

    # lấy vector bit của 1 từ
    def get_row(self, word):
        return self.matrix[np.where(self.vocabs == word)[0][0]]

    # lấy kết quả trả về (vector bit) từ câu query truyền vào
    def query(self, str_query):

        # tách các thành phần trong câu query 
        tokens = []
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

        # chuyển biểu thức trung tố sang biểu thức hậu tố
        convert = Conversion()
        output = convert.infixToPostfix(tokens)

        # Thực hiện câu query từ biểu thức hậu tố
        result = []
        while (len(output) != 0):
            x = output.pop(0)
            if x[0] == '"':
                result.append(self.get_row(x[1:-1]))
            else:
                a = result.pop()
                if x == "not":
                    result.append(self.operator[x](a))
                else:
                    b = result.pop()
                    result.append(self.operator[x](a, b))

        return result[0]


