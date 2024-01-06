import asyncio
from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine]
                        | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины,
    # необходимо вернуть результат её выполнения.
    if isinstance(f, Callable):
        return await asyncio.create_task(f())
    elif isinstance(f, Task):
        return await f
    elif isinstance(f, Coroutine):
        return await asyncio.create_task(f)
    else:
        raise ValueError('invalid argument')
