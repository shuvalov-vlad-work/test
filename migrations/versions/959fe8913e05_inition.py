"""inition

Revision ID: 959fe8913e05
Revises: 76d99ee6cd85
Create Date: 2024-07-20 12:19:04.498309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '959fe8913e05'
down_revision: Union[str, None] = '76d99ee6cd85'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
