from flask_restful import abort, reqparse
from src.app.authentication import Resource


todos = {}
todos['task_1'] = 'Create api template'


parser = reqparse.RequestParser()
parser.add_argument('task_text', type=str)


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos.keys():
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class Todos(Resource):
    def get(self, current_user):
        return todos


class Todo(Resource):
    def get(self, current_user, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return {todo_id: todos[todo_id]}

    def put(self, current_user, todo_id):
        args = parser.parse_args()
        todos[todo_id] = args['task_text']
        return {todo_id: todos[todo_id]}, 201
