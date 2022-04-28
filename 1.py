import random
import time

book_list = []

def enrollment_book():  
    book = input("책을 등록해주세요.: ")
    book_list.append(book)


def delete_book():  
    book = input("책을 삭제해주세요 : ")
    book_list.remove(book)


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
        print("책 추천 결과는 3초뒤에 발표됩니다!")
        print("3")
        time.sleep(1)
        print("2 !!")
        time.sleep(1)
        print("1 !!!!! ")
        time.sleep(1)
        print("책 추천 결과는", random.choice(book_list), "입니다!")
    elif menu_num == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다!")
