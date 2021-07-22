from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from scrapy.utils import project
from scrapy import spiderloader
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
import threading


def get_spiders():
    settings = project.get_project_settings()
    spider_loader = spiderloader.SpiderLoader.from_settings(settings)
    return spider_loader.list()

def get_chosen_spider(value):
    global chosen_spider
    chosen_spider = value
    return chosen_spider

def get_chosen_feed(value):
    global chosen_feed
    chosen_feed = value
    return chosen_feed


def browse_button():
    global folder_path
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, END)
    folder_path_entry.insert(0, folder_path)
    return folder_path

def execute_spider():
    if dataset_entry.get() == '' or chosen_feed not in ['CSV', 'JSON']:
        messagebox.showerror('Error', 'All entries are required')
        return
    
    try:
        feed_uri = f"file:///{folder_path}/{dataset_entry.get()}.{chosen_feed}"
    except:
        messagebox.showerror('Error', 'All entries are required')
    
    settings = project.get_project_settings()
    settings.set('FEED_URI', feed_uri)
    settings.set('FEED_TYPE', chosen_feed)

    configure_logging()
    runner = CrawlerRunner(settings)
    runner.crawl(chosen_spider)
    
    reactor.run(installSignalHandlers=False)

def start_execute_thread(event):
    global execute_thread
    execute_thread = threading.Thread(target=execute_spider, daemon=True)
    execute_thread.start()
    app.after(10, check_execute_thread)

def check_execute_thread():
    if execute_thread.is_alive():
        app.after(10, check_execute_thread)



app = Tk()

#Spiders list
spider_label = Label(app, text='Choose a spider')
spider_label.grid(row=0 , column=0, sticky=W, pady=10, padx=10)

spider_text = StringVar(app)
spider_text.set('Choose a spider')
spiders = [spider for spider in get_spiders()]

spiders_dropdown = OptionMenu(app, spider_text, *spiders, command=get_chosen_spider)
spiders_dropdown.grid(row=0, column=1, columnspan=2)

# Feed Type
feed_label = Label(app, text='Choose a feed')
feed_label.grid(row=1 , column=0, sticky=W, pady=10, padx=10)

feed_text = StringVar(app)
feed_text.set('Choose a feed')
feeds = ['JSON', 'CSV']

feed_dropdown = OptionMenu(app, feed_text, *feeds, command=get_chosen_feed)
feed_dropdown.grid(row=1, column=1, columnspan=2)

# Path Entry
folder_path_text = StringVar(app)
folder_path_entry = Entry(app, textvariable=folder_path_text)
folder_path_entry.grid(row=2, column=0, pady=10, padx=10)

# Dataset Entry
dataset_text = StringVar(app)
dataset_entry = Entry(app, textvariable=dataset_text, width=10)
dataset_entry.grid(row=2, column=1, pady=10, padx=10)

browse_btn = Button(app, text='Browse', command=browse_button)
browse_btn.grid(row=2, column=2)

#update this one too
execute_btn = Button(app, text='Execute', command=lambda: start_execute_thread(None))
execute_btn.grid(row=3, column=0, columnspan=3)

app.title('Spider Executer')
app.geometry('300x200')
app.resizable(False, False)
app.mainloop()