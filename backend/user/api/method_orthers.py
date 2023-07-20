from django.conf import settings
import json
import base64
import datetime
import uuid 
import os
path_upload_image = str(settings.BASE_DIR)+"/media/photos"
path_upload_video = str(settings.BASE_DIR)+"/media/videos"

# ---------------------------------------------------------------------------- #
#                              HANDLE FILE ENCODE                              #
# ---------------------------------------------------------------------------- #
"""_summary_
PARMAS : 
    + file_data : data file encode
    + is_image : file is image
    + is_video : file is video
RETURN :
    + name : name file before decode
    + file :path file
    + type : type of file
"""
def handleDecodeFile(file_data):
    file_format, file_string = file_data.split(';base64,')
    file_ext = file_format.split('/')[-1]
    file_bytes = base64.b64decode(file_string)
    name_file = 'user-' + str(uuid.uuid4()) + '.' + file_ext
    with open( os.path.join(path_upload_image, "user" , name_file), 'wb+') as decoded_image_file:
        decoded_image_file.write(file_bytes)
        print(decoded_image_file)
        return { 
            'name' : name_file ,
            'file' : 'media/photos/user/' + name_file ,
            'type' : False
        }

def removeImage(path):
    try:
        os.remove(os.path.join(path))
        return True
    except Exception as e:
        print(e)
        return False