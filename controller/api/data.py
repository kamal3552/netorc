"""
data.py
"""
from controller.api.main import fastapi
from controller.misc.celery import celery


@fastapi.get("/api/data/task/{task_id}")
async def task_result(task_id: str):
    task = celery.AsyncResult(task_id)
    return {"status": task.status, "result": task.result}
