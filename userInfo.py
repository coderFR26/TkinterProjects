from tkinter import *

def submit():
    first_name = fname_entry.get()
    last_name = lname_entry.get()
    age = age_entry.get()
    degree = degree_entry.get()
    job = job_entry.get()

    userInformation = {
                        'first_name':first_name,
                        'last_name':last_name,
                        'age': age,
                        'degree': degree,
                        'job': job
    }

    with open('userInformation.txt', 'w') as f:
        for date in userInformation:
            f.write(f'{date} :{userInformation[date]}\n')

window = Tk()

frame = Frame(window, bg='#7cc1cc', background='#7cc1cc')
frame.pack(fill=BOTH, expand=True)

#first name
fname_label = Label(frame, text="First Name: ", font=("Monotype Corsiva", 25), bg='#7cc1cc')
fname_label.grid(row=0, column=0, padx=5, pady=5)

fname_entry = Entry(frame, font=("Monotype Corsiva", 23), fg='red', bg='#7cc1cc')
fname_entry.grid(row=0, column=1, padx=5, pady=5)

#last name
lname_label = Label(frame, text="Last Name: ", font=("Monotype Corsiva", 25), bg='#7cc1cc')
lname_label.grid(row=1, column=0, padx=5, pady=5)

lname_entry = Entry(frame, font=("Monotype Corsiva", 23), fg='red', bg='#7cc1cc')
lname_entry.grid(row=1, column=1, padx=5, pady=5)

#age
age_label = Label(frame, text="age: ", font=("Monotype Corsiva", 25), bg='#7cc1cc')
age_label.grid(row=2, column=0, padx=5, pady=5)

age_entry = Entry(frame, font=("Monotype Corsiva", 23), fg='red', bg='#7cc1cc')
age_entry.grid(row=2, column=1, padx=5, pady=5)

#degree
degree_label = Label(frame, text="degree: ", font=("Monotype Corsiva", 25), bg='#7cc1cc')
degree_label.grid(row=3, column=0, padx=5, pady=5)

degree_entry = Entry(frame, font=("Monotype Corsiva", 23), fg='red', bg='#7cc1cc')
degree_entry.grid(row=3, column=1, padx=5, pady=5)

#job
job_label = Label(frame, text="occupation: ", font=("Monotype Corsiva", 25), bg='#7cc1cc')
job_label.grid(row=4, column=0, padx=5, pady=5)

job_entry = Entry(frame, font=("Monotype Corsiva", 23), fg='red', bg='#7cc1cc')
job_entry.grid(row=4, column=1, padx=5, pady=5)


#submit button
submit_button = Button(window, text="Submit", font=('Monotype Corsiva', 25), fg='red', bg='#7cc1cc',
                       command=submit, width=10, relief=RAISED)
submit_button.pack(side=BOTTOM, fill=X)

window.mainloop()