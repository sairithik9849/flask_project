import requests
import json

BASE = "http://127.0.0.1:5000"

# Test RegisterUser
response = requests.post(f"{BASE}/user", json={"name": "John Doe", "age": 30})
print("RegisterUser:")
print(response.status_code)
print(json.dumps(response.json(), indent=2))
print("///////////////////")

user_id = response.json()["id"]

# Test GetUser
response_get = requests.get(f"{BASE}/user/{user_id}")
print("GetUser:")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("///////////////////")

# Test AddWorkout
response_workout = requests.put(f"{BASE}/workouts/{user_id}", json={
    "date": "2024-11-28",
    "time": "30:00",
    "distance": "5km"
})
print("AddWorkout:")
print(response_workout.status_code)
print(json.dumps(response_workout.json(), indent=2))
print("///////////////////")

# Test ListWorkouts
response_list_workouts = requests.get(f"{BASE}/workouts/{user_id}")
print("ListWorkouts:")
print(response_list_workouts.status_code)
print(json.dumps(response_list_workouts.json(), indent=2))
print("///////////////////")

# Register another user to test FollowFriend and ShowFriendWorkouts
response_friend = requests.post(f"{BASE}/user", json={"name": "Jane Doe", "age": 25})
friend_id = response_friend.json()["id"]

# Test FollowFriend
response_follow = requests.put(f"{BASE}/follow-list/{user_id}", json={"follow_id": friend_id})
print("FollowFriend:")
print(response_follow.status_code)
print(json.dumps(response_follow.json(), indent=2))
print("///////////////////")

# Add a workout for the friend
requests.put(f"{BASE}/workouts/{friend_id}", json={
    "date": "2024-11-29",
    "time": "45:00",
    "distance": "10km"
})

# Test ShowFriendWorkouts
response_friend_workouts = requests.get(f"{BASE}/follow-list/{user_id}/{friend_id}")
print("ShowFriendWorkouts:")
print(response_friend_workouts.status_code)
print(json.dumps(response_friend_workouts.json(), indent=2))
print("///////////////////")

# Test RemoveUser
response_delete = requests.delete(f"{BASE}/user/{user_id}")
print("RemoveUser:")
print(response_delete.status_code)
if response_delete.status_code == 200:
    print("{} successfully deleted.".format(user_id))
else:
    print(json.dumps(response_delete.json(), indent=2))
print("///////////////////")

# Test ListUsers to see remaining users
response_list_users = requests.get(f"{BASE}/users")
print("ListUsers:")
print(response_list_users.status_code)
print(json.dumps(response_list_users.json(), indent=2))