import random


book_list=[["어린왕자", "생텍쥐페리", "열린책들","20210409"]]
table_list=["제목", "저자", "출판사", "입고일"]

def enrollment_book():
    book_name=input("what is the book name?: ")
    book_auth=input("who is the author?: ")
    book_pub=input("where is the publishing company?: ")
    book_in=input("when is the book in stock?(yyyymmdd): ")
    book_list.append([book_name, book_auth, book_pub, book_in])
    print(book_list)
            
def delete_book():
    find_title=input("what is the book name to delete?: ")
    del_title=[i for i in range(len(book_list)) if find_title in book_list[i]]
    num_del_title=" ".join(map(str, del_title))
    book_list.pop(int(num_del_title))
    
def book_List():
    for i in range(len(book_list)):
        print(book_list[i], end = '\n')

        
while True:
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    menu_num = input("메뉴 선택: ")

    if menu_num == "1":
        enrollment_book()

    elif menu_num == "2":
        delete_book()
        
    elif menu_num == "3":
        print(table_list)
        book_List()
        
    elif menu_num == "4":
        print(random.choice(book_list))
        
    elif menu_num == "5":
        break
    
    else:
        "제대로 입력"

print(book_list)
