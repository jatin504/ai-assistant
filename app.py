from flask import Flask, render_template_string, request, redirect
import webbrowser

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Your AI Assistant</title>
</head>
<body style="background-color: steelblue; text-align: center; padding-top: 50px;">
    <h2>Enter your command:</h2>
    <form method="POST">
        <input type="text" name="query" style="width: 300px;" required><br><br>
        <button name="action" value="youtube">Search on YouTube</button>
        <button name="action" value="google">Search on Google</button>
        <button name="action" value="instagram">Search on Instagram</button>
    </form>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form["query"]
        action = request.form["action"]

        if action == "youtube":
            return redirect(f"https://www.youtube.com/results?search_query={query}")
        elif action == "google":
            return redirect(f"https://www.google.com/search?q={query}")
        elif action == "instagram":
            username = query.replace('@', '')
            return redirect(f"https://www.instagram.com/{username}/")

    return render_template_string(TEMPLATE)


if __name__ == "__main__":
    app.run()
