"""fias

Revision ID: a57262046435
Revises: 113975606318
Create Date: 2024-07-20 14:50:10.520827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a57262046435'
down_revision: Union[str, None] = '113975606318'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
