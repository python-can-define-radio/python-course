```python3
import time

from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("Counting...", total=2*60*60)
    lasttime = time.perf_counter()

    while not progress.finished:
        ## We could simply advance it by 0.1 seconds, but I think this approach
        ## (using perf_counter() ) is more precise. Feel free to test.
        newestTime = time.perf_counter()
        diff = newestTime - lasttime
        lasttime = newestTime
        progress.update(task1, advance=diff)
        time.sleep(0.1)
```
