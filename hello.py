
from flask import Flask

app = Flask(__name__)

def hello():
    """Return a friendly HTTP greeting.

    Returns:
        A string with the words 'Hello World!'.
    """
    a=int(input("Enter num:"))
    b=int(input("Enter num:"))
    print(a+b)
    return "Hello World!"

@app.route("/")
def route_hello():
    return hello()

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)

