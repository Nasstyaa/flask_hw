from flask import Flask
from views import AdvView
from app import get_app

app = get_app()

app.add_url_rule("/advertisements/<int:id_ad>/", view_func=AdvView.as_view('advertisements_delete'),
                 methods=['DELETE', 'GET'])
app.add_url_rule("/advertisements", view_func=AdvView.as_view('advertisements_create'), methods=['POST'])