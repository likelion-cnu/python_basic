import random

book_list = []

def enrollment_book():
    name = (input("도서명 :"))
    writer = (input("저자 :"))
    ph = (input("출판사 :"))
    sd = (input("입고일 :"))
    infor = {"도서명":name, "저자":writer, "출판사":ph, "입고일":sd}
    book_list.append(infor)


def delete_book():
    del_name = input("삭제할 도서명 :")
    for a in range(len(book_list)):
        if book_list[a]["도서명"]==del_name:
            del book_list[a]
            break

def list_book():
    for a in range(len(book_list)):
        print(book_list[a], end = '\n')

def rec_book():
    rec = random.choice(book_list)
    rec_name = rec["도서명"]
    print("오늘의 책 :", rec_name)

while True:
    print('-'*30)
    print("1. 도서 등록")
    print("2. 도서 삭제")
    print("3. 도서 목록")
    print("4. 도서 추천")
    print("5. 종료")
    print('-'*30)
    x = input("메뉴 선택 : ")

    if x == "1":
        enrollment_book()

    elif x == "2":
        delete_book()

    elif x == "3":
        list_book()

    elif x == "4":
        rec_book()

    elif x == "5":
        break

    else:
        print("지원하지 않는 기능입니다.\n다시 입력해주십시오.")
        continue