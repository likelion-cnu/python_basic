import random

book_list = []

def enrollment_book():
    book_name = input("책 제목을 입력: ")
    book_list.append(book_name)
    author = input("저자를 입력해주세요: ")
    book_list.append(author)
    publisher = input("출판사를 입력해주세요: ")
    book_list.append(publisher)
    date = input("입고일을 입력해주세요: ")
    book_list.append(date)

def delete_book(num1):
    for i in range(4):
        del book_list[num1]

def recommend():
    check = random.choice(book_list)
    index = book_list.index(check)
    if(index%4 == 0):
        return check
    else:
        recommend()

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
        dele = input("삭제하려는 책 이름: ")
        index = book_list.index(dele)
        #print(index)
        delete_book(index)

    elif menu_num == "3":
        print(book_list)

    elif menu_num == "4":
        num2 = recommend()
        print(num2)

    elif menu_num == "5":
        break