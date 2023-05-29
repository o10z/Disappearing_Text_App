# import modules
from tkinter import *
import time


# Create a class for the DisappearingText application
class DisappearingText:
    def __init__(self):
        # Create the main window
        self.root = Tk()
        self.title = "Disappearing Text App"
        self.root.geometry("800x600")
        self.frame = Frame()
        self.running = False
        self.elapsed_time = 0

        # Create a label to display the text
        self.sample_label = Label(self.frame, text="Don't stop typing!!!", width=40, font=("Courier", 24))
        self.sample_label.grid(column=0, row=0, columnspan=2, padx=5, pady=10)

        # Create an entry widget for user input
        self.input_entry = Entry(self.frame, width=40, font=("Courier", 24))
        self.input_entry.grid(column=0, row=1, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        # Pack the frame and start the Tkinter event loop
        self.frame.pack(expand=True)
        self.root.mainloop()

    def count(self):
        # Check if the application is running
        if self.running:
            # Get the starting time
            start_time = time.time()
            self.elapsed_time = 0

            # Loop until the elapsed time reaches 5 seconds
            while self.elapsed_time < 5:
                # Calculate the elapsed time
                self.elapsed_time = time.time() - start_time
                # Update the root window to refresh the display
                self.root.update()
                # Pause the loop for a short duration
                time.sleep(0.1)
                # Check if the text needs to be cleared
                self.clear_text()

    def start(self, event):
        # Set the running flag to True when the user starts typing
        self.running = True
        # Start counting the elapsed time
        self.count()

    def clear_text(self):
        # Check if the elapsed time is greater than or equal to 5 seconds
        if self.elapsed_time >= 5:
            # Clear the text in the input entry widget
            self.input_entry.delete(0, END)


# An instance of the DisappearingText class to run the application
DisappearingText()
