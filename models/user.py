from datetime import datetime



class User:

    def __init__(self, first_name, last_name, username, email,
                 bio='', password='', profile_image_url='', 
                 created_on=None, active=True, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.bio = bio
        self.profile_image_url = profile_image_url
        self.created_on = created_on or datetime.now()
        self.active = active