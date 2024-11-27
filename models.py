from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'  # Specify the correct table name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.String(50))
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f"<Task {self.title}>"
