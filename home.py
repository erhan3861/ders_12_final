import tkinter as tk
from PIL import Image, ImageTk
import client
from courses import Courses

def make_widgets(root):
    root.title("Anasayfa")
    root.geometry("1366x768+0+0")
    
    # Load images
    my_courses_image = Image.open("images/kurslarım.jpg").resize((310, 310))
    my_courses_photo = ImageTk.PhotoImage(my_courses_image)

    other_courses_image = Image.open("images/diger_kurslar.jpg").resize((310, 310))
    other_courses_photo = ImageTk.PhotoImage(other_courses_image)

    profile_image = Image.open("images/profile.jpg").resize((310, 310))
    profile_photo = ImageTk.PhotoImage(profile_image)

    statistics_image = Image.open("images/istatistik.jpg").resize((310, 310))
    statistics_photo = ImageTk.PhotoImage(statistics_image)

    chat_image = Image.open("images/chat.jpg").resize((150, 150))
    chat_photo = ImageTk.PhotoImage(chat_image)

    # Title label
    title_label = tk.Label(root, text="Online Kurs Yönetim Sistemi", font=("Arial", 24))
    title_label.grid(row=0, column=0, columnspan=4, pady=20)

    # Buttons
    my_courses_button = tk.Button(root, image=my_courses_photo, command=button_click)
    my_courses_button.grid(row=1, column=0, padx=10, pady=10)
    my_courses_button.image = my_courses_photo

    my_courses_label = tk.Label(root, text="Kurslarım", font=("Arial", 20))
    my_courses_label.grid(row=2, column=0, padx=10, pady=10)

    other_courses_button = tk.Button(root, image=other_courses_photo, command=lambda:show_other_courses(root))
    other_courses_button.grid(row=1, column=1, padx=10, pady=10)
    other_courses_button.image = other_courses_photo

    other_courses_label = tk.Label(root, text="Diğer Kurslar", font=("Arial", 20))
    other_courses_label.grid(row=2, column=1, padx=10, pady=10)

    profile_button = tk.Button(root, image=profile_photo, command=button_click)
    profile_button.grid(row=1, column=2, padx=10, pady=10)
    profile_button.image = profile_photo

    profile_label = tk.Label(root, text="Profilim", font=("Arial", 20))
    profile_label.grid(row=2, column=2, padx=10, pady=10)

    istatistik_button = tk.Button(root, image=statistics_photo, command=lambda: show_stats(root))
    istatistik_button.grid(row=1, column=3, padx=10, pady=10)
    istatistik_button.image = statistics_photo

    istatistik_label = tk.Label(root, text="İstatistikler", font=("Arial", 20))
    istatistik_label.grid(row=2, column=3, padx=10, pady=10)

    # Live Chat button (added)
    chat_button = tk.Button(root, image=chat_photo, command=live_chat_click)
    chat_button.grid(row=3, column=3, padx=10, pady=10)
    chat_button.image = chat_photo

def live_chat_click():
    print("Live Chat button clicked")
    client.get_chat_window()
    
# Function: What to do when a button is clicked
def button_click():
    print("Button clicked")

def show_stats(root):
    # Import the UserStatsApp class from the stats module (stats.py)
    from stats import UserStatsApp
    stats_window = tk.Toplevel(root)  # Create a Toplevel window for stats.py
    app = UserStatsApp(stats_window)

    root.deiconify()

# ders 12 diğer kurslar bölümü eklendi
def show_other_courses(root):
    for w in root.grid_slaves():
        w.destroy()

    back_button = tk.Button(root, text="Back", command = lambda : back(root))
    back_button.pack(pady=10)
    
    courses_root = Courses(root)
    

# ders 12 geri tuşu eklendi
def back(root):
    for w in root.pack_slaves():
        w.destroy()
    make_widgets(root)


if __name__ == "__main__":
    root = tk.Tk()
    make_widgets(root)
    root.mainloop()
