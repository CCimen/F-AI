import pytest

from fai_backend.message_broker.memory import MemoryQueue


def echo(value):
    return value


def test_memory_queue_enqueue_and_result():
    queue = MemoryQueue()

    test_value = "Hello, World!"
    job_id = queue.enqueue(echo, test_value)
    assert job_id is not None

    status = queue.get_status(job_id)
    assert status == "finished"

    result = queue.get_result(job_id)
    assert result == test_value
