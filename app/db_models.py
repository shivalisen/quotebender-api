import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Episode(db.Model):
  name: so.Mapped[str] = so.mapped_column(sa.String(50), primary_key=True)
  number: so.Mapped[int]
  season_number: so.Mapped[int]

  quotes: so.Mapped[list['Quote']] = so.relationship(
    back_populates='episode', lazy='joined'
  )

  __tablename__ = 'episodes'
  __table_args__ = (
    sa.Index('ix_season_episode', 'season_number', 'number'),
  )

class Quote(db.Model):
  id: so.Mapped[int] = so.mapped_column(primary_key=True)
  quote: so.Mapped[str] = so.mapped_column(sa.Text)
  character: so.Mapped[str] = so.mapped_column(sa.String(25), index=True)
  episode_name: so.Mapped[str] = so.mapped_column(sa.String(50), sa.ForeignKey(Episode.name))

  episode: so.Mapped[Episode] = so.relationship(back_populates='quotes', lazy='joined')

  __tablename__ = 'quotes'