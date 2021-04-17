# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
import logging

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user

from radio_chaser.extensions import login_manager
from radio_chaser.public.forms import RadioForm
from radio_chaser.public.models import Radio
from radio_chaser.user.forms import LoginForm
from radio_chaser.user.models import User
from radio_chaser.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")
log = logging.getLogger(__name__)


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("public.home")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    radios = Radio.query.order_by(Radio.badge).all()
    return render_template("public/home.html", login_form=form, radios=radios)


@blueprint.route("/radio/add", methods=["GET", "POST"])
@login_required
def add_radio():
    form = RadioForm(request.form)
    if form.validate_on_submit():
        radio = Radio.create(
            badge=form.badge.data,
            radio=form.radio.data,
        )
        flash(f"Created radio record: {radio}", "info")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("public/create-radio.html", form=form)


@blueprint.route("/radio/delete/<radio_id>", methods=["POST"])
@login_required
def delete_radio(radio_id: int):
    radio: Radio = Radio.get_by_id(radio_id)
    if radio is None:
        abort(404, description=f"Radio by ID {radio_id} not found")

    log.info(f"Deleting radio: {radio}")
    radio.delete()
    flash(f"Deleted radio: {radio}", "info")
    return redirect(url_for("public.home"))


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)
