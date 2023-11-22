from lib.task_formatter_challenge_03_unit_testing_peer_classes_bite import TaskFormatter
from unittest.mock import Mock

def test_task_incomplete_1():
    fake_task = Mock()
    fake_task.title = "Task 1"
    fake_task.complete = False
    task_form = TaskFormatter(fake_task)
    assert task_form.format() == "-[ ] Task 1"

def test_task_complete_2():
    fake_task = Mock()
    fake_task.title = "Task 2"
    fake_task.complete = True
    task_form = TaskFormatter(fake_task)
    assert task_form.format() == "-[x] Task 2"

