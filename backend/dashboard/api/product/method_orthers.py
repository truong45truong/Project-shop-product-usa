from django.conf import settings
import json
import base64
import datetime
import uuid 
import os
path_upload_image = str(settings.BASE_DIR)+"/media"
path_upload_video = str(settings.BASE_DIR)+"/media"

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
def handleDecodeFile(file_data,is_image,is_video):
    file_format, file_string = file_data.split(';base64,')
    file_ext = file_format.split('/')[-1]
    file_bytes = base64.b64decode(file_string)
    if is_image is True:
        name_file = 'blog-' + str(uuid.uuid4()) + '.' + file_ext
        with open( os.path.join(path_upload_image, "photos" , name_file), 'wb+') as decoded_image_file:
            decoded_image_file.write(file_bytes)
            return { 
                'name' : name_file ,
                'file' : 'media/photos/' + name_file ,
                'type' : False
            }
    if is_video is True:
        name_file = 'blog' + str(uuid.uuid4()) + '.' + file_ext
        with open( os.path.join(path_upload_video, "videos",name_file), 'wb+') as decoded_image_file:
            decoded_image_file.write(file_bytes)
            return {
                'name' : name_file,
                'file' : 'media/videos/' + name_file ,
                'type' : True
            }
def removeFile(file_src):
    print(file_src)
    os.remove(file_src)