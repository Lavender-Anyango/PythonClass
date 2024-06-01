class MovieProject:
    def __init__(self, title, budget, cast, shooting_schedule):
        self.title = title
        self.budget = budget
        self.cast = cast
        self.shooting_schedule = shooting_schedule

    def display_project_info(self):
        print(f"Title: {self.title}")
        print(f"Budget: ${self.budget}")
        print(f"Cast: {', '.join(self.cast)}")
        print(f"Shooting Schedule: {self.shooting_schedule}")

    def update_budget(self, new_budget):
        self.budget = new_budget

    def update_cast(self, new_cast):
        self.cast = new_cast

    def update_shooting_schedule(self, new_schedule):
        self.shooting_schedule = new_schedule


class MovieProjectManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def display_all_projects(self):
        for project in self.projects:
            project.display_project_info()

    def update_project(self, project_title, update_type, new_value):
        for project in self.projects:
            if project.title == project_title:
                if update_type == "budget":
                    project.update_budget(new_value)
                elif update_type == "cast":
                    project.update_cast(new_value)
                elif update_type == "shooting_schedule":
                    project.update_shooting_schedule(new_value)
                else:
                    print("Invalid update type. Please choose 'budget', 'cast', or 'shooting_schedule'.")
                return
        print("Project not found.")

    def manage_projects(self):
        while True:
            print("\n1. Add a new project")
            print("2. Display all projects")
            print("3. Update a project")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter the title of the new project: ")
                budget = float(input("Enter the budget for the new project: "))
                cast = input("Enter the cast members for the new project (comma-separated): ").split(',')
                shooting_schedule = input("Enter the shooting schedule for the new project: ")
                new_project = MovieProject(title, budget, cast, shooting_schedule)
                self.add_project(new_project)
            elif choice == "2":
                self.display_all_projects()
            elif choice == "3":
                project_title = input("Enter the title of the project to update: ")
                update_type = input("Enter the type of update (budget, cast, or shooting_schedule): ")
                new_value = input(f"Enter the new {update_type} for the project: ")
                self.update_project(project_title, update_type, new_value)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please choose a valid option.")


# Example usage:
manager = MovieProjectManager()
manager.manage_projects()