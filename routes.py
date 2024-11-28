from flask_restful import Api
from api import *

base_route = "/user"
user_id = "/user/<string:user_id>"
workouts_user_id = "/workouts/<string:user_id>"
follow = "/follow-list/<string:user_id>"

routes = {
    RegisterUser: base_route,
    GetUser: user_id,
    RemoveUser: user_id,
    ListUsers: "/users",
    AddWorkout: workouts_user_id,
    ListWorkouts: workouts_user_id,
    FollowFriend: follow,
    ShowFriendWorkouts: f"{follow}/<string:follow_id>"
}

methods = {
    RegisterUser: "POST",
    GetUser: "GET",
    RemoveUser: "DELETE",
    ListUsers: "GET",
    AddWorkout: "PUT",
    ListWorkouts: "GET",
    FollowFriend: "PUT",
    ShowFriendWorkouts: "GET"
}

def init_routes(api):
    for [api_name,route] in routes.items():
        api.add_resource(api_name,routes[api_name],methods=[methods[api_name]])