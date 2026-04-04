from flask import Flask, render_template, request, jsonify
from smart_contract import contract
from dns_resolver import resolver
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    domain = request.form.get('domain')
    value = request.form.get('value')
    owner = request.form.get('owner')

    if domain and value:
        contract.register_domain(domain, "A", value, owner)
        return jsonify({'result': f"✅ {domain} registered!"})

    return jsonify({'result': "❌ Invalid input"})


@app.route('/update', methods=['POST'])
def update():
    domain = request.form.get('domain')
    new_value = request.form.get('new_value')
    owner = request.form.get('owner')

    if contract.update_domain(domain, new_value, owner):
        return jsonify({'result': f"✅ {domain} updated!"})

    return jsonify({'result': "❌ Update failed"})


@app.route('/transfer', methods=['POST'])
def transfer():
    domain = request.form.get('domain')
    new_owner = request.form.get('new_owner')
    current_owner = request.form.get('current_owner')

    if contract.transfer_ownership(domain, new_owner, current_owner):
        return jsonify({'result': f"✅ Ownership transferred!"})

    return jsonify({'result': "❌ Transfer failed"})


@app.route('/resolve', methods=['POST'])
def resolve():
    domain = request.form.get('domain')

    value = resolver.resolve(domain)

    if value:
        return jsonify({'result': f"🌐 {domain} → {value}"})

    return jsonify({'result': "❌ Not found"})


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))