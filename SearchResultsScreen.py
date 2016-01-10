#SearchResultsScreen

from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *
from MainScreen import *
from CalculateTax import *

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
    def __init__(self, parent, names, departments, DOBs, genders,
                 salaries, codes, searchIn, searchFor):
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
        self.searchIn = searchIn
        self.searchFor = searchFor

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

        statsMenu = Menu(menubar)

        statsMenu.add_command(label=STATS_TOTAL_EMP_TEXT, underline=0, command=self.TotalEmployees)
        statsMenu.add_command(label=STATS_TOTAL_MALE_TEXT, underline=0, command=self.TotalMale)
        statsMenu.add_command(label=STATS_TOTAL_FEMALE_TEXT, underline=0, command=self.TotalFemale)
        statsMenu.add_command(label=STATS_TOTAL_SALARY_TEXT, underline=0, command=self.TotalSalary)
        statsMenu.add_command(label=STATS_TOTAL_TAX_TEXT, underline=0, command=self.TotalTax)
        statsMenu.add_command(label=STATS_AVERAGE_SALARY_TEXT, underline=0, command=self.AverageSalary)
        statsMenu.add_command(label=STATS_AVERAGE_TAX_TEXT, underline=0, command=self.AverageTax)

        statsMenu.add_separator()
        
        menubar.add_cascade(label=DROPDOWN_FILE_TEXT, underline=0, menu=fileMenu)
        menubar.add_cascade(label=DROPDOWN_STATS_TEXT, underline=0, menu=statsMenu)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MENUBAR_INITIALISED_TEXT)

        TitleLabel = Label(text=SEARCH_FOR_TEXT + str(self.searchFor)
                           + SEARCH_FOR_IN_TEXT + str(self.searchIn) + SEARCH_FOR_END_TEXT, font=("Purisa", 16))

        TitleLabel.pack()

        AnchorLabel = Label(width=9)

        AnchorLabel.pack(side=LEFT)

        scrollbar = Scrollbar(self.parent)
        scrollbar.pack(side=RIGHT, fill=Y)

        listboxOne = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxOne.insert(END, NAME_TEXT)
        listboxOne.insert(END, SPACE_TEXT)
     
        for i in range(len(self.names)):
            listboxOne.insert(END, self.names[i])
            listboxOne.pack(side=LEFT, fill=BOTH)

        listboxOne.insert(END, SPACE_TEXT)

        listboxTwo = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxTwo.insert(END, DEPARTMENT_TEXT)
        listboxTwo.insert(END, SPACE_TEXT)

        for i in range(len(self.departments)):
            listboxTwo.insert(END, self.departments[i])
            listboxTwo.pack(side=LEFT, fill=BOTH)

        listboxTwo.insert(END, SPACE_TEXT)

        listboxThree = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxThree.insert(END, DOB_TEXT)
        listboxThree.insert(END, SPACE_TEXT)

        for i in range(len(self.DOBs)):
            listboxThree.insert(END, self.DOBs[i])
            listboxThree.pack(side=LEFT, fill=BOTH)
            
        listboxThree.insert(END, SPACE_TEXT)

        listboxFour = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxFour.insert(END, GENDER_TEXT)
        listboxFour.insert(END, SPACE_TEXT)

        for i in range(len(self.genders)):
            if self.genders[i] == MALE_SINGLE_TEXT:
                listboxFour.insert(END, MALE_TEXT)
            else:
                listboxFour.insert(END, FEMALE_TEXT)
            listboxFour.pack(side=LEFT, fill=BOTH)
            
        listboxFour.insert(END, SPACE_TEXT)

        listboxFive = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxFive.insert(END, SALARY_TEXT)
        listboxFive.insert(END, SPACE_TEXT)

        for i in range(len(self.salaries)):
            Salary = str(self.salaries[i])
            Tax = str(CalculateTax(Salary))
            SalaryAndTax = Salary + " [" + Tax + "]"
            listboxFive.insert(END, SalaryAndTax )
            listboxFive.pack(side=LEFT, fill=BOTH)

        listboxFive.insert(END, SPACE_TEXT)

        listboxSix = Listbox(self.parent, yscrollcommand=scrollbar.set)

        listboxSix.insert(END, EMP_CODE_TEXT)
        listboxSix.insert(END, SPACE_TEXT)

        for i in range(len(self.codes)):
            listboxSix.insert(END, self.codes[i])
            listboxSix.pack(side=LEFT, fill=BOTH)

        listboxSix.insert(END, SPACE_TEXT)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)

        scrollbar.config(command= self.yview)

    def TotalEmployees(self):
        CreatePopup(STAT_TOTAL_EMP_TEXT + str(len(self.codes)))

    def TotalFemale(self):
        TotalFemales = 0
        for i in range(len(self.genders)):
            if self.genders[i] == FEMALE_SINGLE_TEXT:
                TotalFemales += 1
        CreatePopup(STAT_TOTAL_FEMALE_TEXT + str(TotalFemales))

    def TotalMale(self):
        TotalMales = 0
        for i in range(len(self.genders)):
            if self.genders[i] == MALE_SINGLE_TEXT:
                TotalMales += 1
        CreatePopup(STAT_TOTAL_MALE_TEXT + str(TotalMales))

    def TotalSalary(self):
        TotalSalary = 0
        for salary in self.salaries:
            TotalSalary += int(salary)
        CreatePopup(STAT_TOTAL_SALARY_TEXT + str(TotalSalary))

    def TotalTax(self):
        TotalTax = 0
        for salary in self.salaries:
            TotalTax += CalculateTax(salary)
        CreatePopup(STAT_TOTAL_TAX_TEXT + str(TotalTax))
        
    def AverageSalary(self):
        TotalSalary = 0
        for salary in self.salaries:
            TotalSalary += int(salary)
        AverageSalary = TotalSalary/len(self.salaries)
        CreatePopup(STAT_AVERAGE_SALARY_TEXT + str(AverageSalary))

    def AverageTax(self):
        TotalTax = 0
        for salary in self.salaries:
            TotalTax += CalculateTax(salary)
        AverageTax = TotalTax/len(self.salaries)
        CreatePopup(STAT_AVERAGE_TAX_TEXT + str(AverageTax))

    def yview(self, *args):
        apply(listboxOne.yview, args)
        apply(listboxTwo.yview, args)
        apply(listboxThree.yview, args)
        apply(listboxFour.yview, args)
        apply(listboxFive.yview, args)
        apply(listboxSix.yview, args)

    def onBack(self):
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + BACK_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + WINDOW_TERMINATED_TEXT)
        root =Tk()
        root.geometry(WINDOW_GEOMETRY)
        app = Splash(root)
        root.mainloop()

    def Help(self):
        pass

'''
This section is used for testing the GUI.
It passes generic results in to ensure
that everything is formated as it should
be.
=========================================

alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
names = []
departments = []
DOBs = []
genders = []
salaries = []
codes = []
SearchFor = "Meow"
SearchIn = "Cake"
for i in range(50):
    name = ""
    for i in range(random.randint(5,17)):
        name += alphabet[random.randint(0,25)]
    names.append(name)
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
app = SearchResultsScreen(root, names, departments, DOBs, genders, salaries, codes, SearchIn, SearchFor)
                    
root.mainloop()
'''
