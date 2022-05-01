import random as rnd

book_list = [{"제목":"어린왕자", "저자":"생텍쥐페리", "출판사":"열린책들", "입고일":20210321}, 
             {"제목":"미적분학", "저자":"제임스", "출판사":"경문사", "입고일":20190429}]

def enrollment_book():  # 책 등록 함수
    title = input("제목을 입력해 주세요 : ")
    author = input("저자를 입력해 주세요 : ")
    publisher = input("출판사를 입력해 주세요 : ")
    date = input("입고일을 입력해 주세요 : ")
    add_book = {"제목":title, "저자":author, "출판사":publisher, "입고일":date}
    book_list.append(add_book)

def delete_book():  # 책 삭제 함수
    title = input("제목을 입력해 주세요 : ")
    for i in range(0, len(book_list)):
      if book_list[i]["제목"] == title:
          del book_list[i]
          break

def list_book():  # 책 목록 함수
    for i in range(len(book_list)):
            print(book_list[i], end = "\n")

def recommend_book():  # 책 추천 함수
    print("추천 책 : ", rnd.choice(book_list))

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
        list_book()
    elif menu_num == "4":
        recommend_book()
    elif menu_num == "5":
        break
    else:
        print("잘못된 번호입니다.")