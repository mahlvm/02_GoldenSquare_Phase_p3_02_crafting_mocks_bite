from lib.task_list_challenge_03_unit_testing_peer_classes_bite import TaskList
from lib.task_challenge_03_unit_testing_peer_classes_bite import Task
from lib.task_formatter_challenge_03_unit_testing_peer_classes_bite import TaskFormatter

def test_adds_tasks_to_list_1():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]


def test_marks_tasks_as_complete_2():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert task_list.all_complete() == True

def test_marks_tasks_as_incomplete_format_3():
    task_list = TaskList()
    task_1 = TaskFormatter(Task("Walk the dog"))
    task_2 = TaskFormatter(Task("Walk the cat"))
    task_list.add(task_1.format())
    task_list.add(task_2.format())
    assert task_list.tasks == ['-[ ] Walk the dog', '-[ ] Walk the cat']
    
#def test_marks_tasks_as_complete_format_4():
#    list_edit = []
#    task_list = TaskList()
#    task_1 = TaskFormatter(Task("Walk the dog"))
#    task_2 = TaskFormatter(Task("Walk the cat"))
#    task_1.mark_complete()
#    task_2.mark_complete()
#    list = task_list.all_complete()
#    for i in list:
#        list.edit.append(task) 
#    assert task_list.tasks == ['-[x] Walk the dog', '-[x] Walk the cat']
