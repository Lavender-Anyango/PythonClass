# class Movies:
#     def __init__(self):
#         self.movie_projects=[]

#     def add_movies(self, cst_members, due_date, budgets):

#       """"
#       As a producer in the booming Nolywood movie industry, you are in charge of multiple film projects at once.
#       Each movie has diferent cast members, shooting schedules, and budgets. You want to write a prrogram to help manage your film projects efficiently. The software should be able to handle the complexities of scheduling, budgeting and coordinating between different movie projects.
#       """

#       """

class FilmProject:
    def __init__(self, title, budget):
        self.title = title
        self.budget = budget
        self.cast_members = []
        self.shooting_schedule = {}

    def add_cast_member(self, name, role):
        self.cast_members.append({"name": name, "role": role})

    def set_shooting_schedule(self, day_schedule):
        self.shooting_schedule = day_schedule

    def update_budget(self, amount):
        self.budget -= amount

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Budget: {self.budget}")
        print("Cast Members:")
        for member in self.cast_members:
            print(f"{member['name']} ({member['role']})")
        print("Shooting Schedule:")
        for day, schedule in self.shooting_schedule.items():
            print(f"{day}: {schedule}")

class CastMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Example usage
films = [
    FilmProject("Nollywood Thriller", 5000000),
    FilmProject("Romantic Drama", 3000000)
]

# Adding cast members to the first film project
john_doe = CastMember("John Doe", "Lead Actor")
jane_smith = CastMember("Jane Smith", "Female Lead")
films[0].add_cast_member(john_doe.name, john_doe.role)
films[0].add_cast_member(jane_smith.name, jane_smith.role)

# Setting shooting schedules for both film projects
films[0].set_shooting_schedule({"Day 1": "Scene 1: Location A", "Day 2": "Scene 2: Location B"})
films[1].set_shooting_schedule({"Day 1": "Scene 3: Location C", "Day 2": "Scene 4: Location D"})

# Updating the budget for the first film project
films[0].update_budget(200000)

# Displaying information for all film projects
for i, film in enumerate(films, start=1):
    print(f"\nFilm {i}:")
    film.display_info()


# in a small village, there is a baobab tree believed to have magical properties. every season, it bears different types of trees each with its own unique power. you have decided to creae a softwar problem that tracks the changes in the tree and predicts what type of fruit it will bear next season and what powers it will possess. the system will also record the effect of each fruit when consumed