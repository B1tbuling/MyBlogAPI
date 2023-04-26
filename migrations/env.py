from alembic import context

from utils.db import Base, engine

from posts.models import Post, Tags, AssociationPostTags
from users.models import User


target_metadata = Base.metadata


def run_migrations_online() -> None:
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
