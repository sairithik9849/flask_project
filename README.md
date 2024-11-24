# Strava Lite

## Project Information
- **GitHub Repository**: https://github.com/sairithik9849/flask_project
- **Name**: Sairithik Komuravelly
- **Stevens Email**: skomurav@stevens.edu
- **CWID**: 20029694

## Project Description
Strava Lite is a simplified run tracking server API. It allows users to register, manage accounts, record workouts, and interact with other users.

## Features
- User registration and management
- Workout tracking
- User following system

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `python app.py`
3. Server runs on `http://localhost:5000`

## Bugs and Issues Faced
1. Issue: Workouts displayed in GetUser and ListUsers endpoints.
   Resolution: Modified classes to return only required fields.

2. Issue: Handling edge cases in FollowFriend functionality.
   Resolution: Added checks to prevent self-following and non-existent user following.

3. Issue: Missing field handling in AddWorkout requests.
   Resolution: Implemented robust error checking for required fields.