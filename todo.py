todo_list = []

def show_menu():
    print("작업 관리 애플리케이션")
    print("1. 할 일 추가")
    print("2. 할 일 목록보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")

def add_task(task_name):
    todo_list.append(task_name)
    print(f"{task_name} 추가 됨")

def view_tasks():
    print(todo_list)

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
            add_task()
        elif choice == 2:
            print(todo_list)
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