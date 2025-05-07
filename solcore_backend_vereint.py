
from flask import Flask, jsonify
from flask_cors import CORS
from solcore_memory_core import MemoryCore

app = Flask(__name__)
CORS(app)

@app.route("/letzte", methods=["GET"])
def letzte_erinnerung():
    memory = MemoryCore()
    letzte = memory.lade_letzte(limit=1)
    memory.schliessen()
    if letzte:
        zeit, benutzer, symbol, kontext = letzte[0]
        return jsonify({
            "history": [[zeit, benutzer, symbol, kontext]]
        })
    return jsonify({"history": []})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
