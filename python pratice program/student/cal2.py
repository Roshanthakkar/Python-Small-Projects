# importing all files from the tkinter
from tkinter import *
# importing calendar module
import calendar

# Function for showing the calendar of the given year
def showCal() :

    # Create a GUI window
    root= Tk()
    # Set the background colour of GUI window
    root.config(background = "white")
    # set the name of tkinter GUI window
    root.title("MY CALENDAR")
    # Set the configuration of GUI window
    root.geometry("650x700")
    # using constructor int() we are type casting the string text that we through get() method
    fetch_year = int(year_field.get())
    # calendar() method of calendar module returns the calendar of the given year .
    cal_data = calendar.calendar(fetch_year)

    # Create a label for showing the content of the calender
    cal_year = Label(root, text = cal_data, font = "Lucida 10 bold")

    # grid() method is used for placing the widgets at respective positions in table i.e 2-D like structure
    cal_year.grid(row = 7, column = 1, padx = 20,)

    # start the GUI
    root.mainloop()


# Driver Code:
#this mechanism ensures,the main function is executed only as direct run not when imported as module.
if __name__ == "__main__" :

    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background = "light pink")

    # set the name of tkinter GUI window
    gui.title("CALENDAR")

    # Set the configuration of GUI window
    gui.geometry("250x250")

    # Create a CALENDAR : label with specified font and size
    cal = Label(gui, text = "CALENDAR",bg="red",font = ("times", 28, 'bold'))

    # Create a Enter Year : label
    year = Label(gui, text = "Enter Year", bg = "light green")

    # Create a text entry box for filling or typing the information.
    year_field = Entry(gui)

    # Create a Show Calendar Button and attached to showCal function
    Show = Button(gui, text = "Show Calendar", fg = "Black",
                              bg = "Red", command = showCal)

    # Create a Exit Button and attached to exit function
    Exit = Button(gui, text = "Exit", bg = "Red", command = exit)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row = 1, column = 1)

    year.grid(row = 2, column = 1)

    year_field.grid(row = 3, column = 1)

    Show.grid(row = 4, column = 1)

    Exit.grid(row = 6, column = 1)

    # start the GUI
    gui.mainloop()