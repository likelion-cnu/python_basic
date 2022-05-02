#문제1
import random

booklist = [] #빈 리스트 생성

def enrollment_book():
    
    enrollment_name = input("책 이름은? ")
    enrollment_author = input("책 저자는? ")
    enrollment_publisher = input("책 출판사는? ")
    enrollment_day = input("책 입고일은? 8숫자로 입력해주세요. ex:20220425 >> ")
    booklist.append({"제목":enrollment_name, "저자":enrollment_author,
    "출판사":enrollment_publisher, "입고일":enrollment_day})
    print("책 등록이 완료되었습니다. 메뉴로 돌아갑니다.")

def delete_book(): #삭제처리를 무수히 많이 고민해보았으나...전부다 실패 ㅠㅠ 그외에는 구현완료
    for i in booklist:
        print(i["제목"])
    select_book = input("삭제할 책 이름을 입력해주세요. ")
    for i in booklist:
        if select_book == i["제목"]:
            print(booklist) #책 데이터제거 완료후 체크
    print("책 삭제가 완료되었습니다. 메뉴로 돌아갑니다.")

while True:
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    menu_select = input("메뉴 선택: ")

    if menu_select == "1": #입력값(menu_select가 1일 때)
        enrollment_book()

    if menu_select == "2": #책 삭제 항목(미완성)
        delete_book()

    if menu_select == "3": #책 목록 출력
        print(list(m["제목"]for m in booklist))
        select = input("더 자세히 알고 싶다면 Y, 아니면 N을 입력하세요! ")
        #Y/N이 아닌 다른것을 입력하면 다시 메뉴로 돌아감
        if(select == "Y"):
            print(booklist)
        if(select == "N"):
            print("다시 메뉴로 돌아갑니다...")


    if menu_select == "4": #책 추천 항목
        print(random.choice(list(m["제목"]for m in booklist))+" 선택 되었습니다!!")
        #booklist의 항목중 제목항목의 리스트를 추출하여 접근, 랜덤하게 뽑아서 추천함

    if menu_select == "5": #종료
        print("프로그램을 종료합니다....")
        break