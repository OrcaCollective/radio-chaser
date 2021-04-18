from flask import request, current_app

from radio_chaser.public.models import Radio
from radio_chaser.public.views import blueprint


@blueprint.route("/radios/get")
def get_badges():
    radio_numbers = request.args.getlist("radio")
    if isinstance(radio_numbers, str):
        radio_numbers = [radio_numbers]

    current_app.logger.info(f"Radio #s received: {radio_numbers}")
    radios = [
        r
        for radio_number in radio_numbers
        if (r := Radio.query.filter_by(radio=radio_number).first()) is not None
    ]
    current_app.logger.info(f"Radios found: {radios}")

    return {radio.radio: radio.badge for radio in radios}
