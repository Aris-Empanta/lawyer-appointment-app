import uuid
import time

class BaseProfile:

    PROFILE_PICTURE_MIME_TYPES = [
        'image/jpeg',
        'image/png',
        'image/webp',
        'image/avif',
        'image/tiff',
    ]

    default_profile_pic_name = 'images/profile-pics/avatar.png'

     # The flag to query if the profile's avatar is an 
     # external link or not.
    def is_avatar_external_link(self, image_link):
        is_external = False

        if image_link.startswith('http') or image_link.startswith('https'):
            is_external = True
            
        return is_external
    
    # The method to add in avatar's name the /media/ in front  
    # if it is from our server's files.
    def format_avatar_link(self, request, avatar_link):
        if(not avatar_link.startswith('http') or avatar_link.startswith('/http')):
                protocol = "http"

                if request.is_secure():
                    protocol = 'https' 

                avatar_link = f'{ protocol }://{request.META["HTTP_HOST"]}/media/{avatar_link}'
                return avatar_link
        
        return avatar_link
    
    # The method to rename a profile pic image so that it has a
    #  unique name in the server
    def rename_image(self, image_name):
        # We add the timestamp infront so that the image never starts with 
        # http or http like google account images. then we add a unique id, 
        # so that the name is unique, and at the end its extension.
        random_uuid = str(uuid.uuid4())
        timestamp = int(time.time())
        file_extension = image_name.split('.')[-1]
        
        return f'{timestamp}_{random_uuid}.{file_extension}'