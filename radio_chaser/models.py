from radio_chaser.app import db


class Radio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    badge = db.Column(db.Integer, unique=True, nullable=False)
    radio = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"<Radio {self.badge} ({self.radio})>"
