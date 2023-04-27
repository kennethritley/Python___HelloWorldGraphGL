'''
Simplest possible Python script that shows GraphQL in action

Author: KEN
Date:   2022.04.04
'''

from flask import Flask
from flask_graphql import GraphQLView
import graphene

# Define a simple schema with a single query
class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hello, world!"

# Create the schema
schema = graphene.Schema(query=Query)

# Initialize Flask app
app = Flask(__name__)

# Add the GraphQL endpoint
# It's here where you will point your browser http://localhost:500/graphql
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
