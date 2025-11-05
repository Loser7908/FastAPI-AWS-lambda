import uuid
from app.db import table
from app.models import NoteIn

def create_note(note: NoteIn):
    note_id = str(uuid.uuid4())
    item = {"id": note_id, "title": note.title, "content": note.content}
    table.put_item(Item=item)
    return item

def get_all_notes():
    response = table.scan()
    return response.get("Items", [])

def get_note(note_id: str):
    response = table.get_item(Key={"id": note_id})
    return response.get("Item")

def update_note(note_id: str, note: NoteIn):
    response = table.update_item(
        Key={"id": note_id},
        UpdateExpression="set title = :t, content = :c",
        ExpressionAttributeValues={":t": note.title, ":c": note.content},
        ReturnValues="ALL_NEW"
    )
    return response.get("Attributes")

def delete_note(note_id: str):
    response = table.delete_item(
        Key={"id": note_id},
        ReturnValues="ALL_OLD"
    )
    return "Attributes" in response
