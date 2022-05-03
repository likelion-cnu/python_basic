#문제1

import random
import time

book_list = []

def enrollment_book():
    name = input("책의 제목을 입력하세요 : ")
    writer = input("저자를 입력하세요 : ")
    publish = input("출판사를 입력하세요 : ")
    date = input("입고일 입력하세요 : ")
    book_list.append({"이름":name ,"저자":writer,"출판사":publish,"입고일":date})
    
def delete_book():
    del_name = input("삭제할 책의 제목은?")
    for i in range(len(book_list)):
        if book_list[i]["이름"] == del_name:
            del book_list[i]
            break

while True:
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    menu_num = input("메뉴 선택: ")
    break

    if menu_num == "1":
        enrollment_book()
    elif menu_num == "2":
        delete_book()
    elif menu_num == "3":
        print(book_list)
    elif menu_num == "4":
        print(random.choice(book_list))
    elif menu_num == "5":
        break
    else:
        print("다시 입력해 주세요.")
