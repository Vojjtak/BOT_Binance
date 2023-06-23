import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("500x350")
app.title("Vojjtak Binance Bot")

frame1 = ctk.CTkFrame(app, width=500, height=600)
frame2 = ctk.CTkFrame(app, width=500, height=600)

def frame1(app, frame1):
    frame1.tkraise()
    frame1 = ctk.CTkFrame(app, width=500, height=600)
    frame1.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame1, text="Enter your API and SCR_KEY")
    label.pack(pady=12, padx=10)
    return frame1

def frame2(app, frame2):
    frame2.ctkraise
    frame2 = ctk.CTkFrame(app, width=500, height=600)
    frame1.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame1, text="Enter your API and SCR_KEY")
    label.pack(pady=12, padx=10)
    return frame2