from app import db                                                

# Example class
class Paperclip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serialnum = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Paperclip %r>' % self.serialnum
