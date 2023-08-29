This is a (not production-ready) way to remotely run administrative commands. Mostly just a proof-of-concept.

1. This would run on the target computer (whose settings are to-be-changed)

`command_run_server.py`

```python3
from flask import Flask, request
import requests


app = Flask(__name__)


ips = ["127.0.0.1"]


@app.route("/")
def admin_view():
    return """
    <form action="/admin-run" method="POST">
    <input name="command" id="command" />
    <input type="submit" value="submit" />
    </form>
    """


@app.route("/admin-run", methods=["POST"])
def admin_run():
    command = request.form["command"]
    
    t = ""
    for ip in ips:
        response = requests.post(
            f"http://{ip}:5000/run", 
            { "command": command }
        )
        t += f"""
ip: {ip}  response code: {response.status_code}
{response.text}

"""

    return f" <pre>{t}</pre>"


if __name__ == "__main__":
    app.run(port=5001)
```

2. This one would run on the admin's computer.

`admin_controller.py`
```python3
from flask import Flask, request
import subprocess


app = Flask(__name__)


@app.route("/run", methods=["POST", "GET"])
def run_command():
    raw_command = request.form["command"]
    mapping = {
        "ls": ["ls"],
        "delete_vs_code_cache": ["echo", "'Not yet implemented'"],
        
        # I find this un-obvious, but -N can be used to avoid creating multiple copies of the downloaded file.
        "update_command_runner": ["wget", "-N", "Need_an_https_path_to_this_file_somewhere_that_doesn't_have_easy_write_access"]
    }
    safe_command = mapping[raw_command]
    result = subprocess.run(safe_command, capture_output=True)
    return "<pre>" + result.stdout.decode() + "</pre>"


if __name__ == "__main__":
    app.run()
```
