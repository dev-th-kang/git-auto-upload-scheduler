from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용하겠다.
root = Tk()                      # root라는 창을 생성
root.geometry("600x400")       # 창 크기설정
root.title("yeachan_yeachan")    # 창 제목설정
root.option_add("*Font","맑은고딕 25") # 폰트설정
root.resizable(False, False)  # x, y 창 크기 변경 불가


def btnpress():                   # 함수 btnpress() 정의
    lb.insert(END, ent.get())     # 입력창의 내용을 리스트 박스 마지막에 추가
    
def btnpress1():                  # 함수 btnpress1() 정의
    lb.delete(lb.curselection())  # 리스트 박스 중 선택된 값 삭제

lb = Listbox(root)                # root라는 창에 리스트 박스 생성
lb.config(selectmode="single")    # 리스트 박스 selectmode 설정
lb.config(height = 0)             # 리스트 박스 높이 설정
lb.pack()                         # 리스트 박스 배치
    
ent = Entry(root)                 # root라는 창에 입력창 생성
ent.pack()                        # 입력창 배치
    
btn = Button(root)                # root라는 창에 버튼 생성
btn.config(text= "추가")          # 버튼 내용 
btn.config(width=10)              # 버튼 크기
btn.config(command=btnpress)      # 버튼 기능 (btnpree() 함수 호출)
btn.pack()                        # 버튼 배치

btn1 = Button(root)                # root라는 창에 버튼 생성
btn1.config(text= "삭제")          # 버튼 내용 
btn1.config(width=10)              # 버튼 크기
btn1.config(command=btnpress1)     # 버튼 기능 (btnpree1() 함수 호출)
btn1.pack()                        # 버튼 배치

root.mainloop()                  # 창 실행