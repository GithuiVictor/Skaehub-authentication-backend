from sqlalchemy.orm import query
from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from api.mutations import resolve_create_user
from api.queries import resolve_user_authentication, resolve_user_profile
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

#initialized with the name of the type defined in the schema
mutation = ObjectType("Mutation")
query = ObjectType("Query")

# binds the user field of the mutation to our resolver function
mutation.set_field("createUser", resolve_create_user)

# binds the user field of the query to our resolver function
query.set_field("user", resolve_user_authentication)
query.set_field("user", resolve_user_profile)

# The load_schema_from_path takes the name oof the schema file
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code