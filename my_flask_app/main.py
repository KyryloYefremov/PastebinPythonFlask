from app import app, db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()
    # u = User(nick="Kirrawv")
    # db.session.add(u)
    # db.session.commit()


@app.route("/")
def home():
    return "<h1> Hello </h1>"


if __name__ == '__main__':
    app.run(debug=True)
