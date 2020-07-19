import os
from PIL import Image
from flask import url_for, current_app

#function for adding a picture to the created game
def add_game_pic(pic_upload,game_code):

    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(game_code)+'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static/games',storage_filename)

    output_size = (300,200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
