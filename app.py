from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

ZACK_TOKEN_ADDRESS = "8vCAUbxejdtaxn6jnX5uaQTyTZLmXALg9u1bvFCAjtx7"

@app.route('/')
def index():
    print("Rendering index page")
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
            <title>Solscan Wallet Checker</title>
            <style>
              .container {
                max-width: 500px;
                margin-top: 100px;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                background-color: #fff;
              }
              body {
                background-color: #f8f9fa;
              }
            </style>
          </head>
          <body>
            <div class="container text-center">
              <h1 class="mb-4">Solscan Wallet Checker</h1>
              <form action="/search" method="get">
                <div class="form-group">
                  <input type="text" name="wallet" class="form-control" placeholder="Enter wallet address" required>
                </div>
                <button type="submit" class="btn btn-primary">Search</button>
              </form>
            </div>
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
          </body>
        </html>
    ''')

@app.route('/search')
def search():
    wallet = request.args.get('wallet')
    print(f"Searching for wallet: {wallet}")

    if not wallet:
        return "Wallet address is required.", 400

    url = f"https://solscan.io/account/{wallet}?token_address={ZACK_TOKEN_ADDRESS}#transfers"
    print(f"Redirecting to: {url}")
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
