from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from app.schema import schema

app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000,
    )
    CORS(app, supports_credentials=True)
    app.run(threaded=True, **config)