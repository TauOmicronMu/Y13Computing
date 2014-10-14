#SearchResultsScreen

from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *

from LoggingStringsEnglish import *

import random

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from SearchResultsScreenStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from SearchResultsScreenStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

import re

class SearchResultsScreen(Frame):

    def __init__(self, parent, names, departments, DOBs, genders, salaries, codes):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INSTANCE_OF_SEARCHRESULTSSCREEN_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

        self.parent = parent
        self.names = names
        self.departments = departments
        self.DOBs = DOBs
        self.genders = genders
        self.salaries = salaries
        self.codes = codes

        self.initialiseUI()

    def initialiseUI(self):

        global listboxOne
        global listboxTwo
        global listboxThree
        global listboxFour
        global listboxFive
        global listboxSix

        self.parent.title(WINDOW_TITLE)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)

        fileMenu.add_command(label=DROPDOWN_BACK_TEXT, underline=0, command=self.onBack)

        fileMenu.add_separator()

        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command=self.Help)
        
        fileMenu.add_separator()

        menubar.add_cascade(label=DROPDOWN_FILE_TEXT, underline=0, menu=fileMenu)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MENUBAR_INITIALISED_TEXT)

        TitleLabel = Label(text="Search Results", font=("Purisa", 16))

        TitleLabel.pack()

        AnchorLabel = Label(width=9)

        AnchorLabel.pack(side=LEFT)

        scrollbar = Scrollbar(self.parent)
        scrollbar.pack(side=RIGHT, fill=Y)

        listboxOne = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxOne.insert(END, "Name: ")
        listboxOne.insert(END, "------------------------")
     
        for i in range(len(self.names)):
            listboxOne.insert(END, self.names[i])
            listboxOne.pack(side=LEFT, fill=BOTH)

        listboxOne.insert(END, "------------------------")

        listboxTwo = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxTwo.insert(END, "Department: ")
        listboxTwo.insert(END, "------------------------")

        for i in range(len(self.departments)):
            listboxTwo.insert(END, self.departments[i])
            listboxTwo.pack(side=LEFT, fill=BOTH)

        listboxTwo.insert(END, "------------------------")

        listboxThree = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxThree.insert(END, "DOB: ")
        listboxThree.insert(END, "------------------------")

        for i in range(len(self.DOBs)):
            listboxThree.insert(END, self.DOBs[i])
            listboxThree.pack(side=LEFT, fill=BOTH)
            
        listboxThree.insert(END, "------------------------")

        listboxFour = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxFour.insert(END, "Gender: ")
        listboxFour.insert(END, "------------------------")

        for i in range(len(self.genders)):
            if self.genders[i] == "M":
                listboxFour.insert(END, "Male")
            else:
                listboxFour.insert(END, "Female")
            listboxFour.pack(side=LEFT, fill=BOTH)
            
        listboxFour.insert(END, "------------------------")

        listboxFive = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxFive.insert(END, "Salary: ")
        listboxFive.insert(END, "------------------------")

        for i in range(len(self.salaries)):
            listboxFive.insert(END, self.salaries[i])
            listboxFive.pack(side=LEFT, fill=BOTH)

        listboxFive.insert(END, "------------------------")

        listboxSix = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxSix.insert(END, "Employee Code: ")
        listboxSix.insert(END, "------------------------")

        for i in range(len(self.codes)):
            listboxSix.insert(END, self.codes[i])
            listboxSix.pack(side=LEFT, fill=BOTH)

        listboxSix.insert(END, "------------------------")

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)

        scrollbar.config(command= self.yview)

    def yview(self, *args):
        apply(listboxOne.yview, args)
        apply(listboxTwo.yview, args)
        apply(listboxThree.yview, args)
        apply(listboxFour.yview, args)
        apply(listboxFive.yview, args)
        apply(listboxSix.yview, args)

    def onBack(self):
        pass

    def Help(self):
        pass

'''
This section is used for testing the GUI.
It passes generic results in to ensure
that everything is formated as it should
be.
=========================================
'''

alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
names = []
departments = []
DOBs = []
genders = []
salaries = []
codes = []
for i in range(50):
    names.append(alphabet[random.randint(0,25)]*random.randint(0,5))
    departments.append(random.randint(0,100000))
    DOBs.append(str(random.randint(1,31)) + "/" + str(random.randint(1,12)) + "/" + str(random.randint(1900,2014)))
    if random.randint(0,1) == 0:
        genders.append("M")
    else:
        genders.append("F")
    salaries.append(random.randint(0,10000000))
    codes.append("EMP" + str(random.randint(1000000,9999999)) + "E")
root = Tk()
root.geometry(WINDOW_GEOMETRY)
app = SearchResultsScreen(root, names, departments, DOBs, genders, salaries, codes)
                    
root.mainloop()
