# Notifio
Notifio is a flexible and decoupled event bus library for Python. With asyncio at its core, it allows for seamless communication between different components of your software, making it a great fit for a wide variety of Python projects.

The `EventBus` class in this code implements an event bus that allows subscribers to receive and handle events that are published by other parts of the system.

##Installation and Dependencies
The code uses the asyncio library, which is built into Python 3.11 and later versions. Therefore, no additional installation is required.

##Usage
To use the `EventBus` class, create an instance of it in your code, then call its `subscribe`, `unsubscribe`, and `publish` methods as needed.

##Creating an EventBus Instance
To create an instance of the `EventBus` class, simply instantiate it:
```python
event_bus = EventBus()
```

##Subscribing to Events
To subscribe to an event, call the `subscribe` method, passing in the event type and the event handler function. The event handler should be an asynchronous function that takes any number of arguments and/or keyword arguments.

```python
async def event_handler(arg1, arg2, kwarg1=None, kwarg2=None):
    # Handle the event
    ...

await event_bus.subscribe('event_type', event_handler)
```

##Unsubscribing from Events
To unsubscribe from an event, call the `unsubscribe` method, passing in the event type and the event handler function that was previously subscribed.

```python
await event_bus.unsubscribe('event_type', event_handler)
```

##Publishing Events
To publish an event, call the `publish` method, passing in the event type and any arguments and/or keyword arguments that should be passed to the event handlers.

```python
await event_bus.publish('event_type', arg1, arg2, kwarg1=val1, kwarg2=val2)
```

##Error Handling
If an error occurs while executing an event handler, the error will be logged to the console using Python's built-in logging library. Specifically, an error message will be printed that includes the name of the event handler and the event type, as well as the error message that was raised by the handler.

```python
logging.error(f"Error while executing handler {handler.__name__} for event {event_type}: {error}")
```

##Conclusion
The `EventBus` class in this code provides a simple and flexible way to implement an event bus in your Python code. By allowing multiple parts of your system to subscribe to and publish events, it makes it easier to implement decoupled, maintainable software architectures.
