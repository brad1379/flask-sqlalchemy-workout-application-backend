# Workout Application Backend

## Description

This is a Flask backend API for a workout tracking app. It uses Flask-SQLAlchemy with a SQLite database to keep track of workouts, exercises, and the exercises done in each workout.

There are three models:

- **Exercise** - an exercise with a name, category, and whether it needs equipment
- **Workout** - a workout with a date, duration in minutes, and notes
- **WorkoutExercise** - the join table between workouts and exercises. It also stores the reps, sets, and duration in seconds for that exercise in that workout

### Relationships

- A WorkoutExercise belongs to a Workout
- A WorkoutExercise belongs to an Exercise
- A Workout has many WorkoutExercises
- An Exercise has many WorkoutExercises
- A Workout has many Exercises through WorkoutExercises
- An Exercise has many Workouts through WorkoutExercises

## Installation

1. Clone the repo and cd into it:

```bash
git clone <repo-url>
cd flask-sqlalchemy-workout-application-backend
```

2. Install the dependencies and start the virtual environment:

```bash
pipenv install
pipenv shell
```

3. Move into the server folder:

```bash
cd server
```

4. Run the migrations to create the database:

```bash
flask db upgrade head
```

5. Seed the database with example data:

```bash
python seed.py
```

## Running the App

From inside the `server` folder, run:

```bash
flask run
```

The API will be running at `http://127.0.0.1:5000`.

You can also run it with `python app.py`, which runs on port 5555 with debug mode on.

## Endpoints

### Exercises

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/exercises` | Returns a list of all exercises |
| GET | `/exercises/<id>` | Returns one exercise by its id. Returns a 404 error if it is not found |
| POST | `/exercises` | Creates a new exercise |
| DELETE | `/exercises/<id>` | Deletes an exercise by its id. Returns a 404 error if it does not exist |
| GET | `/exercises/<id>/workout` | Returns all the workouts that include this exercise |

Example POST body for `/exercises`:

```json
{
  "name": "Push Up",
  "category": "Chest",
  "equipment_needed": false
}
```

### Workouts

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/workouts` | Returns a list of all workouts |
| GET | `/workouts/<id>` | Returns one workout by its id. Returns a 404 error if it is not found |
| POST | `/workouts` | Creates a new workout |
| DELETE | `/workouts/<id>` | Deletes a workout by its id. Returns a 404 error if it does not exist |

Example POST body for `/workouts`:

```json
{
  "date": "2026-11-10T08:00:00",
  "duration_minutes": 45,
  "notes": "Leg day"
}
```

### Workout Exercises

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Adds an exercise to a workout with reps, sets, and duration |

Example POST body:

```json
{
  "reps": 10,
  "sets": 3,
  "duration_seconds": 60
}
```

## Validations

- Exercise `name` and `category` can't be blank and must be 20 characters or less
- Workout `date` is required and must be a valid ISO date string
- Workout `duration_minutes` must be between 15 and 240
- Workout `notes` must be 256 characters or less
- WorkoutExercise `reps` must be between 1 and 20
- WorkoutExercise `sets` must be between 1 and 10
- WorkoutExercise `duration_seconds` must be between 1 and 999
