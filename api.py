from flask_restful import Resource, reqparse
from uuid import uuid4

users = {}

register_new_user_parser = reqparse.RequestParser().add_argument("name",type=str,required=True).add_argument("age",type=int,required=False)

class RegisterUser(Resource):
    def post(self):
        name,age = register_new_user_parser.parse_args().values()
        id = str(uuid4())
        users[id] = {
            "id": id, "name": name, "age": age
        }
        return users[id], 200

class GetUser(Resource):
    def get(self,user_id):
        user = users.get(user_id)
        if user is None:
            return {"Message": "There is no user with the specified id"}
        return {
            "id": user["id"],
            "name": user["name"],
            "age": user["age"]
        }, 200

class RemoveUser(Resource):
    def delete(self,user_id):
        if user_id in users:
            del users[user_id]
            return {}, 200
        return {"Message": "There is no user with the specified id"}

class ListUsers(Resource):
    def get(self):
        user_list = [
            {
                "id": user["id"],
                "name": user["name"],
                "age": user["age"]
            }
            for user in users.values()
        ]
        return {"users": user_list}, 200    

AddWorkout_parser = reqparse.RequestParser().add_argument("date",type=str,required=True).add_argument("time",type=str,required=True).add_argument("distance",type=str,required=True)
class AddWorkout(Resource):
    def put(self,user_id):
        date,time,distance = AddWorkout_parser.parse_args().values()
        user = users.get(user_id)
        if user is None:
            return {"Message": "There is no user with the specified id"}, 404
        if date is not None and time is not None and distance is not None:
            new_workout = {
                "date": date,
                "time": time,
                "distance": distance
            }
            if "workouts" not in user:
                user["workouts"] = []
            user["workouts"].append(new_workout)
            return new_workout, 200
        else:
            return {"Message": "Missing required fields"}, 400

class ListWorkouts(Resource):
    def get(self,user_id):
        user = users.get(user_id)
        if user is None:
            return {"Message": "There is no user with the specified id"}, 404
        workouts = user.get("workouts", [])
        return {"workouts": [{"date": workout["date"],"distance": workout["distance"],"time": workout["time"]} for workout in workouts]}, 200

# Work on Extra Credit --
FollowFriend_parser = reqparse.RequestParser().add_argument("follow_id",type=str,required=True)
class FollowFriend(Resource):
    def put(self,user_id):
        user = users.get(user_id)
        follow_id = FollowFriend_parser.parse_args()["follow_id"]
        follow = users.get(follow_id)
        if user is None or follow is None:
            return {"Message": "There is no user with the specified id"}, 404
        if "following" not in users[user_id]: users[user_id]["following"] = set()
        users[user_id]["following"].add(follow_id)
        return {"following": list(map(str,users[user_id]["following"]))}, 200

class ShowFriendWorkouts(Resource):
    def get(self,user_id,follow_id):
        user = users.get(user_id)
        follow = users.get(follow_id)
        if user is None or follow is None: 
            return {"Message": "There is no user with the specified id"}, 404
        if "following" not in users[user_id] or follow_id not in users[user_id]["following"]:
            return {"Message": "You are not following the specified user!"}, 403
        friend_workouts = users[follow_id].get("workouts", [])
        response = {
            "workouts": [
                {
                    "date": workout["date"],
                    "distance": workout["distance"],
                    "time": workout["time"]
                }
                for workout in friend_workouts
            ]
        }
        return response, 200