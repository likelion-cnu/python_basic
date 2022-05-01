import random

# key를 제외하고 value들만 따로 저장하는 리스트 
book_values = []

# 책 등록 함수
def enrollment_book():
    # 질문에 대한 답(=values)를 입력받아서 리스트에 추가해줍니다. 
    for i in range(4):
        if i == 0:
            n = input('책 제목을 입력해주세요! : ')
            book_values.append(n)
        if i == 1:
            n = input('책 저자를 입력해주세요! : ')
            book_values.append(n)
        if i == 2:
            n = input('책 출판사를 입력해주세요! : ')
            book_values.append(n)
        if i == 3:
            n = int(input('책 입고일을 입력해주세요! : ')) 
            book_values.append(n)
            

# 책 삭제 함수
def delete_book():  
    del_book = input("삭제할 책 이름을 적어주세요! : ")
    
    # 삭제할 책 이름의 원소를 찾아 인덱스를 반환받습니다.
    del_index = book_values.index(del_book)
    
    # 일차원 리스트에 저장했기에 책 제목부터 입고일까지 원소들을 모두 삭제 시켜줍니다.
    del book_values[del_index:del_index+4]
 
        
# 책 목록 함수
def list_book():
    # 일차원 리스트에 저장되었기에 num 변수를 통해서 리스트의 인덱스에 접근해줍니다. (0,1,2,3) -> (4,5,6,7)
    num = 0
    
    # len(book_values) // 4 (= 저장된 책의 수)을 통해서 반복문의 범위를 지정해줍니다
    for i in range(len(book_values)//4):
        print("제목 : {0}, 저자 : {1}, 출판사 : {2}, 입고일 : {3}\n".format(book_values[num], book_values[num+1], book_values[num+2], book_values[num+3]))
        num += 4
    
    
# 책 추천 함수
def recommend_book():
    # 0, 4, 8 등등 일차원 리스트에서 책 제목 값 인덱스만을 범위로 랜덤 숫자를 생성합니다.
    rdn_num = random.randrange(0, len(book_values), 4)
    
    print("오늘같은 날 이 책은 어떠신가요??\n")
    print("제목 : {0}, 저자 : {1}, 출판사 : {2}, 입고일 : {3}".format(book_values[rdn_num], book_values[rdn_num+1], book_values[rdn_num+2], book_values[rdn_num+3]))


while True:
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    menu_num = input("메뉴 선택: ")

    # 책 등록 함수 호출
    if menu_num == "1":
        enrollment_book()
    
    # 책 삭제 함수 호출
    elif menu_num == "2":
        delete_book()
    
    # 책 목록 함수 호출
    elif menu_num == "3":
        list_book()
    
    # 책 추천 함수 호출
    elif menu_num == "4":
        recommend_book()
    
    # 프로그램 종료
    elif menu_num == "5":
        break
    
    # 1~5까지가 아닌 다른 입력을 받는다면 
    else:
        print("올바른 번호가 아닙니다. 재입력해주세요 !\n")
        continue