from flask import Flask

program = Flask("Ovo je nasa flask aplikacija")

@program.route("/")
def naslovna():
    return "Hellow World"


program.run(debug=True)