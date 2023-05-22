
import numpy as np

# Đọc file
path_docs = "./doc-text"
with open(path_docs, 'r') as f:
    documents = f.read()


# tách từng docID_doc
docID_documents = documents.replace("\n"," ").split("/")

docID_documents.pop()

# tách docID(index) và doc
documents = []
for document in docID_documents:
    document = document.strip() 
    index = document.find(" ") 
    documents.append(document[index+1:]) 

# tạo danh sách từ 
vocabs = list(set(" ".join(documents).strip().split()))

# Tạo file từ vựng và file văn bản từ file doc - text
np.save('./documents.npy', documents, allow_pickle=True)
np.save('./vocabs.npy', vocabs, allow_pickle=True)

print("Done!")