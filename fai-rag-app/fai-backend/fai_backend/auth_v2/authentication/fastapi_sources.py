from fastapi.security import APIKeyHeader

from fai_backend.auth.security import access_security

api_key_source = APIKeyHeader(
    name='X-Api-Key',
    description='API Key. Can be created/revoked by an administrator.',
    auto_error=False
)

# bearer_token_source = HTTPBearer(
#     scheme_name='User Token',
#     description='JWT Token associated with an user. Generated by logging in.',
#     auto_error=False
# )

# TODO: don't use fastapi_jwt
bearer_token_source = access_security
