"""Module to import and format the data"""
import os
import pandas as pd


class DataBase():

    # PK	Name	Subject	Exp	Rating	Cost	Start Time	End Time	Location	Language
    def __init__(self):
        self.file = ""
        self.teachers = pd.DataFrame
        self.subjects = []
        self.languages = []
        self.locations = []
        self.costs = []

    def preProcess(self):
        # converting the data to the right format
        self.teachers["Name"] = self.teachers["Name"].str.lower()
        self.teachers["Subject"] = self.teachers["Subject"].str.lower()
        self.teachers["Location"] = self.teachers["Location"].str.lower()
        self.teachers["Language"] = self.teachers["Language"].str.lower()
        self.teachers["Rating"] = self.teachers["Rating"].apply(pd.to_numeric)
        self.teachers["Exp"] = self.teachers["Exp"].apply(pd.to_numeric)
        self.teachers["Cost"] = self.teachers["Cost"].apply(pd.to_numeric)
        # finding the sets for each category
        self.subjects = list(self.teachers["Subject"])
        self.languages = list(self.teachers["Language"])
        self.costs = list(self.teachers["Cost"])
        self.locations = list(self.teachers["Location"])

    def setFilePath(self,path):
        if os.path.isfile(path):
            if __name__ == "__main__":
                print("Fie Exists!!")
        else:
            raise FileNotFoundError
        self.file = path

    def readFile(self):
        self.teachers = pd.read_excel(self.file)
        self.preProcess()

    def displayFile(self):
        print(self.teachers.head())

    def getDataFrame(self):
        return self.teachers

    def getTeacherBasedOnSubject(self,data_frame,subject):
        subject = subject.lower()
        new_subject_dataframe = data_frame.loc[data_frame["Subject"] == subject]
        # new_subject_dataframe.pop("Subject")
        return new_subject_dataframe

    def  getTeachersBasedOnRating(self,data_frame,rating):
        new_subject_dataframe = data_frame.loc[data_frame["Rating"] >= rating]
        # new_subject_dataframe.pop("Rating")
        return new_subject_dataframe

    def  getTeachersBasedOnExperience(self,data_frame,exp):
        new_subject_dataframe = data_frame.loc[data_frame["Exp"] >= exp]
        # new_subject_dataframe.pop("Exp")
        return new_subject_dataframe

    def  getTeachersBasedOnCost(self,data_frame,**args):
        """The function returns the cost based on the keywords min and max"""
        for key in args:
            if key == "minCost":
                new_subject_dataframe = data_frame.loc[data_frame["Cost"] >= args["minCost"] ]
            if key == "maxCost":
                new_subject_dataframe = data_frame.loc[data_frame["Cost"] <= args["maxCost"] ]
        # new_subject_dataframe.pop("Cost")
        return new_subject_dataframe

    def getTeachersBasedOnLocation(self,data_frame,loc):
        loc = loc.lower()
        new_subject_dataframe = data_frame.loc[data_frame["Location"] == loc ]
        new_subject_dataframe.pop("Location")
        return new_subject_dataframe

    def getTeachersBasedOnLanguage(self,data_frame,lang):
        lang = lang.lower()
        new_subject_dataframe = data_frame.loc[data_frame["Language"] == lang ]
        new_subject_dataframe.pop("Language")
        return new_subject_dataframe


if __name__ == "__main__":
#test module
    db = DataBase()
    db.setFilePath("Data.xlsx")
    db.readFile()
    # db.displayFile()
    df = db.getDataFrame()
    # df = db.getTeacherBasedOnSubject(df,"Programming")
    # df = db.getTeachersBasedOnRating(df,4.5)
    # df = db.getTeachersBasedOnCost(df,minCost = 500)
    # df = db.getTeachersBasedOnCost(df,maxCost = 500)
    # df = db.getTeachersBasedOnExperience(df,9)
    # df = db.getTeachersBasedOnLocation(df,"Borivali")
    # df = db.getTeachersBasedOnLanguage(df,"Hindi")
    print(df)
