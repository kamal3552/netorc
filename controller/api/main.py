"""
main.py
"""
from fastapi import FastAPI
from controller.misc.decorators import queue_task
from controller.worker.tasks.example import example_task

fastapi = FastAPI()


@fastapi.get("/api")
async def example():
    task = queue_task(example_task)
    return {"id": task.id}
