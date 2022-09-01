import json

from . import model, db


def loads_data(filename):
    json_data = []
    with open(filename) as file:
        json_data = json.load(file)
    return json_data


def load_user(filename):
    users = loads_data(filename)
    for user in users:
        new_user = model.Users(**user)
        db.session.add(new_user)

    db.session.commit()

    print(model.Users.query.get(1).to_dict())
