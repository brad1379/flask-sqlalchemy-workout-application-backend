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

# Route to get all exercises
@app.route('/exercises')
def get_exercises():
    pass

# Route to get an exercise by an ID
@app.route('/exercises/<int:id>')
def get_exercise(id):
    pass

# Route to get a exercise's workout 
@app.route('/exercises/<int:id>/workout')
def get_exercises_workout(id):
    pass
    
# Route to get all workouts
@app.route('/workouts')
def get_workouts():
    pass

# Route to get an workout by an ID
@app.route('/workouts/<int:id>')
def get_workout(id):
    pass

# Route to get a workout's exercises 
@app.route('/workouts/<int:id>/exercises')
def get_workout_exercises(id):
    pass


if __name__ == '__main__':
    app.run(port=5555, debug=True)