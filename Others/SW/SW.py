from pyscript import document, display

#  Classmate Class 
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        """Returns a formatted introduction string for this classmate."""
        return (
            f"Hello, my name is {self.name}. "
            f"I am in section {self.section}, "
            f"and my favorite subject is {self.favorite_subject}."
        )
# Pre-loaded list of classmates shown when the page first loads
classmates = [
    Classmate("Bea",    "Topaz", "ICT"),
    Classmate("Sang",   "Topaz", "Science"),
    Classmate("Allen",  "Topaz", "ICT"),
    Classmate("Ramon",  "Topaz", "Science"),
    Classmate("Simran", "Topaz", "English"),
]

#  Show List Button Handler 
def show_list(event):
    """Clears the output area and displays all classmate introductions."""
    document.getElementById("output").innerHTML = ""  # clear previous output
    for mate in classmates:
        display(mate.introduce(), target="output")

#  Add Classmate Button Handler 
def add_classmate(event):
    """Reads input fields, validates them, creates a new Classmate, and appends it to the list."""
    # Read and trim whitespace from each input field
    name             = document.getElementById("Name").value.strip()
    section          = document.getElementById("Section").value.strip()
    favorite_subject = document.getElementById("FavoriteSubject").value.strip()

    # Validate: all fields must be filled in
    if not name or not section or not favorite_subject:
        display(
            "Fill in all the lines before adding a classmate.",
            target="output",
        )
        return

    # Create and store the new classmate
    new_mate = Classmate(name, section, favorite_subject)
    classmates.append(new_mate)
    display(f"Added: {new_mate.introduce()}", target="output")

    # Clear the input fields after a successful add
    document.getElementById("Name").value            = ""
    document.getElementById("Section").value         = ""
    document.getElementById("FavoriteSubject").value = ""