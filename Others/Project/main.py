from pyscript import document, display

#  Photo Caption Loader 
def show_captions():
    """Injects captions into the four photo Output elements on Project.html."""
    display(f"TLE project (2024-2025)",    target="Output1")
    display(f"Christmas party (2025-2026)", target="Output2")
    display(f"Teen talk (2024-2025)",       target="Output3")
    display(f"Intrams (2025-2026)",         target="Output4")

# Run immediately when the script loads so captions appear on page load
show_captions()