from app import app

if __name__ == '__main__':
    import os

    if os.getenv('FLASK_ENV') == 'production':
        from gunicorn.app.wsgiapp import run
        run()
    else:
        app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
