import random

book_list = []

def enrollment_book():  # 책 등록 함수
    name = input("등록할 책의 이름을 입력하시오 ")
    write = input("등록할 책의 저자를 입력하시오 ")
    publish = input("등록할 책의 출판사를 입력하시오 ")
    date = input("등록할 책의 입고일 입력하시오 ")

    book_list.append({"이름" : name ,"저자" : write, "출판사" : publish, "입고일" : date})

def delete_book():  # 책 삭제 함수
    del_name = input("삭제할 책의 이름을 입력하시오 ")
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

    if menu_num == "1":
        enrollment_book()

    elif menu_num == "2":
        delete_book()

    elif menu_num == "3":
        print(book_list)

    elif menu_num == "4":
        print(random.choice(book_list))

    elif menu_num == "5":
        print("프로그램을 종료합니다")
        break
    else:
        continue