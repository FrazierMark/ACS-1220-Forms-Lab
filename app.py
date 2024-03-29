from books_app.extensions import app, db
from books_app.routes import main

app.register_blueprint(main)

with app.app_context():
    db.create_all()

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)