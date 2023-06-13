import tkinter
import customtkinter
from pytube import YouTube

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YtDownloader")
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


def startDownload():
    optionmenu_var.get()
    try:
        if optionmenu_var.get() == "Video":
            ytLink = link.get()
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            title.configure(
                text=(ytObject.author + " \n " + ytObject.title))
            video = ytObject.streams.get_highest_resolution()
            video.download()
            resultLabel.configure(text="Download Complete")

        elif optionmenu_var.get() == "Audio Only":
            ytLink = link.get()
            ytObject = YouTube(ytLink, on_progress_callback=on_progress)
            title.configure(
                text=(ytObject.author + " \n " + ytObject.title))
            audio = ytObject.streams.get_audio_only()
            audio.download()
            resultLabel.configure(text="Download Complete")

    except:
        resultLabel.configure(text="Invalid Link")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    porcentage_of_completion = bytes_downloaded / total_size * 100
    poc = str(int(porcentage_of_completion))
    porcentage.configure(text=poc+"%")
    porcentage.update()
    progress.set(float(porcentage_of_completion)/100)


title = customtkinter.CTkLabel(
    app, text="Download your YouTube videos", font=("Poppins bold", 24))
title.pack(padx=16, pady=36)


link = customtkinter.CTkEntry(
    app, width=350, height=40, placeholder_text="Video link here")
link.pack()

resultLabel = customtkinter.CTkLabel(app, text="", font=("Poppins bold", 16))
resultLabel.pack(pady=8)


optionmenu_var = customtkinter.StringVar(value="Video")
optionmenu = customtkinter.CTkOptionMenu(app, values=["Video", "Audio Only"],
                                         command=optionmenu_callback, width=100, fg_color="#495057", button_color="#495057",
                                         button_hover_color="#212529", dropdown_fg_color="#495057",  variable=optionmenu_var)
optionmenu.pack()

download = customtkinter.CTkButton(
    app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

porcentage = customtkinter.CTkLabel(app, text="")
porcentage.pack()
progress = customtkinter.CTkProgressBar(app, width=400)
progress.set(0)
progress.pack(padx=10, pady=10)


app.mainloop()
