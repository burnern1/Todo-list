import json
import os

TASK_FILE = 'tasks.json'

def load_task():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r', encoding = "UTF-8") as file: # file => open(TASK_FILE, 'r', encoding = "UTF-8")
            return json.load(file) # json.load
    return []

def save_task(tasks): # add task를 통해 전달받은 해야할 일을 파일에 저장하는 기능
    with open(TASK_FILE, 'w', encoding = "UTF-8") as file: # file => open(TASK_FILE, 'w', encoding = "UTF-8")
        json.dump(tasks, file, indent = 4, ensure_ascii = False) # 



def show_menu(): # 메뉴를 보여주는 함수
    print("작업 관리 애플리케이션")
    print("1. 할 일 추가")
    print("2. 할 일 목록보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")

def add_task(task_name): # 할 일 추가 함수
    tasks = load_task() # 파일이 존재 할 경우 가져오기
    task = {'name' : task_name, "completed" : False} # 입력값에 대한 데이터 타입
    tasks.append(task)
    save_task(tasks)

def view_tasks():
    pass

def complete_task(task_number):
    pass
def delete_task(task_number):
    pass


def main():
    while(True):
        show_menu()
        choice = int(input("원하는 작업을 선택해주세요. (1~5): "))

        if choice == 1:
            task_name = input("추가할 할 일을 입력하세요: ")
            add_task(task_name)
        elif choice == 2:
            pass
            view_tasks()
        elif choice == 3:
            task_number = int(input("완료를 원하는 작업의 번호를 입력하세요"))
            complete_task()
        elif choice == 4:
            task_number = int(input("삭제를 원하는 작업의 번호를 입력하세요"))
            delete_task()
        elif choice == 5:
            print("종료")
            break
        else:
            print("잘못 입력하셨습니다. 1 ~ 5번 까지의 기능 중 하나를 선택해주세요")

main()