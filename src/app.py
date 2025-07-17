"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "basketball": {
        "name": "Basketball Team",
        "description": "Join our competitive basketball team and represent Mergington High in tournaments.",
        "category": "Sports",
        "participants": []
    },
    "debate_club": {
        "name": "Debate Club",
        "description": "Develop your public speaking and critical thinking skills through competitive debates.",
        "category": "Academic",
        "participants": []
    },
    "drama_club": {
        "name": "Drama Club",
        "description": "Express yourself through acting, directing, and stage production.",
        "category": "Arts",
        "participants": []
    },
    "soccer": {
        "name": "Soccer Team",
        "description": "Join our varsity soccer team and compete in the regional league.",
        "category": "Sports",
        "participants": []
    },
    "tennis": {
        "name": "Tennis Team",
        "description": "Serve up some competition with our tennis team in singles and doubles matches.",
        "category": "Sports",
        "participants": []
    },
    "track_field": {
        "name": "Track and Field",
        "description": "Sprint, jump, and throw your way to victory in track and field events.",
        "category": "Sports",
        "participants": []
    },
    "art_club": {
        "name": "Art Club",
        "description": "Explore various artistic mediums including painting, drawing, and sculpture.",
        "category": "Arts",
        "participants": []
    },
    "music_band": {
        "name": "School Band",
        "description": "Play instruments and perform at school events and concerts.",
        "category": "Arts",
        "participants": []
    },
    "chess_club": {
        "name": "Chess Club",
        "description": "Master the game of chess through strategy sessions and tournaments.",
        "category": "Academic",
        "participants": []
    },
    "robotics": {
        "name": "Robotics Club",
        "description": "Build and program robots for competitions and STEM challenges.",
        "category": "Academic",
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
