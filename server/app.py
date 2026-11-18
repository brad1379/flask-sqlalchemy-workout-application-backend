from flask import Flask, make_response
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
@app.route('/exercises')
def get_exercises():
    pass

# POST - Route to add exercise
@app.route('/exercises')
def add_exercise():
    pass

# Route to GET an exercise by an ID
@app.route('/exercises/<int:id>')
def get_exercise(id):
    pass

# DELETE - Route to delete a workout
@app.route('/exercises/<int:id>')
def delete_exercise(id):
    pass

# Route to GET a exercise's workout 
@app.route('/exercises/<int:id>/workout')
def get_exercises_workout(id):
    pass
    
# Route to GET all workouts
@app.route('/workouts')
def get_workouts():
    pass

# POST - Route to add workout
@app.route('/workouts')
def add_workout():
    pass

# Route to GET a workout by an ID
@app.route('/workouts/<int:id>')
def get_workout(id):
    pass

# DELETE - Route to delete a workout by an ID
@app.route('/workouts/<int:id>')
def delete_workout(id):
    pass

# POST - Route to add an exercise to a workout
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises')
def add_workout_exercises(id):
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)