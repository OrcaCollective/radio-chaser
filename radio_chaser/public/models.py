"""Radio Chaser models."""
import datetime as dt

from radio_chaser.database import Column, PkModel, db


class Radio(PkModel):
    """A radio association."""

    __tablename__ = "radios"
    badge = Column(db.String(20), unique=True, nullable=False)
    radio = Column(db.Integer(), unique=True, nullable=False)
    last_updated = Column(
        db.DateTime,
        nullable=False,
        default=dt.datetime.utcnow,
        onupdate=dt.datetime.utcnow,
    )

    def __repr__(self):
        return f"[Radio {self.badge} ({self.radio})]"
