import random
book_list = []

def enroll_book():
    title = input("제목 ")
    author = input("저자 ")
    publish = input("출판사 ")
    date = input("출판일 ")
    book_list.append({"제목": title, "작가": author, "출판사": publish, "출판일": date} )

def delete_book():
    title = char(input("삭제할 책 "))
    if title in book_list:
        book_list.remove(title)
    print(book_list)

while True :
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    menu_num = input("메뉴 선택: ")

    if menu_num =="1":
        enroll_book()
    elif menu_num =="2":
        delete_book()
    elif menu_num =="3":
        print(book_list)
    elif menu_num =="4":
        print(random.choice(book_list))
    elif menu_num =="5":
        print("종료")
    else :
        break