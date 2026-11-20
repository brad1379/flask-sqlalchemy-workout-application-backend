#!/usr/bin/env python3

from app import app
from models import *
import datetime

with app.app_context():

	# reset data and add new example data, committing to db 
	Workout.query.delete()
	Exercise.query.delete()
	WorkoutExercise.query.delete()

	# Create exercises
	exercise1 = Exercise(name="Lat pull down", category="Back", equipment_needed=True)
	exercise2 = Exercise(name="Bench Press", category="Chest", equipment_needed=True)
	exercise3 = Exercise(name="Squat", category="Legs", equipment_needed=False)
	exercise4 = Exercise(name="Bicep Curl", category="Arms", equipment_needed=True)
	exercise5 = Exercise(name="Crunch", category="Abs", equipment_needed=False)
	exercise6 = Exercise(name="Test", category="TEST", equipment_needed=False)
	db.session.add_all([exercise1, exercise2, exercise3, exercise4, exercise5, exercise6])
	db.session.commit()

	# Create Workouts
	workout1 = Workout(date=datetime.datetime(2026, 11, 6), duration_minutes=65, notes="Workout went really well. I feel refreshed")
	workout2 = Workout(date=datetime.datetime(2026, 10, 21), duration_minutes=15, notes="Workout was short today, but at least I go something in!")
	workout3 = Workout(date=datetime.datetime(2026, 10, 23), duration_minutes=90, notes="Long workout today, had to make up for the other day!")
	workout4 = Workout(date=datetime.datetime(9999, 1, 1), duration_minutes=120, notes="TEST")
	db.session.add_all([workout1, workout2, workout3, workout4])
	db.session.commit()

	# Create WorkoutExercises
	workex1 = WorkoutExercise(workout_id=1, exercise_id=1, reps=10, sets=4, duration_seconds=30)
	workex2 = WorkoutExercise(workout_id=1, exercise_id=4, reps=10, sets=4, duration_seconds=60)
	workex3 = WorkoutExercise(workout_id=3, exercise_id=2, reps=12, sets=3, duration_seconds=20)
	workex4 = WorkoutExercise(workout_id=2, exercise_id=5, reps=20, sets=5, duration_seconds=45)
	workex5 = WorkoutExercise(workout_id=3, exercise_id=3, reps=5, sets=5, duration_seconds=90)
	db.session.add_all([workex1, workex2, workex3, workex4, workex5])
	db.session.commit()

