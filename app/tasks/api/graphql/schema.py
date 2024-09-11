"""
This module defines the schema for the GraphQL API.
"""

import strawberry
from .queries import Query
from .mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
