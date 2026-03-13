from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    # Find the current maximum ID in the list and increment by 1 to create a unique ID.
    new_event_id = max((e for e in events if e.id == id), default=0) + 1
    new_event = Event(id=new_event_id, title=data['title'])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201


# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()
    event_to_update = next((e for e in events if e.id == event_id), None)
    if not event_to_update:
        return ("Event to update not found", 404)
    if "title" in data:
        event_to_update.title = data['title']
    return jsonify(event_to_update.to_dict()), 200


# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    #use global to allow modification of the global 'events' variable from inside this function
    global events
    #find the event id of the event we want to delete
    event_to_delete = next((e for e in events if e.id == event_id),None)
    if not event_to_delete:
        return ("Events not found", 404)
    #filter the list to exclude the specified ID (effectively deleting it)
    events = [e for e in events if e.id != event_id]
    #204 for successful deleted event
    return ("Event deleted succeffuly", 204)

if __name__ == "__main__":
    app.run(debug=True)
