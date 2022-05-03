import random

book_list = []

def enrollment_book():  # 책 등록 함수
    title = input("제목을 입력하시오")
    author = input("저자를 입력하시오")
    publisher = input("출판사를 입력하시오")
    date = input("입고일을 입력하시오")
    book_list.append({"제목":title, "저자":author, "출판사":publisher, "입고일":date})

def delete_book():  # 책 삭제 함수 
  title = input("제목을 입력하시오")
for i in range(0, len(book_list)):
      if book_list[i]["제목"] == "title":
          del book_list[i]
          break
          
def show_book():  # 책 목록 함수
    print(book_list)

def recommend_book():  # 책 추천 함수
    print("추천하는 책", random.choice(book_list))


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
        show_book()
    elif menu_num == "4":
        recommend_book()
    elif menu_num == "5":
        break
    else:
        print("1-5 중 입력하시오.")
        