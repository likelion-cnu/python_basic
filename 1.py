import random

book_list = []

def enrollment_book():  # 책 등록 함수
    print("\n새 책을 등록합니다.\n")
    title = input("제목을 입력해주세요 : ")
    author = input("저자를 입력해주세요 : ")
    publiching_company = input("출판사를 입력해주세요 : ")
    delivery_date = input("입고일을 입력해주세요 : ")
    book_list.append({"제목" : title, "저자" : author, "출판사" : publiching_company, "입고일" : delivery_date})
    print("\n새 책 등록 완료\n")

def delete_book():  # 책 삭제 함수
    print("\n등록된 책을 삭제합니다.\n")
    title = input("삭제할 책 제목을 입력해주세요 : ")
    ### enumerate함수 : 인덱스와 원소를 동시에 접근 -> generator 생성
    del_title = (index for (index, item) in enumerate(book_list) if item["제목"] == title)
    ### next함수 : 반복가능객체, 마지막요소 출력 이후 반환할 기본값
    del_index = next(del_title, None)
    del book_list[del_index]
    print("\n책 삭제 완료\n")

def show_book():
    #한글 폰트때문에 깔끔한 정렬 실패..
    print("{:>10}{:>10}{:>10}{:>10}".format("제목", "저자", "출판사", "입고일"))
    print("===================================================")
    for i in range(len(book_list)):
        for item in book_list[i].values():
            print("{:>10}".format(item), end='')
        print("\n")

def recommend_book():
    recom_book = random.choice(book_list)
    print("\n오늘의 추천 책은, <<", recom_book["제목"], ">> 입니다.\n")

while True:
    print("~~~~~~~~~~")
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    print("~~~~~~~~~~")
    menu_num = input("메뉴를 선택하세요 : ")

    if menu_num == "1":
        enrollment_book()
    elif menu_num == "2":
        delete_book()
    elif menu_num == "3":
        show_book()
    elif menu_num == "4":
        recommend_book()
    elif menu_num == "5":
        break
    else:
        print("잘못된 메뉴를 선택하셨습니다.\n")