from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)

@app.route('/')
def get_form():
    return render_template('form.html')

@app.route('/story')
def view_story():
    place =  request.args.get("place")
    noun =  request.args.get("noun")
    verb = request.args.get("verb")
    adjective =  request.args.get("adjective")
    plural =  request.args.get("plural")
    data = story.generate({"place": place, "verb": verb, "noun": noun, "adjective": adjective, "plural_noun":plural})

    return render_template("story.html",data=data)

# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

