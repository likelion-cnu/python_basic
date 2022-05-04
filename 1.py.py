import random

 

book_list = []

 

def enrollment_book():

    title = input()

    author = input()

    company = input()

    date = input()

    book_list.append({'title': title, 'author': author, 'company':company, 'date':date }) 

 

def delete_book(name):  # 책 삭제 함수

    for i in range(len(book_list)):

        if book_list[i]['title'] == name:

            order = i

    del book_list[order]

 

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

        title = input()

        delete_book(title)

 

    elif menu_num == "3":

        print(book_list)

 

    elif menu_num == "4":

        print (random.choice(book_list))

 

    elif menu_num == "5":

        break

 

    else:

        print("1부터 5 사이의 메뉴를 골라주세요.")
        continue