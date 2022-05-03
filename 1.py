## 문제 1

import random

book_list = []

while True:
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    menu_num = input("메뉴 선택: ")
    
    if menu_num == "1":
        title = input('제목: ')
        writer = input('저자: ')
        publish = input('출판사: ')
        date = int(input('입고일: '))
        
        enrollment = [title, writer, publish, date]
        book_list.append(enrollment)
        
        print('목록에 추가됐는지 확인: ', book_list)
        
    elif menu_num == "2":
        for i in book_list:
            for j in book_list[i]:
                delete = input('삭제할 책의 제목 입력: ')
                if j == delete:
                    book_list.delete(book_list[i])
                else:
                    print('책이 존재하지 않습니다.')
                    
    print('책 목록: ', book_list)
    
    elif menu_num == "3":
        print('책 목록: ', book_list)
        
    elif menu_num == "4":
        a = random.choice(book_list) 
        print('추천 책: ', a)
        
    elif menu_num == "5":
        print("종료합니다.")
        
    else:
        print("잘못 입력하셨습니다.")
