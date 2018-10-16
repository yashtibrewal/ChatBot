from DataInput import DataBase


class Bot():

    # PK	Name	Subject	Exp	Rating	Cost	Start Time	End Time	Location	Language
    def __init__(self):
        self.subject = None  # compulsory
        self.exp = None
        self.rating = None
        self.cost = None
        self.minBudget = None
        self.maxBudget = None  # compulsory
        self.location = None  # compulsory
        self.language = None
        self.db = DataBase()
        self.db.setFilePath("Chatbot.xlsx")
        self.db.readFile()
        self.df = self.db.getDataFrame()

    def talk(self):
        self.greet()
        self.ask()
        self.think()
        self.answer()
        self.confirm()

    def confirm(self):
        """Confirm with the user for his requirements."""
        user_input = input("Have you got what you are looking for?")
        user_input = user_input.lower()
        if "no" in user_input:
            self.talk()
            return
        elif "yes" in user_input:
            self.thank()
            self.collectFeedback()
        else:
            print("Please reply a yes or a not")
            self.confirm()
            return

    def thank(self):
        """Thank the user"""
        print("--------------------------------------\n Thank you for using our services,"
              "please help us know what you think!")

    def collectFeedback(self):
        """Store feed back into a file"""
        return

    def greet(self):
        """Greeting the user"""
        print("Hello! I shall help you to find the best fit tution for you")
        return

    def ask(self):
        """
        call the functions to ask the following variable values.
        Name	Subject	Exp	Rating	Cost	Start Time	End Time	Location	Language
        :return:
        """
        self.askSubject()
        self.askExperience()
        self.askRating()
        self.askBudget()
        self.askLocation()
        self.askLanguage()

    def askSubject(self, first=True):
        if first:
            user_input = input("Which subject tution are you looking for?\n")
        else:
            user_input = input("Please enter another subject\n")
        user_input = user_input.lower()
        user_input = user_input.split(" ")
        if "which" in user_input and "subjects" in user_input:
            user_input = input("Would you like to know which all subjects we offer?\n")
            if "yes" in user_input:
                print("We offer the following subjects!")
                for subject in self.db.subjects:
                    print(subject)
                self.askSubject(False)
                return
        sub = self.matchWord(user_input, self.db.subjects)
        if len(sub) > 1:
            print("Please enter only one subject at a time, I am in a learning stage")
            self.askSubject()
            return
        elif len(sub) is 0:
            print("Sorry! we don't have tutions for that subject")
            self.askSubject(False)
            return
        self.subject = sub[0]
        print("Okay, I will keep in mind you need tution for ", self.subject)

    def askExperience(self):
        pass

    def askRating(self):
        pass

    def askBudget(self):
        self.askMaxBudget()
        self.askMinBudget()

    def askMinBudget(self):
        pass

    def askMaxBudget(self):
        # Tests:
        # Check with more than one value entered,
        # Check with one value entered,
        # Check with no values entered,
        user_input = input("What is your maximum budget?\n")
        user_input = user_input.lower()
        # extract numbers from the input
        value = [int(element) for element in user_input.split(" ") if element.isdigit()]
        if value.__len__() > 1:
            print("Please enter only one value at a time, I am in a learning stage")
            self.askMaxBudget()
            return
        elif "max" in user_input:
            print("You entered a maximum budget of ", value[0])
        elif len(value) is 1:
            print("You entered a maximum budget of ", value[0])
        else:
            self.askMaxBudget()
            return
        self.maxBudget = value[0]
        print("Okay, I will keep in mind that your maximum budget is ", self.maxBudget)

    def matchWord(self, user_input, check_list):
        # loop to check for single word match
        match = []
        for element in user_input:
            if element in check_list:
                match.append(element)
        length = len(user_input)
        # loop to check for 2 word match
        for i in range(length - 1):
            word1 = user_input[i]
            word2 = user_input[i + 1]
            if word1 + " " + word2 in check_list:
                match.append(word1 + " " + word2)
        return match

    def askLocation(self, first=True):
        if first:
            user_input = input("Please share where do you live in Mumbai\n")
        else:
            user_input = input("Please share a new location\n")
        user_input = user_input.lower()
        user_input = user_input.split(" ")
        loc = []
        loc = self.matchWord(user_input, self.db.locations)
        # print(loc)
        if len(loc) > 1:
            print("Please enter only one locaion at a time,  I am in a learning stage")
            self.askLocation()
            return
        if len(loc) is 0:
            print("Sorry there are no tutions for that location, try another location")
            self.askLocation(False)
            return
        self.location = loc[0]
        print("Okay, I will keep in mind that your location is ", self.location)
        return

    def askLanguage(self):
        pass

    def answer(self):
        if self.df.empty:
            print("Sorry we do not have any faculty with the specified details")
            return
        print("Here is a list which shall be helpful to you")
        print("Faculty Name  Contact ")
        for element in self.df["Faculty"]:
            print(element)

    def think(self):
        self.df = self.db.getTeachersBasedOnCost(self.df, maxCost=self.maxBudget)
        self.df = self.db.getTeacherBasedOnSubject(self.df, self.subject)
        self.df = self.db.getTeachersBasedOnLocation(self.df, self.location)


if __name__ == "__main__":
    bot = Bot()
    bot.talk()
    # bot.askMaxBudget()
    # bot.askLocation()
