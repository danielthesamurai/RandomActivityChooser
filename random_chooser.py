import random
import tkinter as tk
import json
#activities that can be chosen randomly
actives = []
games = []
anime = []
movies = []
save_load_list = []

#load lists from disk
with open("things_to_do.json","r") as newfile:
    save_load_list = json.load(newfile)

actives = save_load_list["actives"]
games = save_load_list["games"]
movies = save_load_list["movies"]
anime = save_load_list["anime"]


#variables for handling consistent font sizes
font_size = 18

#function for handling choosing randomly from the list
def choose_function(meta):
    meta_choose = meta[random.randint(0,len(meta)-1)]
    return meta_choose

#choose the things
active_choose = choose_function(actives)
game_choose = choose_function(games)
anime_choose = choose_function(anime)
movies_choose = choose_function(movies)

def check_active_type(label_var):
    if active_choose == "Watch A Movie":
        label_var.configure(text=movies_choose)
    if active_choose == "Play A Game":
        label_var.configure(text=game_choose)
    if active_choose == "Watch An Anime":
        label_var.configure(text=anime_choose)
        
def generate_new_random():
    active_choose = choose_function(actives)
    game_choose = choose_function(games)
    anime_choose = choose_function(anime)
    movies_choose = choose_function(movies)
    main_label.configure(text=active_choose)
    if active_choose == "Watch A Movie":
        sub_label.configure(text=movies_choose)
    if active_choose == "Play A Game":
        sub_label.configure(text=game_choose)
    if active_choose == "Watch An Anime":
        sub_label.configure(text=anime_choose)
        
#functions for the domain specific buttons
def get_new_movie():
    movies_choose = choose_function(movies)
    main_label.configure(text=actives[0])
    sub_label.configure(text=movies_choose)


def get_new_game():
    game_choose = choose_function(games)
    sub_label.configure(text=game_choose)
    main_label.configure(text=actives[1])

def get_new_anime():
    anime_choose = choose_function(anime)
    sub_label.configure(text=anime_choose)
    main_label.configure(text=actives[2])

#save the new lists to the file after appending
def save_to_file():
    with open("things_to_do.json","w") as newfile:
        meta_list = {"actives":actives,"games":games,"anime":anime,"movies":movies}
        json.dump(meta_list,newfile)

#functions for adding new activities based on entry box
def get_anime_text():
    if new_entry_form.get() != "":
        anime.append(new_entry_form.get().title())
        new_entry_form.delete(0,"end")
        save_to_file()
    
def get_movie_text():
    if new_entry_form.get() != "":
        movies.append(new_entry_form.get().title())
        new_entry_form.delete(0,"end")
        save_to_file()
    
def get_game_text():
    if new_entry_form.get() != "":
        games.append(new_entry_form.get().title())
        new_entry_form.delete(0,"end")
        save_to_file()

#function for removing entries 
def remove_active():
    for movie_entry in movies:
        if new_entry_form.get().title() == movie_entry:
            movies.pop(movies.index(new_entry_form.get().title()))
            save_to_file()
    for game_entry in games:
        if new_entry_form.get().title() == game_entry:
            games.pop(games.index(new_entry_form.get().title()))
            save_to_file()
    for anime_entry in anime:
        if new_entry_form.get().title() == anime_entry:
            anime.pop(anime.index(new_entry_form.get().title()))
            save_to_file()
    new_entry_form.delete(0,"end")

#initialize the window 
window = tk.Tk()
window.geometry("500x600")
window.title("Random Activity Chooser")

#make the widgets
main_label = tk.Label(text=active_choose,font=("Arial",font_size))
subtext = tk.StringVar()
sub_label = tk.Label(font=("Arial",font_size))
check_active_type(sub_label)
new_button = tk.Button(text="Anything",command=generate_new_random,font=("Arial",font_size),pady=10,bd=10)
new_entry_form = tk.Entry(window,font=("Arial",font_size))
entry_form_label = tk.Label(text="Enter a New Activity: ",font=("Arial",font_size))
choose_activity_label = tk.Label(text="Choose Activity Type: ",font=("Arial",font_size))
movie_button = tk.Button(text="Movie",font=("Arial",font_size),command=get_movie_text,bd=10)
game_button = tk.Button(text="Game",font=("Arial",font_size),command=get_game_text,bd=10)
anime_button = tk.Button(text="Anime",font=("Arial",font_size),command=get_anime_text,bd=10)
remove_button = tk.Button(text="Remove Activity",font=("Arial",font_size),command=remove_active,bd=10)
frame = tk.Frame(window)
new_game_button = tk.Button(frame,text="Game",font=("Arial",font_size),bd=10,command=get_new_game)
new_movie_button = tk.Button(frame,text="Movie",font=("Arial",font_size),bd=10,command=get_new_movie)
new_anime_button = tk.Button(frame,text="Anime",font=("Arial",font_size),bd=10,command=get_new_anime)

#pack all the widgets into the window
new_button.pack(pady=15,padx=(10,0))
new_movie_button.pack(side=tk.LEFT,padx=20)
new_game_button.pack(side=tk.LEFT,padx=10)
new_anime_button.pack(side=tk.LEFT,padx=20)
frame.pack(padx=(30,10))
main_label.pack(pady=(40,0))
sub_label.pack(pady=(0,10))
entry_form_label.pack(pady=15)
new_entry_form.pack()
choose_activity_label.pack(pady=15)
remove_button.pack()
movie_button.pack(side=tk.LEFT,padx=(80,0))
game_button.pack(side=tk.LEFT,padx=30)
anime_button.pack(side=tk.LEFT)

#create the window
window.mainloop()