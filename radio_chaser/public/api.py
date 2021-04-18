from typing import List

import requests
from flask import request, current_app, Blueprint

from radio_chaser.public.models import Radio


blueprint = Blueprint("api", __name__)
LOOKUP_URL = "https://1312api.tech-bloc-sea.dev/seattle/officer"


def _get_radios() -> List[Radio]:
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
    return radios


@blueprint.route("/radios/get")
def get_badges():
    radios = _get_radios()
    return {radio.radio: radio.badge for radio in radios}


@blueprint.route("/radios/get-verbose")
def get_officer_info():
    radios = _get_radios()
    payload = {"dataset_select": "spd"}
    results = {}
    for radio in radios:
        response = requests.get(
            url=LOOKUP_URL, params={**payload, "badge": radio.badge}
        )
        data = response.json()
        if data:
            results[radio.radio] = data[0]
    return results
