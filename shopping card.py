import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.master.title("Login")

        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy login check
        if username == "user" and password == "password":
            self.master.destroy()
            self.app.show_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

class ECommerceApp:
    def __init__(self, master):
        self.master = master
        self.master.title("E-Commerce Shopping App")
        self.logged_in = False

        self.login_window = LoginWindow(tk.Toplevel(), self)

        self.products = [
            {"name": "Laptop", "price": 1000.00, "description": "Powerful laptop for all your computing needs."},
            {"name": "Smartphone", "price": 700.00, "description": "Latest smartphone with advanced features."},
            {"name": "Headphones", "price": 50.00, "description": "High-quality headphones for immersive audio experience."},
            {"name": "Smart Watch", "price": 150.00, "description": "Smart wearable device for tracking fitness and notifications."}
        ]

    def show_app(self):
        self.logged_in = True
        self.master.deiconify()

        self.product_frame = tk.Frame(self.master)
        self.product_frame.pack(padx=10, pady=10)

        tk.Label(self.product_frame, text="Product").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.product_frame, text="Price").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.product_frame, text="Description").grid(row=0, column=2, padx=10, pady=5)

        for i, product in enumerate(self.products, start=1):
            tk.Label(self.product_frame, text=product["name"]).grid(row=i, column=0, padx=10, pady=5)
            tk.Label(self.product_frame, text=f"${product['price']:.2f}").grid(row=i, column=1, padx=10, pady=5)
            tk.Label(self.product_frame, text=product["description"]).grid(row=i, column=2, padx=10, pady=5)

        self.payment_options = ["Phone Pay", "Google Pay", "Debit Card"]

        for j, option in enumerate(self.payment_options, start=len(self.products) + 1):
            tk.Label(self.product_frame, text=option).grid(row=j, column=0, padx=10, pady=5)

        self.checkout_button = tk.Button(self.product_frame, text="Checkout", command=self.checkout)
        self.checkout_button.grid(row=len(self.products) + len(self.payment_options), column=0, padx=10, pady=5)

    def checkout(self):
        if not self.logged_in:
            messagebox.showerror("Error", "Please log in first.")
            return

        selected_option = messagebox.askquestion("Payment Method", "Choose your payment method:\nPhone Pay, Google Pay, or Debit Card")
        if selected_option == "yes":
            messagebox.showinfo("Payment", "Processing payment via Phone Pay.")
        elif selected_option == "no":
            messagebox.showinfo("Payment", "Processing payment via Google Pay.")
        else:
            messagebox.showinfo("Payment", "Processing payment via Debit Card.")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window until login
    app = ECommerceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
