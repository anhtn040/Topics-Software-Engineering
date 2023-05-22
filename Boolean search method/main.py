
from truy_van_chi_muc_nguoc import Inverted_Index
from truy_van_ma_tran_danh_dau import Incidence_Matrix

def matrix():
    Matrix = Incidence_Matrix("./incidenceMatrix.npy", "./documents.npy", "./vocabs.npy")

    while True:
        # ex: "characteristics" and "computer" and not("the" or "a") 
        str_query = input("\nQuery: ")
        if str_query.strip() == "":
            break

        vectorResult = []
        try:
            vectorResult = Matrix.query(str_query)
        except:
            pass

        results = Matrix.get_documents(vectorResult)

        if len(results) == 0:
            print("No result!")
        else:
            print("Results:")
            for result in results:
                print("Document", result[0], ":", result[1])
def invertedIndex():
    I_index = Inverted_Index("./invertedIndex.npy", "./documents.npy", skip = 3, optimal=True)
    
    while True:
        # ex: "characteristics" and "computer" 
        str_query = input("\nQuery: ")
        if str_query.strip() == "" :
            break
        
        listDocID = []
        try:
           listDocID = I_index.query(str_query)    
        except:
            pass      
        
        results = I_index.get_documents(listDocID)

        if len(results) == 0:
            print("No result!")
        else:
            print("Results:")
            for result in results: 
                print("Document", result[0], ":",result[1])  
if __name__ == "__main__":
    n =1
    while n==1:
        k=int(input('\nVui lòng chọn thuật toán mà bạn muốn sử dụng:\n1:Ma trận đánh dấu \n2:Chỉ mục ngược \n0:Exit\n'))
        if k==0:
            n=0
            break
        while (k>0 and k<3):
            print('\nCâu query có dạng: \n\t-"characteristics" \n\t-"characteristics" and "computer" \n\t-"characteristics" and "computer" and not("the" or "a")')
            if k==1:
                matrix()
                k=7
            elif k==2:
                invertedIndex()
                k=7

