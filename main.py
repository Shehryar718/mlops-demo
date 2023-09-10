class Note:
    """
    This class represents a simple note.

    Attributes:
        title (str): The title of the note.
        content (str): The content or body of the note.
    """

    def __init__(self, title, content):
        """
        Initialize a Note instance with a title and content.

        Args:
            title (str): The title of the note.
            content (str): The content or body of the note.
        """
        self.title = title
        self.content = content

    def get_title(self):
        """
        Get the title of the note.

        Returns:
            str: The title of the note.
        """
        return self.title

    def get_content(self):
        """
        Get the content or body of the note.

        Returns:
            str: The content or body of the note.
        """
        return self.content

    def set_title(self, new_title):
        """
        Set a new title for the note.

        Args:
            new_title (str): The new title for the note.
        """
        self.title = new_title

    def set_content(self, new_content):
        """
        Set new content or body for the note.

        Args:
            new_content (str): The new content or body for the note.
        """
        self.content = new_content

    def display(self):
        """
        Display the title and content of the note.

        Returns:
            str: A formatted string containing the title and content of the note.
        """
        return f"Title: {self.title}\nContent: {self.content}"


if __name__ == "__main__":
    # Create a new note
    my_note = Note("Meeting Agenda", "Discuss project updates and plan for next sprint.")

    # Display the note
    print(my_note.display())

    # Modify the note
    my_note.set_content("Meeting rescheduled to 2:00 PM due to team availability.")

    # Display the modified note
    print(my_note.display())
