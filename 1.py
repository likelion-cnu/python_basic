import random
import time
#import pandas as pd
#import numpy as np


book_list = [["어린왕자","생텍쥐페리","열린책들","20210321"],
["미적분학","제임스","경문사","20190429"]]
#set_book_list = set(book_list)

def enrollment_book():  # 책 등록 함수
    print("추가할 도서의 정보를 입력하세요: ")
    title=input("제목: ")
    author=input("저자:")
    company=input("출판사: ")
    date=input("입고일: ")

    book_list.append([title,author,company,date])
    print(book_list)

      

def delete_book():  # 책 삭제 함수
    dele=0
    cnt=1

    for i in range(len(book_list)):
        print(("%d."+str(book_list[i]))%cnt)
        cnt+=1

    dele=int(input("삭제할 도서정보의 번호를 입력하세요: "))
    book_list.pop(dele-1)
    print("삭제완료")    


while True:
    print("\n--------------\n")
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    print("\n--------------\n")
    menu_num = input("메뉴 선택: ")
    print("\n--------------\n")

    if menu_num == "1":
        enrollment_book()     

    elif menu_num == "2":
        delete_book()

    elif menu_num == "3":
        cnt=1
        for i in range(len(book_list)):
            print(("%d."+str(book_list[i]))%cnt)
            cnt+=1
        #df=pd.DataFrame(book_list,columns=['제목','저자','출판사','입고일'])
        #print(df)    
    elif menu_num == "4":
        print(random.choice(book_list))
    elif menu_num == "5":
        break
    else:
        print("잘못된 입력입니다.")