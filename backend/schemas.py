from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

#------Validação de Dados com Pydantic-----#

#----------------Habit---------------------#

class HabitBase(BaseModel):
    title: str
    description: str | None = None

class HabitCreate(HabitBase):
    pass

class Habit(HabitBase):
    id: UUID
    is_completed: bool
    created_at: datetime

    class Config:
        orm_mode = True

#-------------Milestone-------------------#

class MilestoneBase(BaseModel):
    habit_id: UUID
    target: int

class MilestoneCreate(MilestoneBase):
    pass

class Milestone(MilestoneBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

#--------------Reward----------------------#

class RewardBase(BaseModel):
    milestone_id: UUID
    title: str
    redeemed: bool = False

class RewardCreate(RewardBase):
    pass

class Reward(RewardBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True