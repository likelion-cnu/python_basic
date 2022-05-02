import random

book_list = []

def register_book():
    new_book = {}
    new_book["제목"] = input("제목을 입력하세요: ")
    new_book["저자"] = input("저자를 입력하세요: ")
    new_book["출판사"] = input("출판사를 입력하세요: ")
    new_book["입고일"] = input("입고일을 입력하세요: ")
    book_list.append(new_book)

def discard_book():
    title = input("폐기할 책 제목을 입력하세요: ")
    for i in range(len(book_list)):
        if book_list[i]["제목"] == title:
            del book_list[i]
            break

def list_book():
    for i in range(len(book_list)):
        for key, value in book_list[i].items():
            print(f"{key}: {value}", end = "  ")
        print()

def recommend_book():
    random_recommend = random.choice(book_list)
    for key, value in random_recommend.items():
        print(f"{key}: {value}", end = "  ")


while True:
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    menu_num = int(input("메뉴 선택: "))

    if menu_num == 1:
        register_book()
    elif menu_num == 2:
        discard_book()
    elif menu_num == 3:
        list_book()
    elif menu_num == 4:
        recommend_book()
    elif menu_num == 5:
        print("메뉴를 종료합니다.")
        break
    else:
        print("메뉴에 없는 번호를 입력했습니다.")
        print("다시 입력하세요.")