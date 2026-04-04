from flask import Flask, render_template, request, jsonify
from smart_contract import contract
from dns_resolver import resolver
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# ✅ REGISTER DOMAIN
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() or request.form

    domain = data.get('domain')
    value = data.get('value') or data.get('ip')  # support both
    owner = data.get('owner', 'default_user')

    if domain and value:
        contract.register_domain(domain, "A", value, owner)
        return jsonify({
            'status': 'success',
            'message': f"{domain} registered successfully"
        })

    return jsonify({
        'status': 'error',
        'message': 'Invalid input'
    }), 400


# ✅ UPDATE DOMAIN
@app.route('/update', methods=['POST'])
def update():
    data = request.get_json() or request.form

    domain = data.get('domain')
    new_value = data.get('new_value')
    owner = data.get('owner')

    if domain and new_value and owner:
        if contract.update_domain(domain, new_value, owner):
            return jsonify({'status': 'success', 'message': f"{domain} updated"})
    
    return jsonify({'status': 'error', 'message': 'Update failed'}), 400


# ✅ TRANSFER OWNERSHIP
@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.get_json() or request.form

    domain = data.get('domain')
    new_owner = data.get('new_owner')
    current_owner = data.get('current_owner')

    if domain and new_owner and current_owner:
        if contract.transfer_ownership(domain, new_owner, current_owner):
            return jsonify({'status': 'success', 'message': "Ownership transferred"})

    return jsonify({'status': 'error', 'message': 'Transfer failed'}), 400


# ✅ RESOLVE DOMAIN (GET + POST both supported)
@app.route('/resolve', methods=['GET', 'POST'])
def resolve():
    if request.method == 'GET':
        domain = request.args.get('domain')
    else:
        data = request.get_json() or request.form
        domain = data.get('domain')

    if domain:
        value = resolver.resolve(domain)
        if value:
            return jsonify({
                'status': 'success',
                'domain': domain,
                'ip': value
            })

    return jsonify({'status': 'error', 'message': 'Domain not found'}), 404


# ✅ VIEW ALL (Extra for marks)
@app.route('/all', methods=['GET'])
def all_records():
    return jsonify(resolver.records)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
