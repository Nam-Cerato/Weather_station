from app import app
# from app import create_app

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    # app.run(debug=True)