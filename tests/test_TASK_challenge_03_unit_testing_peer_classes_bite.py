from lib.task_challenge_03_unit_testing_peer_classes_bite import Task


def test_constructs():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"


def test_can_be_marked_as_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.is_complete() == True