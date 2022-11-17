Start with this:

```python3
from flask import Flask, request

app = Flask(__name__)



@app.route("/")
def home():
    return """
    <p>
      Welcome to my website! Check out my <a href="/anotherpage">other page</a>.
    </p>
    """
  
  
  
@app.route("/anotherpage")
def anotherpage():
    return """
    <p>
      This is another page. You can also go back <a href="/">home</a>.
    </p>
    """



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
```
