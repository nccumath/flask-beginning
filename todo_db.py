
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_list.sql'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(80))

    def __init__(self, item):
        self.item = item
