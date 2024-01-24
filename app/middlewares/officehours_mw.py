from datetime import datetime
from aiogram import BaseMiddleware
from typing import Any, Callable, Awaitable, AnyStr, Dict

from aiogram.types import Message


def office_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4) and \
        datetime.now().hour() in [i for i in range(8, 19)]


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
        event: Message, 
        data: Dict[str, Any]) -> Any:
        if not office_hours():
            return await handler(event, data)
        
        await event.answer(f'Bot working time:\r\nMon-Fri from 8 to 18. Come during business hours.')
        