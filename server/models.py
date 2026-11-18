from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from marshmallow import Schema, fields

db = SQLAlchemy()

# Exercise Model
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean)

    # Relationship mapping workout exercises to exercise
    workout_exercises = db.Relationship('WorkoutExercise', back_populates='exercise')

    # Association proxy to get workouts for an exercise through workout exercises
    workouts = association_proxy('workout_exercises', 'workout', creator=lambda workout_obj: WorkoutExercise(workout=workout_obj))

    def __repr__(self):
        return f'<Exercise {self.id}, {self.name}, {self.category}, {self.equipment_needed}>'

# Exercise Schema
class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    category = fields.Str()
    equipment_needed = fields.Boolean()

    workout_exercises = fields.List(fields.Nested(lambda: WorkoutExerciseSchema(exclude=("exercise",))))


# ================================================================================


# Workout Model
class Workout(db.Model):
    __tablename__ = 'workouts'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.String)

    # Relationship mapping workout exercises to workout
    workout_exercises = db.Relationship('WorkoutExercise', back_populates='workout')
 
    # Association proxy to get exercises for this workout through workout exercises
    exercises = association_proxy('workout_exercises', 'exercise', creator=lambda exercise_obj: WorkoutExercise(exercise=exercise_obj))

    def __repr__(self):
        return f'<Workout {self.id}, {self.date}, {self.duration_minutes}, {self.notes}>'

# Workout Schema
class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.DateTime()
    duration_minutes = fields.Int()
    notes = fields.Str()

    workout_exercises = fields.List(fields.Nested(lambda: WorkoutExerciseSchema(exclude=("exercise",))))


# ================================================================================
 

# WorkoutExercise Model
class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    # Relationship mapping workout to workout exercises
    workout = db.Relationship('Workout', back_populates="workout_exercises")

    # Relationship mapping exercise to workout exercises
    exercise = db.Relationship('Exercise', back_populates="workout_exercises")


# WorkoutExercise Schema   
class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()

    workout_id = fields.Int()
    exercise_id = fields.Int()

    workout = fields.Nested(WorkoutSchema(exclude=("workout_exercises",)))
    exercise = fields.Nested(ExerciseSchema(exclude=("workout_exercises",)))

 