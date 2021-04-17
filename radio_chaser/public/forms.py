# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, NumberRange, Length

from radio_chaser.public.models import Radio


class RadioForm(FlaskForm):

    badge = StringField(
        "Badge",
        validators=[
            DataRequired(),
            Length(min=4, max=4, message="Badge must be exactly 4 digits"),
        ],
    )
    radio = IntegerField(
        "Radio",
        validators=[
            DataRequired(),
            NumberRange(
                min=700000,
                max=799999,
                message="Radio must be exactly 6 digits and start with 7",
            ),
        ],
    )


class RadioCreateForm(RadioForm):

    def validate(self):
        initial_validation = super().validate()
        if not initial_validation:
            return False

        badge = Radio.query.filter_by(badge=self.badge.data).first()
        if badge:
            self.badge.errors.append("Record already exists for this badge")
            return False

        radio = Radio.query.filter_by(radio=self.radio.data).first()
        if radio:
            self.radio.errors.append("Record already exists for this radio")
            return False

        return True
