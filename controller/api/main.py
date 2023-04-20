"""
main.py
"""
from fastapi import FastAPI
from controller.tasks.example import example_task
from controller.misc.decorators import queue_task

fastapi = FastAPI()


@fastapi.get("/")
async def example():
    task = queue_task(example_task)
    return {"id": task.id}
