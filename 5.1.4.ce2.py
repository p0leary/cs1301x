class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = self.setTitle(title)
        self.description = self.setDescription(description)
        self.completed = self.setCompleted(completed)
        # self.setTitle(title)
        # self.setDescription(description)
        # self.setCompleted(completed)
    # Getters
    def getTitle(self):
        print("title accessed")
        return self.title
    def getDescription(self):
        print("description accessed")
        return self.description
    def getCompleted(self):
        print("completed accessed")
        return self.completed
    # Setters
    def setTitle(self, newTitle):
        print("title changed")
        if type(newTitle) == str:
            # self.title = newTitle
            return newTitle
        else:
            print("invalid value")
            # self.title = None
            return None
    def setDescription(self, newDescription):
        print("description changed")
        if type(newDescription) == str:
            self.description = newDescription
            return newDescription
        else:
            print("invalid value")
            self.description = None
            return None
    def setCompleted(self, newCompleted):
        print("completed changed")
        if type(newCompleted) == bool:
            self.completed = newCompleted
            # return newCompleted
        else:
            print("invalid value")
            self.completed = None
            # return None

newItem = TodoItem(100, 37, True)
print(newItem.title)
print(newItem.description)
print(newItem.completed)
# newItem.setTitle("test")
# print(newItem.title)

# # print("description: " + newItem.description)
# # print("completed: " + str(newItem.completed))