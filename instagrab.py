# Author: Alex O Regan

from html.parser import HTMLParser
from urllib.request import urlopen
import tkinter


class Gui:
    def __init__(self, master):
        master.title("Instagrab")
        self.frame = tkinter.Frame(master, bg="white")
        self.frame.pack()

        self.title_img = tkinter.PhotoImage(file="instagrab_data/bin/title.png")
        self.title_label = tkinter.Label(self.frame, image=self.title_img, bg="white")
        self.title_label.grid(row=0, column=0, columnspan=3)

        self.url_image = tkinter.PhotoImage(file="instagrab_data/bin/content.png")
        self.label_url = tkinter.Label(self.frame, image=self.url_image, bg="white")
        self.label_url.grid(column=0, row=1)

        self.fn_image = tkinter.PhotoImage(file="instagrab_data/bin/filename.png")
        self.label_fn = tkinter.Label(self.frame, image=self.fn_image, bg="white")
        self.label_fn.grid(column=0, row=2)

        self.url_field = tkinter.Entry(self.frame, width=43, highlightbackground="black", highlightthickness=2)
        self.url_field.grid(column=1, row=1, columnspan=3)
        self.name_field = tkinter.Entry(self.frame, width=26, highlightbackground="black", highlightthickness=2)
        self.name_field.grid(column=1, row=2)

        self.get_button = tkinter.Label(self.frame, text="Grab!", width=9, bg="white", highlightbackground="black",
                                        highlightthickness=2)
        self.get_button.bind("<Button-1>", get_url)
        self.get_button.grid(column=2, row=2)

        self.done_image = tkinter.PhotoImage(file="instagrab_data/bin/done.png")
        self.wait_image = tkinter.PhotoImage(file="instagrab_data/bin/wait.png")
        self.view_image = tkinter.Label(self.frame, image=self.wait_image, bg="white")
        self.view_image.grid(column=3, row=2)


class InstaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.filename = None

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if ("property", "og:video") in attrs:
            u = urlopen((attrs[1][1]))
            d = u.read()
            path = "instagrab_data/" + self.filename + ".mp4"
            f = open(path, "wb")
            f.write(d)
            f.close()
        elif ("property", "og:image") in attrs:
            u = urlopen((attrs[1][1]))
            d = u.read()
            path = "instagrab_data/" + self.filename + ".jpg"
            f = open(path, "wb")
            f.write(d)
            f.close()


def get_url(event):
    url_req = urlopen(gui.url_field.get())
    data = str(url_req.read())
    parse_object.filename = gui.name_field.get()
    parse_object.feed(data)
    gui.view_image.config(image=gui.done_image)
    print(flush=True)

root = tkinter.Tk()
root.resizable(width=False, height=False)
img = tkinter.PhotoImage(file='instagrab_data/bin/ico.png')
root.tk.call('wm', 'iconphoto', root._w, img)
gui = Gui(root)
parse_object = InstaParser()
root.mainloop()
