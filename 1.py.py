import random

book_list = []


def enrollment_book():  # 책 등록 함수
    print("책제목")
    title = input()
    print("저자")
    author = input()
    print("출판사")
    publisher = input()
    print("입고일")
    stock_date = input()

    book_list.append({'title': title, 'author': author, 'publisher': publisher, 'stock_date': stock_date})


def delete_book():  # 책 삭제 함수
    print("책 제목을 입력해주세요.")
    title = input()

    for book in book_list:
        if book["title"] == title:
            book_list.remove(book)
            return

    print("해당 제목에 해당하는 책이 없습니다.")


def print_book(book):
    print("제목: " + book["title"] + ", 저자: " + book["author"] + ", 출판사: " + book["publisher"] + ", 입고일: " + book["stock_date"])


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
        for book in book_list:
            print_book(book)
    elif menu_num == "4":
        print_book(random.choice(book_list))
    elif menu_num == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("해당하는 메뉴가 존재하지 않습니다.")