from datetime import datetime, timezone
from marshmallow import Schema, fields
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

# Exercise Model
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    # Relationship mapping workout exercises to exercise
    workout_exercises = db.Relationship('WorkoutExercise', back_populates='exercise')

    # Association proxy to get workouts for an exercise through workout exercises
    workouts = association_proxy('workout_exercises', 'workout', creator=lambda workout_obj: WorkoutExercise(workout=workout_obj))

    # Validations
    @validates('name')
    def validate_name(self, key, name):
        if len(name) > 20:
            raise ValueError("Exercise name must be 20 characters or less.")
        return name

    @validates('category')
    def validate_category(self, key, category):
        if len(category) > 20:
            raise ValueError("Category must be 20 characters or less.")
        return category


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
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(256))

    # Relationship mapping workout exercises to workout
    workout_exercises = db.Relationship('WorkoutExercise', back_populates='workout')
 
    # Association proxy to get exercises for this workout through workout exercises
    exercises = association_proxy('workout_exercises', 'exercise', creator=lambda exercise_obj: WorkoutExercise(exercise=exercise_obj))

    # Validations
    @validates('date')
    # Convert date strings into valid datetime objects
    def validate_date(self, key, date):
        if date is None:
            raise ValueError("A date is required")
        if isinstance(date, str):
            try:
                date = datetime.fromisoformat(date)
            except:
                raise ValueError("Date must be a valid ISO datetime string.")
        return date

    @validates('duration_minutes')
    # Make sure the workout duration is between 15 mins and 4 hours.
    def validate_duration_minutes(self, key, duration_minutes):
        if duration_minutes < 5 or duration_minutes > 240:
            raise ValueError("Workout duration must be between 15 and 240 minutes.")
        return duration_minutes

    @validates('notes')
    def validate_notes(self, key, notes):
        if len(notes) > 256: 
            raise ValueError("Notes must be 256 characters or less.")
        return notes

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
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False)

    # Relationship mapping workout to workout exercises
    workout = db.Relationship('Workout', back_populates="workout_exercises")

    # Relationship mapping exercise to workout exercises
    exercise = db.Relationship('Exercise', back_populates="workout_exercises")

    # Validations
    @validates('reps')
    def validate_reps(self, key, reps):
        if reps < 1 or reps > 20:
            raise ValueError("Reps must be more than 1 or less than or equal to 20.")
        return reps

    @validates('sets')
    def validate_sets(self, key, sets):
        if sets < 1 or sets > 10:
            raise ValueError("Sets must be more than 1 or less than or equal to 10.")
        return sets

    @validates('duration_seconds')
    def validate_duration_seconds(self, key, duration_seconds):
        if duration_seconds < 1 or duration_seconds > 999:
            raise ValueError("Exercise duration must be more than 1 second or less than 999 seconds.")
        return duration_seconds


    def __repr__(self):
        return f'<WorkoutExercise {self.id}, {self.reps}, {self.sets}, {self.duration_seconds}>'

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

    