from . import model, db
from flask import current_app as app, request, jsonify
import json


@app.route('/', methods=['GET', 'POST'])
def get_first_user():
    if request.method == "GET":
        result = []
        for user in model.Users.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200
    elif request.method == "POST":
        user_data = json.loads(request.data)
        new_user = model.Users(**user_data)

        db.session.add(new_user)
        db.session.commit()

        result = []
        for user in model.Users.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200

