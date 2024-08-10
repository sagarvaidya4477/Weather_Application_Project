from tkinter import *
from tkinter import messagebox
from Database import DB
from Api import Api

class NLPapp:
    def __init__(self):
        self.api = Api()
        self.dbo = DB()
        self.root = Tk()
        self.root.title("Weather Application")
        self.root.geometry('400x600')
        self.root.configure(bg="#2C3E50")  # Dark blue background
        self.login_gui()
        self.root.mainloop()

    def clear(self):
        """Clear all widgets from the root window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def toggle_password(self):
        """Toggle password visibility."""
        if self.password_input.cget('show') == '*':
            self.password_input.config(show='')
        else:
            self.password_input.config(show='*')

    def login_gui(self):
        """Render the login GUI."""
        self.clear()
        heading = Label(self.root, text='Weather Application', bg='#2C3E50', fg='#ECF0F1', font=('Arial', 24, 'bold'))
        heading.pack(pady=(50, 20))

        email_label = Label(self.root, text="Email", bg="#3498DB", fg='white', font=("Arial", 14))
        email_label.pack(pady=(10, 5))

        self.email_input = Entry(self.root, width=30, font=("Arial", 14))
        self.email_input.pack(pady=(5, 20), ipady=5, padx=10)

        password_label = Label(self.root, text="Password", bg="#3498DB", fg="white", font=("Arial", 14))
        password_label.pack(pady=(10, 5))

        self.password_input = Entry(self.root, width=30, show="*", font=("Arial", 14))
        self.password_input.pack(pady=(5, 20), ipady=5, padx=10)

        self.show_password_var = IntVar()
        show_password_check = Checkbutton(self.root, text="Show Password", variable=self.show_password_var,
                                          command=self.toggle_password, bg="#2C3E50", fg="white", selectcolor="#2C3E50", font=("Arial", 12))
        show_password_check.pack(pady=(5, 20))

        login_btn = Button(self.root, text="Login", width=15, command=self.perform_login, bg="#27AE60", fg='white', font=("Arial", 14, "bold"))
        login_btn.pack(pady=(10, 5))

        member_login = Label(self.root, text="Not a member?", bg="#2C3E50", fg="white", font=("Arial", 14))
        member_login.pack(pady=(20, 10))

        register_btn = Button(self.root, text="Register", width=15, command=self.register, bg="#E74C3C", fg='white', font=("Arial", 14, "bold"))
        register_btn.pack(pady=(5, 20))

    def perform_login(self):
        """Handle login functionality."""
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.check_login(email, password)

        if response == 1:
            messagebox.showinfo(title="Success", message="Login successful")
            self.home()
        elif response == 0:
            messagebox.showerror(title="Failed", message="Incorrect password")
        else:
            messagebox.showwarning(title="Failed", message="Email not registered")

    def home(self):
        """Render the home page GUI."""
        self.clear()
        heading = Label(self.root, text='Weather Application', bg='#2C3E50', fg='#ECF0F1', font=('Arial', 24, 'bold'))
        heading.pack(pady=(50, 75))

        search_by_city_btn = Button(self.root, text="Search by city name", width=20, height=2, command=self.using_city_name, bg="#3498DB", fg='white', font=("Arial", 18, "bold"))
        search_by_city_btn.pack(pady=(5, 5))

        search_by_coordinates_btn = Button(self.root, text="Search by coordinates", width=20, height=2, command=self.using_coordinates, bg="#3498DB", fg='white', font=("Arial", 18, "bold"))
        search_by_coordinates_btn.pack(pady=(50, 50))

        logout_btn = Button(self.root, text="Logout", width=20, height=1, command=self.login_gui, bg="#E74C3C", fg='white', font=("Arial", 12, "bold"))
        logout_btn.pack(pady=(25, 5))

    def using_city_name(self):
        """Render the city name search page."""
        self.clear()
        heading = Label(self.root, text='Weather Application', bg='#2C3E50', fg='#ECF0F1', font=('Arial', 24, 'bold'))
        heading.pack(pady=(20, 5))

        city_label = Label(self.root, text="Enter city name", bg='#2C3E50', fg='#ECF0F1', font=("Arial", 12, "italic"))
        city_label.pack(pady=(5, 25))

        self.city_input = Entry(self.root, width=25, font=("Arial", 12))
        self.city_input.pack(pady=(5, 5), ipady=1, padx=10)

        search_by_city_btn = Button(self.root, text="Search", width=10, command=self.display_info, bg="#27AE60", fg="white", font=("Arial", 12, "bold"))
        search_by_city_btn.pack(pady=(5, 5))

        self.result = Text(self.root, width=40, height=15, wrap=WORD, bg='#2C3E50', fg='#ECF0F1')
        self.result.configure(font=("Cambria", 12, "italic"))
        self.result.pack(pady=(5, 5))

        back_btn = Button(self.root, text="Back", width=10, command=self.home, bg="#E74C3C", fg="white", font=("Arial", 12, "bold"))
        back_btn.pack(pady=(5, 5))

    def using_coordinates(self):
        """Render the coordinates search page."""
        self.clear()
        heading = Label(self.root, text='Weather Application', bg='#2C3E50', fg='#ECF0F1', font=('Arial', 24, 'bold'))
        heading.pack(pady=(20, 5))

        lat_label = Label(self.root, text="Enter Latitude", bg='#2C3E50', fg='#ECF0F1', font=("Arial", 12, "italic"))
        lat_label.pack(pady=(5, 5))

        self.lat_input = Entry(self.root, width=25, font=("Arial", 12))
        self.lat_input.pack(pady=(5, 5), ipady=1, padx=10)

        lon_label = Label(self.root, text="Enter Longitude", bg='#2C3E50', fg='#ECF0F1', font=("Arial", 12, "italic"))
        lon_label.pack(pady=(5, 5))

        self.lon_input = Entry(self.root, width=25, font=("Arial", 12))
        self.lon_input.pack(pady=(5, 5), ipady=1, padx=10)

        search_by_coordinates_btn = Button(self.root, text="Search", width=10, command=self.search_by_coordinates, bg="#27AE60", fg="white", font=("Arial", 12, "bold"))
        search_by_coordinates_btn.pack(pady=(5, 5))

        back_btn = Button(self.root, text="Back", width=10, command=self.home, bg="#E74C3C", fg="white", font=("Arial", 12, "bold"))
        back_btn.pack(pady=(5, 5))

    def display_info(self):
        """Display weather information."""
        city = self.city_input.get()
        data = self.api.get_info_by_city_name(city)

        self.result.configure(font=("Cambria", 12, "italic"))  # Reset the font style

        if "error" in data:
            self.result.config(state=NORMAL)
            self.result.delete(1.0, END)
            self.result.insert(END, data["error"], ('error',))
            self.result.config(state=DISABLED)
        else:
            self.result.config(state=NORMAL)  # Allow text editing
            self.result.delete(1.0, END)  # Clear previous content

            # Insert weather data with different styles
            self.result.insert(END, "Weather Information:\n", ('heading',))
            self.result.insert(END, f"City: {city}\n", ('info',))
            self.result.insert(END, f"Current Temperature: {data['current_temperature']}\n", ('temperature',))
            self.result.insert(END, f"Weather: {data['weather']}\n", ('info',))
            self.result.insert(END, f"Humidity: {data['humidity']}\n", ('info',))
            self.result.insert(END, f"Sunrise: {data['sunrise']}\n", ('info',))
            self.result.insert(END, f"Sunset: {data['sunset']}\n", ('info',))
            self.result.insert(END, f"Country: {data['country']}\n", ('info',))

            # Configure text styles
            self.result.tag_configure('heading', font=("Cambria", 14, "bold"), foreground="#ECF0F1")
            self.result.tag_configure('info', font=("Cambria", 12, "italic"), foreground="#BDC3C7")
            self.result.tag_configure('temperature', font=("Cambria", 12, "bold"), foreground="#E74C3C")
            self.result.tag_configure('error', font=("Cambria", 12, "italic"), foreground="#E74C3C")

            self.result.config(state=DISABLED)  # Make the text read-only

    def register(self):
        """Render the registration page."""
        self.clear()
        heading = Label(self.root, text='Weather Application', bg='#2C3E50', fg='#ECF0F1', font=('Arial', 24, 'bold'))
        heading.pack(pady=(50, 20))

        username_label = Label(self.root, text="Username", bg="#3498DB", fg='white', font=("Arial", 14))
        username_label.pack(pady=(10, 5))

        self.username_input = Entry(self.root, width=30, font=("Arial", 14))
        self.username_input.pack(pady=(5, 20), ipady=5, padx=10)

        email_label = Label(self.root, text="Email", bg="#3498DB", fg='white', font=("Arial", 14))
        email_label.pack(pady=(10, 5))

        self.email_input = Entry(self.root, width=30, font=("Arial", 14))
        self.email_input.pack(pady=(5, 20), ipady=5, padx=10)

        password_label = Label(self.root, text="Password", bg="#3498DB", fg="white", font=("Arial", 14))
        password_label.pack(pady=(10, 5))

        self.password_input = Entry(self.root, width=30, show="*", font=("Arial", 14))
        self.password_input.pack(pady=(5, 20), ipady=5, padx=10)

        register_btn = Button(self.root, text="Register", width=15, command=self.perform_registration, bg="#E74C3C", fg='white', font=("Arial", 14, "bold"))
        register_btn.pack(pady=(10, 5))

        member_login = Label(self.root, text="Already a member?", bg="#2C3E50", fg="white", font=("Arial", 14))
        member_login.pack(pady=(20, 10))

        login_btn = Button(self.root, text="Login", width=15, command=self.login_gui, bg="#27AE60", fg='white', font=("Arial", 14, "bold"))
        login_btn.pack(pady=(5, 20))

    def perform_registration(self):
        """Handle user registration."""
        username = self.username_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(username, email, password)

        if response == 1:
            messagebox.showinfo(title="Success", message="Registration successful")
        elif response == 0:
            messagebox.showerror(title="Failed", message="Email already exists")
        else:
            messagebox.showwarning(title="Error", message="Something went wrong, please try again later")

if __name__ == "__main__":
    NLPapp()
