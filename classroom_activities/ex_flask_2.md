Start with this:

```python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <p>
    Hello from Bob Smith's comp
    Here's another page: <a href="/space">page</a>
    </p>
    """

@app.route("/space")
def space():
    return """
    <p>
    In space, there are things.
    You can view those things on websites like
    <a href="https://nasa.gov">NASA!</a>
    </p>
    """


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
```


1. Create another page. Link to it from the homepage and from the space page.

2. Make a link to go home on the "space" page and on the other page you created. Hint: the `href` should be `"/"`.

3. 
