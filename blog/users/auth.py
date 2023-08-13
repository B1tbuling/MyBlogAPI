import config
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy


# cookie_transport = CookieTransport(cookie_max_age=3600)
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


SECRET = config.JWTConfig.SECRET


def get_jwt_strategy() -> JWTStrategy:  #  type: ignore
    return JWTStrategy(secret=SECRET, lifetime_seconds=2000000)


auth_backend = AuthenticationBackend(
    name="jwt",
    # transport=cookie_transport,
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
