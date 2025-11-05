from fastapi import FastAPI, HTTPException
from mangum import Mangum
from app.models import Note, NoteIn
from app.crud import create_note, get_all_notes, get_note, update_note, delete_note

app = FastAPI(title="Serverless Notes API")
handler = Mangum(app)


@app.get("/serverless-notes-api")
def root_alias():
    return {"message": "Serverless Notes API is running!2"}

@app.get("/")
def root():
    return {"message": "Serverless Notes API is running!"}

@app.get("/serverless-notes-api/notes")
def list_notes():
    return get_all_notes()

@app.post("/serverless-notes-api/notes")
def add_note(note: NoteIn):
    return create_note(note)

@app.get("/serverless-notes-api/notes/{note_id}")
def fetch_note(note_id: str):
    note = get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.put("/serverless-notes-api/notes/{note_id}")
def edit_note(note_id: str, note: NoteIn):
    updated = update_note(note_id, note)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated

@app.delete("/serverless-notes-api/notes/{note_id}")
def remove_note(note_id: str):
    success = delete_note(note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}
