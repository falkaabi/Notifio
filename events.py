import asyncio
import logging

logging.basicConfig(level=logging.INFO)

class EventBus:
    def __init__(self):
        self.subscribers: dict[str|int,list] = {}

    async def subscribe(self, event_type, handler):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []

        self.subscribers[event_type].append(handler)

    async def unsubscribe(self, event_type, handler):
        if (
            event_type in self.subscribers
            and handler in self.subscribers[event_type]
        ):
            self.subscribers[event_type].remove(handler)

    async def publish(self, event_type, *args, **kwargs):
        if event_type in self.subscribers:
            try:
                async with asyncio.TaskGroup() as tg:
                    for handler in self.subscribers[event_type]:
                        tg.create_task(handler(*args, **kwargs))
            except* Exception as e:
                for error in e.exceptions:
                    logging.error(f"Error while executing handler {handler.__name__} for event {event_type}: {error}")

