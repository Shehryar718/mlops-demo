# Import the Note class from your module
from note import Note

def test_note_creation():
    # Create a new note
    my_note = Note("Meeting Agenda", "Discuss project updates and plan for the next sprint.")
    
    # Check if the title and content match
    assert my_note.get_title() == "Meeting Agenda"
    assert my_note.get_content() == "Discuss project updates and plan for the next sprint."

def test_note_modification():
    # Create a new note
    my_note = Note("Meeting Agenda", "Discuss project updates and plan for the next sprint.")
    
    # Modify the note
    my_note.set_title("Updated Meeting Agenda")
    my_note.set_content("Meeting rescheduled to 2:00 PM due to team availability.")
    
    # Check if the title and content are updated
    assert my_note.get_title() == "Updated Meeting Agenda"
    assert my_note.get_content() == "Meeting rescheduled to 2:00 PM due to team availability."
