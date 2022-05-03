import random

book_list = []

def enrollment_book():
    title = input("책 제목을 입력하시오:")
    writer = input("책의 저자를 입력하시오")
    publishment = input("책의 출판사를 입력하시오:")
    date = input("책의 입고일을 입력하시오:")
    book_list.append({"제목": title, "저자": writer, "출판사": publishment, "입고일": date})
def delete_book():
    item = input("폐기할 책 제목을 입력하시오:")
    remove(item)
def show_book():
    print(book_list)
def recommand_book():
    print(random.choice(book_list))

while True:
    print("1.책 등록")
    print("2.책 삭제")
    print("3.책 목록")
    print("4.책 추천")
    print("5.종료")
    menu_num = input("메뉴 선택: ")
 if menu_num == "1":
        enrollment_book()
    elif menu_num == "2":
        delete_book()
    elif menu_num == "3":
        show_book()
    elif menu_num == "4":
        recommand_book()
    elif menu_num == "5":
        break
    else:
        print("1-5 중 입력하세요.")