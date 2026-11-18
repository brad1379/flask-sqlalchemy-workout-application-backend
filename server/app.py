from flask import Flask, jsonify
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Workout Application Backend"

# Route to GET all exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = []
    exercise_query = Exercise.query.all()
    for ex in exercise_query:
        exercise_dict = {
            "id": ex.id, 
            "name": ex.name,
            "category": ex.category,
            "equipment_needed": ex.equipment_needed
        }
        exercises.append(exercise_dict)
    # return list of all exercises and status code 200 for success
    return jsonify(exercises), 200

# TODO: ADD EXERCISE
# POST - Route to add exercise
@app.route('/exercises', methods=['POST'])
def add_exercise():
    pass

# Route to GET an exercise by an ID
@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if exercise:
        exercise_dict = {
            "id": exercise.id, 
            "name": exercise.name,
            "category": exercise.category,
            "equipment_needed": exercise.equipment_needed
        }
        return jsonify(exercise_dict), 200
    else:
        error_message = {"error": f"Exercise id: {id} not found."}
        return jsonify(error_message), 404

# TODO: DELETE WORKOUT
# DELETE - Route to delete a workout
@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    pass

# Route to GET a exercise's workout 
@app.route('/exercises/<int:id>/workout', methods=['GET'])
def get_exercises_workout(id):
    pass
    
# Route to GET all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = []
    workout_query = Workout.query.all()
    for wkout in workout_query:
        workout_dict = {
            "id": wkout.id,
            "date": wkout.date,
            "duration_minutes": wkout.duration_minutes,
            "notes": wkout.notes,
        }
        workouts.append(workout_dict)
    # Return list of all workouts and status code 200 for success
    return jsonify(workouts, 200)

# TODO: ADD WORKOUT
# POST - Route to add workout
@app.route('/workouts', methods=['POST'])
def add_workout():
    pass

# Route to GET a workout by an ID
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout:
        workout_dict = {
            "id": workout.id, 
            "date": workout.date,
            "duration_minutes": workout.duration_minutes,
            "notes": workout.notes
        }
        return jsonify(workout_dict), 200
    else:
        error_message = {"error": f"Workout id: {id} not found."}
        return jsonify(error_message), 404

# TODO: DELETE WORKOUT
# DELETE - Route to delete a workout by an ID
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    pass

# TODO: ADD AN EXERCISE TO A WORKOUT
# POST - Route to add an exercise to a workout
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_workout_exercises(workout_id, exercise_id):
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)