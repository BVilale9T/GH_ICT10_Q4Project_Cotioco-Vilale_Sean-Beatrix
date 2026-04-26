from pyscript import document
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Use non-interactive backend (required for browser/PyScript)
import matplotlib.pyplot as plt

# Generate Graph Button Handler
def Calculate(event):
    """Reads the absence count and month, then generates and displays a line chart."""

    # Clear any previously generated output
    document.getElementById("output").innerHTML = ""

    # Get values from the input fields
    abs_value = document.getElementById("Absent").value
    day_value = document.getElementById("Months").value

    # Validate: absence field must not be empty
    if not abs_value:
        document.getElementById("output").innerHTML = '<p style="color:red;">Please enter a number.</p>'
        return

    # Wrap values in numpy arrays (required for matplotlib plotting)
    missing = np.array([int(abs_value)])  # number of absences
    days    = np.array([str(day_value)])  # selected month label

    # Build the line chart
    plt.plot(days, missing, marker="o")
    plt.title("Topaz Absents")
    plt.xlabel("Month")
    plt.ylabel("Absences")

    # Save chart to a file, then close to free memory
    plt.savefig("chart.png")
    plt.close()

    # Inject the saved chart image into the output div
    document.getElementById("output").innerHTML = (
        '<img src="chart.png" style="max-width:100%;">'
    )