## Preliminaries:
## Run this in the terminal:
##    pip install flask


## See https://flask.palletsprojects.com/en/2.1.x/quickstart/


"""
UNFINISHED

For this one, replace filename and words
localhost:5000/filename/words

For this one, type the literal address
and then use the submission form
localhost:5000/theform
"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/theform/submission")
def formsubmit():
    fn = request.args["fn"]
    q1 = request.args["q1"]
    q2 = request.args["q2"]
    q3 = request.args["q3"]
    if fn.endswith(".py"):
        return "Error: You attempted to attack the server. Bad."
    else:
        f = open(fn, "w")
        # towrite = f"""Q1: \n {q1} \n Q2: \n {q2} \n Q3: \n {q3} \n"""
        towrite = q1
        f.write(towrite)
        f.close()
        return f"Wrote {towrite} to {fn}."

@app.route("/theform")
def theform():
    return """
    <form action="/theform/submission">
    Filename: <input name="fn"/>  <br/>
    Q1: <textarea name="q1"> </textarea> <br/>
    Q2: <textarea name="q2"> </textarea> <br/>
    Q3: <textarea name="q3"> </textarea> <br/>
    <input type="submit" />
    </form>
    """


@app.route('/<filename>/<content>')
def writeThings(filename, content):
    # type: (str, str) -> str
    if filename.endswith(".py"):
        return "Error: You attempted to attack the server. Bad."
    else:
        f = open(filename, "w")
        f.write(content)
        f.close()
        return f"Wrote {content} to {filename}."
