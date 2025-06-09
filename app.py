import os
from flask import Flask, request, jsonify
from ai_model import search_grants

app = Flask(__name__)

@app.route("/search", methods=["POST"])
def search_endpoint():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        ids = search_grants(query)
        return jsonify({"ids": ids})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)