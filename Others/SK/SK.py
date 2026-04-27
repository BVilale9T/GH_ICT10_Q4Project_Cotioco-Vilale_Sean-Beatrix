from pyscript import document, display
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

# Preload to avoid font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# Store data globally
all_months = []
all_absences = []

def Calculate(event):
    abs_value = document.getElementById("Absent").value
    day_value = document.getElementById("Months").value

    if not abs_value:
        document.getElementById("output").innerHTML = '<p style="color:red;">Please enter a number.</p>'
        return

    # Save data
    all_months.append(day_value)
    all_absences.append(int(abs_value))

    # Convert to NumPy array
    converted_absences = np.array(all_absences)

    # Clear previous plot
    plt.clf()

    # Create graph
    plt.plot(all_months, converted_absences, marker='o')
    plt.title("Topaz Absents")
    plt.xlabel("Month")
    plt.ylabel("Absences")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Clear output then display the figure into it
    document.getElementById("output").innerHTML = ""
    display(plt.gcf(), target="output", append=False)
