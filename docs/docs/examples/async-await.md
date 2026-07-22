---
title: Async/Await
description: Asynchronous programming examples
sidebar_label: Async/Await
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Async/Await

Examples of asynchronous programming in ArabPy.

## Basic Async Functions

### Simple Async Function

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import asyncio

    async def greet():
        print("Hello")
        await asyncio.sleep(1)
        print("World")

    asyncio.run(greet())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد asyncio

    غير_متزامن تعريف greet():
        طباعة("Hello")
        انتظار asyncio.sleep(1)
        طباعة("World")

    asyncio.run(greet())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello
World
```

**Explanation:** Basic async function using `غير_متزامن` for `async` and `انتظار` for `await`.

### Async Function with Return Value

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import asyncio

    async def add(a, b):
        await asyncio.sleep(0.1)
        return a + b

    async def main():
        result = await add(5, 3)
        print(result)

    asyncio.run(main())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد asyncio

    غير_متزامن تعريف add(a, b):
        انتظار asyncio.sleep(0.1)
        إرجاع a + b

    غير_متزامن تعريف main():
        result = انتظار add(5, 3)
        طباعة(result)

    asyncio.run(main())
    ```
  </TabItem>
</Tabs>

**Output:**
```
8
```

**Explanation:** Async function returning value.

## Running Multiple Tasks

### Running Concurrent Tasks

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import asyncio

    async def task(name, delay):
        print(f"Task {name} started")
        await asyncio.sleep(delay)
        print(f"Task {name} completed")

    async def main():
        await asyncio.gather(
            task("A", 1),
            task("B", 2),
            task("C", 1)
        )

    asyncio.run(main())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد asyncio

    غير_متزامن تعريف task(name, delay):
        طباعة(f"Task {name} started")
        انتظار asyncio.sleep(delay)
        طباعة(f"Task {name} completed")

    غير_متزامن تعريف main():
        انتظار asyncio.gather(
            task("A", 1),
            task("B", 2),
            task("C", 1)
        )

    asyncio.run(main())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Task A started
Task B started
Task C started
Task A completed
Task C completed
Task B completed
```

**Explanation:** Running multiple async tasks concurrently.

### Creating Tasks

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import asyncio

    async def task(name, delay):
        await asyncio.sleep(delay)
        print(f"Task {name} done")

    async def main():
        task1 = asyncio.create_task(task("A", 1))
        task2 = asyncio.create_task(task("B", 2))
        
        await task1
        await task2

    asyncio.run(main())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد asyncio

    غير_متزامن تعريف task(name, delay):
        انتظار asyncio.sleep(delay)
        طباعة(f"Task {name} done")

    غير_متزامن تعريف main():
        task1 = asyncio.create_task(task("A", 1))
        task2 = asyncio.create_task(task("B", 2))
        
        انتظار task1
        انتظار task2

    asyncio.run(main())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Task A done
Task B done
```

**Explanation:** Creating async tasks with `asyncio.create_task`.

## Async Context Managers

### Async With Statement

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import asyncio

    async def async_context():
        print("Enter context")
        yield
        print("Exit context")

    async def main():
        async with async_context():
            print("Inside context")

    asyncio.run(main())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد asyncio

    غير_متزامن تعريف async_context():
        طباعة("Enter context")
        إنتاج
        طباعة("Exit context")

    غير_متزامن تعريف main():
        غير_متزامن مع async_context():
            طباعة("Inside context")

    asyncio.run(main())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Enter context
Inside context
Exit context
```

**Explanation:** Async context manager using `غير_متزامن مع` for `async with`.

## Async Iterators

### Async For Loop

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import asyncio

    async def async_range(n):
        for i in range(n):
            await asyncio.sleep(0.1)
            yield i

    async def main():
        async for num in async_range(3):
            print(num)

    asyncio.run(main())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد asyncio

    غير_متزامن تعريف async_range(n):
        لكل i في مدى(n):
            انتظار asyncio.sleep(0.1)
            إنتاج i

    غير_متزامن تعريف main():
        غير_متزامن لكل num في async_range(3):
            طباعة(num)

    asyncio.run(main())
    ```
  </TabItem>
</Tabs>

**Output:**
```
0
1
2
```

**Explanation:** Async for loop using `غير_متزامن لكل` for `async for`.

## Practical Examples

### Fetching Data (Simulated)

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import asyncio

    async def fetch_data(url):
        print(f"Fetching {url}")
        await asyncio.sleep(1)
        return f"Data from {url}"

    async def main():
        urls = ["url1", "url2", "url3"]
        tasks = [fetch_data(url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

    asyncio.run(main())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد asyncio

    غير_متزامن تعريف fetch_data(url):
        طباعة(f"Fetching {url}")
        انتظار asyncio.sleep(1)
        إرجاع f"Data from {url}"

    غير_متزامن تعريف main():
        urls = ["url1", "url2", "url3"]
        tasks = [fetch_data(url) لكل url في urls]
        results = انتظار asyncio.gather(*tasks)
        لكل result في results:
            طباعة(result)

    asyncio.run(main())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Fetching url1
Fetching url2
Fetching url3
Data from url1
Data from url2
Data from url3
```

**Explanation:** Simulated concurrent data fetching.

### Timeout Handling

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import asyncio

    async def slow_operation():
        await asyncio.sleep(5)
        return "Done"

    async def main():
        try:
            result = await asyncio.wait_for(slow_operation(), timeout=2.0)
            print(result)
        except asyncio.TimeoutError:
            print("Operation timed out")

    asyncio.run(main())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد asyncio

    غير_متزامن تعريف slow_operation():
        انتظار asyncio.sleep(5)
        إرجاع "Done"

    غير_متزامن تعريف main():
        جرب:
            result = انتظار asyncio.wait_for(slow_operation(), timeout=2.0)
            طباعة(result)
        باستثناء asyncio.TimeoutError:
            طباعة("Operation timed out")

    asyncio.run(main())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Operation timed out
```

**Explanation:** Async operation with timeout handling.

## Next Steps

- [Dataclasses](/docs/examples/dataclasses) - Data class usage
- [Typing](/docs/examples/typing) - Type hints and annotations
- [API Reference](/docs/api/index) - Detailed API documentation
