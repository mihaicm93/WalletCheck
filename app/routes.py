from flask import render_template, request, redirect, jsonify
from . import app
from .utils import load_blacklist, save_blacklist

ZACK_TOKEN_ADDRESS = "8vCAUbxejdtaxn6jnX5uaQTyTZLmXALg9u1bvFCAjtx7"

@app.route('/')
def index():
    return render_template('index.html', ZACK_TOKEN_ADDRESS=ZACK_TOKEN_ADDRESS)

@app.route('/search')
def search():
    wallet = request.args.get('wallet')
    print(f"Searching for wallet: {wallet}")

    if not wallet:
        return "Wallet address is required.", 400

    blacklist = load_blacklist()
    if wallet in blacklist:
        return "This wallet address is blacklisted.", 403

    search_type = request.args.get('type')
    if search_type == 'x':
        url = f"https://x.com/search?q={wallet}&src=typed_query"
    else:
        url = f"https://solscan.io/account/{wallet}?token_address={ZACK_TOKEN_ADDRESS}#transfers"

    print(f"Redirecting to: {url}")
    return redirect(url)

@app.route('/blacklist/add', methods=['POST'])
def add_to_blacklist():
    wallet = request.json.get('wallet')
    if not wallet:
        return jsonify({"error": "Wallet address is required."}), 400

    blacklist = load_blacklist()
    blacklist.add(wallet)
    save_blacklist(blacklist)
    print(f"Added to blacklist: {wallet}")
    return jsonify({"message": "Wallet added to blacklist."}), 200

@app.route('/blacklist/remove', methods=['POST'])
def remove_from_blacklist():
    wallet = request.json.get('wallet')
    if not wallet:
        return jsonify({"error": "Wallet address is required."}), 400

    blacklist = load_blacklist()
    if wallet in blacklist:
        blacklist.remove(wallet)
        save_blacklist(blacklist)
        print(f"Removed from blacklist: {wallet}")
        return jsonify({"message": "Wallet removed from blacklist."}), 200
    else:
        return jsonify({"error": "Wallet not found in blacklist."}), 404
