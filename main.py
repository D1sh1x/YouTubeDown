from pytube import YouTube
import customtkinter as CTk

Ok = YouTube

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("460x370")
        self.title("YouTubeDownload")
        self.main_frame = CTk.CTkFrame(master=self)
        self.main_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.var = CTk.StringVar()
        self.url = CTk.CTkEntry(master=self.main_frame, width=300, textvariable=self.var)
        self.url.grid(row=0, column=0, padx=(0, 20))
        self.button = CTk.CTkButton(master=self.main_frame, text='Download', width=100, command=self.Down)
        self.button.grid(row=1, column=0)

    def Down(self):
        YouTube(self.var.get()).streams.first().download(r'C:\Users\avaki\downloads')

if __name__ == '__main__':
    App().mainloop()