import numpy as np

# Đọc file
vocabs = np.load("./vocabs.npy", allow_pickle=True)
documents = np.load("./documents.npy", allow_pickle=True)
matrix = list(np.zeros((vocabs.shape[0], documents.shape[0])))  

for doc in range(len(documents)):
    for word in documents[doc].split():
        matrix[np.where(vocabs == word)[0][0]][doc] = 1

np.save('./incidenceMatrix.npy', matrix, allow_pickle=True)  

print("Done!")