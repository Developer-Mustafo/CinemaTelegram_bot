class User:
    def __init__(self, user_id, name, surname):
        self.user_id = user_id
        self.name = name
        self.surname = surname
class Film:
    def __init__(self, caption, file_id, film_id=None):
        self.caption = caption
        self.file_id = file_id
        self.film_id = film_id
    def __str__(self):
        return f'{self.caption} {self.film_id}'