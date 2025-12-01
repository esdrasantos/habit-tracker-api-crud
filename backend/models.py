from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from .database import Base


'''
    1. relationship() is useful for returning nested json.
    2. cascade="all, delete" ensures that milestones and rewards are deleted when the habit is deleted.
    3. it allows the usage of habit.milestones, etc.
'''

class Habit(Base):
    __tablename__ = "habits"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    milestones = relationship("Milestone", back_populates="habit", cascade="all, delete")

class Milestone(Base):
    __tablename__ = "milestones"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    habit_id = Column(UUID(as_uuid=True), ForeignKey("habits.id"), nullable=False)
    target = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    habit = relationship("Habit", back_populates="milestones")
    rewards = relationship("Reward", back_populates="milestones", cascade="all, delete")

class Reward(Base):
    __tablename__ = "rewards"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    milestone_id = Column(UUID(as_uuid=True), ForeignKey("milestones.id"), nullable=False)
    title = Column(String, nullable=False)
    redeemed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    milestone = relationship("Milestone", back_populates="rewards")