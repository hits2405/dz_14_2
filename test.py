from app import model, db
from flask import current_app as app, request, jsonify
import json


def get_first_user():
    result = []
    for user in model.Users.query.all():
        result.append(user.to_dict())
    return result

a = get_first_user()
print(a)