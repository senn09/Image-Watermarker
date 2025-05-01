import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Multi-View App")

# Create frames for different views
main_frame = ttk.Frame(root)
view1_frame = ttk.Frame(root)
view2_frame = ttk.Frame(root)

# Function to switch between views
def show_view(view):
    main_frame.pack_forget()
    view1_frame.pack_forget()
    view2_frame.pack_forget()
    view.pack(fill="both", expand=True)

# Widgets for the main frame (e.g., navigation)
ttk.Label(main_frame, text="Main View").pack(pady=10)
ttk.Button(main_frame, text="Go to View 1", command=lambda: show_view(view1_frame)).pack(pady=5)
ttk.Button(main_frame, text="Go to View 2", command=lambda: show_view(view2_frame)).pack(pady=5)

# Widgets for View 1
ttk.Label(view1_frame, text="View 1").pack(pady=10)
ttk.Label(view1_frame, text="Content for View 1").pack(pady=5)
ttk.Button(view1_frame, text="Back to Main", command=lambda: show_view(main_frame)).pack(pady=5)

# Widgets for View 2
ttk.Label(view2_frame, text="View 2").pack(pady=10)
ttk.Label(view2_frame, text="Content for View 2").pack(pady=5)
ttk.Button(view2_frame, text="Back to Main", command=lambda: show_view(main_frame)).pack(pady=5)

# Show the initial view
show_view(main_frame)

root.mainloop()