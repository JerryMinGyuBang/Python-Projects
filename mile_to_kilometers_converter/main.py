from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Label
label = Label(text="Miles")
label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()