"""Revision file template for Alembic.

This file is a minimal version of Alembic's default `script.py.mako` used
when generating revision files with `alembic revision --autogenerate`.
"""
from alembic import op
import sqlalchemy as sa

## revision identifiers, used by Alembic.
revision = '${up_revision}'
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    """Upgrade operations go here."""
    ${upgrades or 'pass'}


def downgrade():
    """Downgrade operations go here."""
    ${downgrades or 'pass'}
