"""
task.py
"""
from controller.api.main import fastapi
from controller.settings import celery


@fastapi.get("/task/{task_id}")
async def task(task_id: str, cancel: bool = False):
    _task = celery.control
    if cancel is True:
        _task.revoke(task_id, terminate=True)
        return {"revoked": task_id}
    _query = _task.inspect().query_task(task_id)
    return _query
