Save this as a `.html` file (NOT a `.py` file), open it in a web browser, and then try moving your mouse within the black rectangle.

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <script type="text/javascript"
        src="https://cdn.jsdelivr.net/npm/brython@3.13.0/brython.min.js">
    </script>
    <script type="text/javascript"
        src="https://cdn.jsdelivr.net/npm/brython@3.13.0/brython_stdlib.js">
    </script>
</head>

<body>
    <div id="everythingwrapper">
        <script type="text/python">
from browser import document
import math


canvas = document["maincanvas"]
ctx = canvas.getContext("2d")

def clearCanvas():
    ctx.clearRect(0, 0, canvas.width, canvas.height)

def drawCircle(x, y, r):
    ctx.beginPath()
    ctx.arc(x, y, r, 0, 2 * math.pi)
    ctx.stroke()

def draw(event):
    clearCanvas()
    xs = range(0, event.clientX-40, 3)
    for x in xs:
        y = 50*(2 + math.sin(x/30))
        drawCircle(x, y, 15)
    

document["everythingwrapper"].bind("mousemove", draw)

        </script>
        <canvas id="maincanvas" width="600px" height="300px" style="border: 1px solid black; margin-left: 2em;"></canvas>
    </div>
</body>

</html>

```
