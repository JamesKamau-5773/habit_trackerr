"""Initial migration

Revision ID: a110e6eb9dfc
Revises: dc728c018dd7
Create Date: 2025-09-05 14:29:52.817193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a110e6eb9dfc'
down_revision: Union[str, None] = 'dc728c018dd7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
