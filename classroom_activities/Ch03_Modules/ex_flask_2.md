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

3. Make an image on the home page following [this source](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML). Note: for this classroom activity, I recommend setting the `src` to an external website, or look up how Flask handles static files (it's not obvious).

4. Change the imports at the top of your program to this:  

```python3
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)
```  
       
Then, add these:  
   
```python3
@app.route("/coolform")
def coolform():
    return """
    <form action="/submit" method="post">
      Name: 
      <input type="text" id="user_name" name="user_name" />
      Animal you would pick as a pet:
      <input type="text" id="animal" name="animal" />
      <input type="submit" value="submit" />
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    user_name = request.form["user_name"]
    animal = request.form["animal"]
    safe_user_name = escape(user_name)
    safe_animal = escape(animal)
    return f"""
    You submitted the form with this data: {safe_user_name} {safe_animal}
    """

```
        
5. Change the `submit` function so that it opens a file called "my_submit_record.txt" for appending, and writes the name and animal.
