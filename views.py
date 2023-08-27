import pydantic
from flask import jsonify, request
from flask.views import MethodView
from models import Session, AdModel
from server import HTTPError, CreateAdModel


class AdvView(MethodView):
    def get(self, id_adv):
        with Session() as session:
            adv = session.query(AdModel).filter(AdModel.id == id_adv).first()
            if id_adv != AdModel.id:
                raise HTTPError(400, 'error')
            return jsonify({
                'id': adv.id,
                'title': adv.title,
                'created_at': adv.created_at,
                'description': adv.description,
                'owner': adv.owner,
            })

    def post(self):
        json_data = dict(request.json)
        try:
            json_data_validate = CreateAdModel(**json_data).dict()
        except pydantic.ValidationError as er:
            raise HTTPError(400, 'error')

        with Session() as session:
            ads = AdModel(**json_data_validate)
            session.add(ads)
            session.commit()
            return jsonify({
                'id': ads.id,
                'title': ads.title,
                'owner': ads.owner,
                'description': ads.description,
            })

    def delete(self, id_adv):
        try:
            with Session() as session:
                ad = session.query(AdModel).filter(AdModel.id == id_adv).first()
                session.delete(adv)
                session.commit()
                return jsonify({
                    'status': 'success'
                })
        except pydantic.ValidationError as er:
            raise HTTPError(400, 'error')