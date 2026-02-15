Additional Questions:

- Hit Counter: ✅
  - Thread Safe ✅
  - High Stream Optimization ✅
- Web Crawler ✅
  - Threading code ✅
    - Python GIL and CPython aspects ✅
    - What is the objective of threads ? ✅
    - How does concurrency work vs parallelism ✅
    - asyncio
- TokenBucket ✅

  - Threading ✅

- Space Panorama ✅

  - file object interaction ✅

- Duplicate Files has good applicable questions ✅

- Buffer, md5, streaming, opening files and writing files, threading, Robin-Karp Hash ✅

- LFU Cache
- Island:

  - MST
  - Short Bridge - between 2 island (https://leetcode.com/problems/shortest-bridge/editorial/)
  - Single Flip (PDF)

---

- Combination Sum:
  - Backtracking -> DFS + Pruning + undo
- CountAndSay:
  - Need to simplify the way I look at these problems -> sliding window but could be solved with a simple for loop
  - first think about the simplest way to solve it which is the for loop
- FileByteInFile:
  - Sliding window got it!! Also figured out the length hash
  - Robin Karp a little confusing

## Python:

    - CPython - Reads rules and implements them:
        - Compilation - Converts code into byte code/machine code
        - Python Virtual Machine - Interprets the byte code and executes it on runtime
    - GIL (Global Interpreter Lock):
        - Ensures only a single thread of bytecode executes at a time
    - Threading vs Concurrency vs Parallelism:
        - Thread: smallest unit of execution
        - Concurrency: Managing many tasks at once - while a single thread awaits for response it releases the GIL and allows another thread to be used - only uses single core on CPU
        - Parallelism: Doing many task simultaneously leveraging multiple cores
    - Threading vs Asyncio:
        - Asyncio - developer in charge - IO tasks
        - Threading - OS scheduler in charge - IO tasks

## Threading:

    - Use this for I/O bound calls (Network or file access calls)

```py
import threading
import time

def task(name, duration):
    time.sleep(2)
    print(f"${name} starting")
    time.sleep(duration)
    print(f"${name} finished")

t1 = threading.Thread(target=task, args =("A", 2))
t2 = threading.Thread(target= task, args =("B", 1))

t1.start()
t2.start()

print("Threads Starting")

t1.join()
t2.join()

# Both threads start at the same time
# second thread ends earlier and hence is done earlier
```

For many tasks use concurrent.futures from ThreadPoolExecutor

```py
from concurrent.futures import ThreadPoolExecutor
import time
def worker(n):
    time.sleep(5)
    return n*n

cur = time.time()
for w in [1,2,3,4,5,6]: # This will take 5 seconds for each request (30 seconds)
    worker(w)
fin = time.time()
print(cur-fin)

cur = time.time()
with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(worker, [1,2,3,4,5,6])

fin = time.time()
print(results)
print(cur-fin) # This will take 15 seconds since 2 requests simultaneously
```

Use asyncio alternatively

```py
import asyncio
import time

async def worker(id, delay):
    print(f"Started: {id}")
    await asyncio.sleep(delay)
    print(f"Finished: {id}")

async def main():
    results = await asyncio.gather(
        worker(1, 2),
        worker(2,1)
    )
    print(f"Result: {results}")

if __name__ == "__main__":
    asyncio.run(main())

```
