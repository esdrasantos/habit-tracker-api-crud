from sqlalchemy.orm import Session
from . import models, schemas

# HabitCreate is for pydantic data validation
def create_habit(db: Session, habit: schemas.HabitCreate):
    db_habit = models.Habit(title=habit.title, description=habit.description)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit