```python3
import time

from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("Counting...", total=2*60*60)
    starttime = time.time()

    while not progress.finished:
        progress.update(task1, completed=time.time()-starttime)
        time.sleep(0.1)
```
