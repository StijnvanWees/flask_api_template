from flask_restful import Api
from src.resources.resource_template import *


api = Api()


api.add_resource(Todos, '/todos')
api.add_resource(Todo, '/todos/<string:todo_id>')
