class User:
    def __init__(self, user_id, name, surname):
        self.user_id = user_id
        self.name = name
        self.surname = surname
class Film:
    def __init__(self, title, year, genre, file_id, film_id=None):
        self.title = title
        self.year = year
        self.genre = genre
        self.file_id = file_id
        self.film_id = film_id
    def __str__(self):
        return f'{self.title} {self.year} {self.genre} {self.film_id}'