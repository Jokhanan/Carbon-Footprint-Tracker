#--------------------------------------------------------------------------------------------------------
# Name: CFET GUI (CFET.py)
# Purpose: To create a program in which a person can track their carbon footprint and overall emissions
#
#
# Author: Nisarg Shah
# Created: 9-Oct-2018
# Updated: 18-Jan-2019
#--------------------------------------------------------------------------------------------------------


from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from ProgramFunctions import signupCheck, login, profileCreation, eventCreation, eventHistoryComplier, emissionsScoreGenerator, leaderBoardScore, decimalLimiter


class GUI(tk.Tk):
    '''
    An Onject that holds all the Windows present in the GUI.

    Attributes
    ---------
    master: Tkinter Variable
        Command that connects all given tkinter commands to the tk/tcl interpreter
    mainFrame: Tkinter Variable
        The window of the GUI
    elements: list
        All the elements on a given page


    Methods
    ------
    clearPage(elements)
        Function that clears all page elements when called
    startPage()
        Page of the GUI where the user can signup or login
    signupPage()
        Page of the GUI where the user can create an account with a given username and password
    loginPage()
        Page of the GUI where the user can login to a previously created account
    profileCreationPage(tempUser, tempPass)
        Page of the GUI where the user creates a profile for their newly created account
    homePage(firstName, lastName)
        Page of the GUI where the user can access all the program functionality
    newEventPage(firstName, lastName)
        Page of the GUI where the user can add an event to their account
    eventHistoryPage(firstName, lastName, events)
        Page of the GUI where the user can view all of their previously created event
    emissionsOverviewPage(firstName, lastName, scoreBreakdown)
        Page of the GUI where the user can view their total emmisions per category
    leaderboardPage(self, firstName, lastName, scores, userScorePairings, currentUserRank)
        Page of the GUI where the user can see how their emmissions compare to other users
    '''

    def __init__(self,master):
        '''
        Constructor to build the GUI

        Parameters
        ----------
        master: Tkinter Variable
            Command that connects all given tkinter commands to the tk/tcl interpreter

        Returns
        -------
        None
        '''
        self.mainFrame = tk.Frame(master, bg = '#eae9e9').grid(column = 0, row = 0)
        root.configure(bg = '#eae9e9')#sets the background colour of the window
        self.titleFont = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.startPage()
  
        
    def clearPage(self, elements):
        '''
        Function that clears all page elements when called

        Parameters
        ---------
        elements: list
           All page elements

        Returns
        -------
        None
        '''
        for element in elements:
            element.destroy()
            
    def startPage(self):
        '''
        Page of the GUI where the user can signup or login

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''

        root.title("Start Page")
        root.geometry('350x200')
        
        title = tk.Label(self.mainFrame, text="Welcome to CFET", font = self.titleFont, bg = '#eae9e9')
        title.grid(column = 0, row = 0,padx =75, pady=10)
        
        signupButton = tk.Button(self.mainFrame, text="Signup",command=lambda:(self.clearPage(self.elements), self.signupPage()),overrelief = tk.GROOVE)
        signupButton.grid(column = 0, row = 1, pady = 10,ipadx = 75, ipady = 5)
        
        loginButton = tk.Button(self.mainFrame, text="Login", command=lambda:(self.clearPage(self.elements), self.loginPage()),overrelief = tk.GROOVE)
        loginButton.grid(column = 0, row = 2,pady= 15, ipadx = 78, ipady = 5)

        self.elements = [title, signupButton, loginButton]
            
    def signupPage(self):
        '''
        Page of the GUI where the user can create an account with a given username and password

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        root.title('Signup')
        root.geometry('350x225')
        
        title = tk.Label(self.mainFrame, text="Create Your Account",font = self.titleFont,  bg = '#eae9e9')
        title.grid(column = 1, row = 0, pady=10)
        
        userLabel = tk.Label(self.mainFrame,text='Username :', bg = '#eae9e9')
        userLabel.grid(column = 0, row = 1, sticky = 'e')

        passLabel = tk.Label(self.mainFrame,text='Password :', bg = '#eae9e9')
        passLabel.grid(column = 0, row = 2, sticky = 'e')

        passConfirmLabel = tk.Label(self.mainFrame,text='Confirm Password :', bg = '#eae9e9')
        passConfirmLabel.grid(column = 0, row = 3, sticky = 'e')

        newUser = tk.Entry(self.mainFrame, width = 25)
        newUser.grid(column = 1, row = 1, pady = 10)
        
        newPass = tk.Entry(self.mainFrame, width = 25, show ='*')
        newPass.grid(column = 1, row = 2, pady = 10)

        passConfirm =tk.Entry(self.mainFrame, width = 25, show ='*')
        passConfirm.grid(column = 1, row = 3, pady = 10)

        submitButton = tk.Button(self.mainFrame, text="Create",command=lambda: signupSuccess(), overrelief = tk.GROOVE)
        submitButton.grid(column = 1, row = 4, ipadx = 55, pady = 15)

        backButton = tk.Button(self.mainFrame, text="Cancel",command=lambda: (self.clearPage(self.elements),self.startPage()), overrelief = tk.GROOVE)
        backButton.grid(column = 0, row = 0)
        self.elements = [title, userLabel, passLabel, passConfirmLabel, newUser, newPass, passConfirm, submitButton, backButton]
        
        def signupSuccess():
            '''
            Checks for inconsistencies in entry fields (empty fields, non-matching passwords) if no errors comes up sends user to profile creation page

            Parameters
            ----------
            None

            Returns
            -------
            None
            '''
            if len(newUser.get()) == 0 or len(newPass.get())== 0 or len(passConfirm.get()) == 0: # if any of the fields are empty and error will be shown
                messagebox.showinfo("Fields Missing","Please Fill In The Appropriate Fields")
            elif newPass.get() != passConfirm.get():# if the two password fields do not match an error will be shown
                messagebox.showinfo("Input Error", "Passwords Do Not Match")
            elif signupCheck(newUser.get(), newPass.get()):# will return true if not problems occur, false if the username is already taken
                    tempUserHold = newUser.get()
                    tempPassHold = newPass.get()
                    self.clearPage(self.elements)
                    self.profileCreationPage(tempUserHold, tempPassHold)
            else:#if the username is already taken
                messagebox.showinfo("Input Error", "Username Already Exists")

                


    def loginPage(self):
        '''
        Page of the GUI where the user can login to a previously created account

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        root.title('Login')
        root.geometry('350x200')        
        title = tk.Label(self.mainFrame, text="Login To Your Account", font=self.titleFont, bg = '#eae9e9')
        title.grid(column = 1, row = 0, pady=10)
        
        userLabel = tk.Label(self.mainFrame,text='Username :', bg = '#eae9e9')
        userLabel.grid(column = 0, row = 1)

        passLabel = tk.Label(self.mainFrame,text='Password :', bg = '#eae9e9')
        passLabel.grid(column = 0, row = 2)

        submitUser = tk.Entry(self.mainFrame, width = 25)
        submitUser.grid(column = 1, row = 1, pady = 10)
        
        submitPass = tk.Entry(self.mainFrame, width = 25, show ='*')
        submitPass.grid(column = 1, row = 2, pady = 10)

        submitButton = tk.Button(self.mainFrame, text="Login",command=lambda: loginSuccess(), overrelief = tk.GROOVE)
        submitButton.grid(column = 1, row = 3, pady = 15, ipadx = 55)

        backButton = tk.Button(self.mainFrame, text="Cancel",command=lambda: (self.clearPage(self.elements),self.startPage()), overrelief = tk.GROOVE)
        backButton.grid(column = 0, row = 0)
        
        self.elements = [title, userLabel, passLabel, submitUser, submitPass, submitButton, backButton]
    
        def loginSuccess():
            '''
            Calls a function that checks username and password fields, any inconsitencies will create an error, if no errors come up sends user to home page
            
            Parameters
            ----------
            None

            Returns
            -------
            None
            '''

            if login(submitUser.get(), submitPass.get()):# Function returns true when login credentials are valid
                userFirstName = login(submitUser.get(), submitPass.get())[0]
                userLastName = login(submitUser.get(), submitPass.get())[1]
                self.clearPage(self.elements)
                self.homePage(userFirstName,userLastName)
            else:#error is shown when login credentials are not valid
                messagebox.showinfo("Input Error", "Invalid Username and/or Password")

    def profileCreationPage(self, tempUser, tempPass):
        '''
        Page of the GUI where the user creates a profile for their newly created account
        
        Parameters
        ----------
        tempUser: str
            username the user signed up with
        tempPass: str
            password the user signed up with

        Returns
        -------
        None
        '''
        self.clearPage(self.elements)
        root.title('Create Your Profile')
        root.geometry('300x270')

        title = tk.Label(self.mainFrame, text="Create Your Profile", font = self.titleFont, bg = '#eae9e9')
        title.grid(column=0, columnspan = 2, row = 0,pady= 10, sticky = "N")

        firstNameLabel = tk.Label(self.mainFrame,text='First Name :', bg = '#eae9e9')
        firstNameLabel.grid(column = 0, row = 1,sticky= "E", padx= 10)

        lastNameLabel = tk.Label(self.mainFrame,text='Last Name :', bg = '#eae9e9')
        lastNameLabel.grid(column = 0, row = 2,sticky= "E", padx= 10)

        dobLabel = tk.Label(self.mainFrame,text='Date of Birth :', bg = '#eae9e9')
        dobLabel.grid(column = 0, row = 3,sticky= "E", padx= 10)

        locLabel = tk.Label(self.mainFrame,text='Place of Residence :', bg = '#eae9e9')
        locLabel.grid(column = 0, row = 4,sticky= "E", padx= 10)

        submitFirstName= tk.Entry(self.mainFrame, width = 25)
        submitFirstName.grid(column = 1, row = 1, pady = 10)

        submitLastName = tk.Entry(self.mainFrame, width = 25)
        submitLastName.grid(column = 1, row = 2, pady = 10)

        submitDOB = tk.Entry(self.mainFrame, width = 25)
        submitDOB.grid(column = 1, row = 3, pady = 10)

        submitLoc = tk.Entry(self.mainFrame, width = 25)
        submitLoc.grid(column = 1, row = 4, pady = 10)
        
        submitButton = tk.Button(self.mainFrame, text="Submit",command=lambda: profileCreated(tempUser, tempPass),overrelief = tk.GROOVE)
        submitButton.grid(column = 0, row = 5,columnspan = 2, ipadx = 25,pady = 15, sticky="N")
        
        self.elements= [title, firstNameLabel, lastNameLabel, dobLabel, locLabel, submitFirstName,
                   submitLastName, submitDOB, submitLoc, submitButton]
        
        def profileCreated(tempUser, tempPass):
            '''
            Checks for inconsistencies in the entry fields, if no errors calls a function that creates a new user and then sends user to home page

            Parameters
            ----------
            tempUser: str
                username the user signed up with
            tempPass: str
                password the user signed up with

            Returns
            -------
            None
            '''
            if len(submitFirstName.get()) == 0 or len(submitLastName.get()) == 0 or len(submitDOB.get()) == 0 or len(submitLoc.get()) == 0:#if any fields are empty an error is shown
                messagebox.showinfo("Fields Missing","Please Fill In The Appropriate Fields")
            else:
                profileCreation(tempUser, tempPass, submitFirstName.get(), submitLastName.get(), submitDOB.get(), submitLoc.get())#calls a function that will update the login file and create a user file

                userFirstName = submitFirstName.get()
                userLastName = submitLastName.get()
                self.clearPage(self.elements)
                self.homePage(userFirstName, userLastName)

    def homePage(self, firstName, lastName):
        '''
        Page of the GUI where the user can access all the program functionality

        Parameters
        ----------
        firstName: str
            First name of the user
        lastName: str
            Last name of the user
        '''
        self.clearPage(self.elements)
        root.title('Home')
        root.geometry('350x250')
        
        title = tk.Label(self.mainFrame, text= 'Home', font=self.titleFont, bg = '#eae9e9')
        title.grid(column=0, row = 0, padx = 140, pady= 10, sticky = "N")
        
        newEventButton = tk.Button(self.mainFrame, text="New Event", width = 17,
                                   command=lambda: (self.clearPage(self.elements),self.newEventPage(firstName, lastName)),overrelief = tk.GROOVE)
        newEventButton.grid(column = 0, row = 1, pady = 10, sticky = "N")

        eventHistoryButton = tk.Button(self.mainFrame, text="Event History", overrelief = tk.GROOVE, width = 17,
                                       command=lambda: historySetup(firstName, lastName))
        eventHistoryButton.grid(column = 0, row = 2, pady = 10)
        
        emissionBreakdownButton = tk.Button(self.mainFrame, text="Emission Breakdown",width = 17, overrelief = tk.GROOVE,
                                            command= lambda: overviewSetup(firstName, lastName))
        emissionBreakdownButton.grid(column = 0, row = 3, pady = 10)

        leaderboardButton = tk.Button(self.mainFrame, text="Leaderboard", width = 17, overrelief = tk.GROOVE,
                                      command = lambda:leaderboardSetup(firstName, lastName))
        leaderboardButton.grid(column = 0, row = 4, pady = 10,)

        self.elements= [title,newEventButton,  eventHistoryButton, emissionBreakdownButton, leaderboardButton]

        def historySetup(firstName, lastName):
            '''
            Setup for event history page, using the complier function appropriate variables are defined and the user is sent to the event history page
               
            Parameters
            ---------
            None

            Returns
            ------
            '''
            events = eventHistoryComplier(firstName, lastName)#puts all event objects into a list
            self.clearPage(self.elements)
            self.eventHistoryPage(firstName, lastName, events)

        def overviewSetup(firstName, lastName):
            '''
            Setup for emissions breakdown page, using the complier function appropriate variables are defined and the user is sent to the emissions breakdown page
               
            Parameters
            ---------
            None

            Returns
            ------
            '''
            scores = emissionsScoreGenerator(firstName, lastName)
            self.clearPage(self.elements)
            self.emissionsOverviewPage(firstName, lastName, scores)

        def leaderboardSetup(firstName, lastName):
            '''
            Setup for leaderboard page, using the complier function appropriate variables are defined and the user is sent to the leaderboard page
               
            Parameters
            ---------
            None

            Returns
            ------
            '''
            self.clearPage(self.elements)
            scores, userScorePairings, currentUserRank = leaderBoardScore(firstName, lastName)
            self.leaderboardPage(firstName, lastName, scores, userScorePairings, currentUserRank)



    def newEventPage(self, firstName, lastName):
        '''
         Page of the GUI where the user can add an event to their account

        Parameters
        ----------
        firstName: str
            First name of the user
        lastName: str
            Last name of the user
        '''
        root.title('Home')
        root.geometry('350x260')

        title = tk.Label(self.mainFrame,text="Event Type", font=self.titleFont, bg = '#eae9e9')
        title.grid(column=0, row = 0, padx = 105, pady= 10, sticky = "N")
        
        technologyButton = tk.Button(self.mainFrame, text = 'Techonology', height = 1, width = 15,
                            command= lambda: (self.clearPage(self.elements), newEventInfo(firstName, lastName, 'Technology')),overrelief = tk.SUNKEN)
        technologyButton.grid(column = 0, row = 1, pady = 25)

        travelButton = tk.Button(self.mainFrame, text = 'Travel',height = 1 ,width = 15,overrelief = tk.SUNKEN,
                                 command= lambda: (self.clearPage(self.elements), newEventInfo(firstName, lastName, 'Travel')))
        travelButton.grid(column = 0, row = 2, pady = 10)

        cancelButton = tk.Button(self.mainFrame, text = 'Cancel', width = 5, height = 1,
                                 command = lambda:(self.clearPage(self.elements), self.homePage(firstName, lastName)),overrelief = tk.SUNKEN)
        cancelButton.grid(column = 0, row = 3 , padx = 5, pady = 10)

        disclaimerLabel = tk.Label(self.mainFrame, text = 'Note: Created Events Cannot Be Deleted or Edited', bg = '#eae9e9')
        disclaimerLabel.grid(column =0, row =4, padx = 15)
        self.elements = [title, technologyButton, travelButton, cancelButton, disclaimerLabel]

        def newEventInfo(firstName, lastName, eventType):
            '''
            Page which user can input specific event details for the Type of event they want to add

            Parameters
            ----------
            None

            Returns
            -------
            None
            '''
            root.geometry('350x375')
            title = tk.Label(self.mainFrame,text="Event Creation", font=self.titleFont, bg = '#eae9e9')
            title.grid(column=0, row = 0, pady= 10, columnspan = 5)

            #changes drop down menu options depending on event type 
            subTypeVar = StringVar(root)
            if eventType == 'Technology':
                subTypes = {'Smartphone', 'Computer', 'Tablet', 'Television'}
            elif eventType == 'Travel':
                subTypes = {'Car', 'Train', 'Public Transit', 'Airplane'}
            subTypeVar.set('Select')

            if eventType == 'Technology':
                subTypeLabel = tk.Label(self.mainFrame, text = 'Techonological Device:', bg = '#eae9e9')
            elif eventType == 'Travel':
                subTypeLabel = tk.Label(self.mainFrame, text = 'Travel Method:', bg = '#eae9e9')
                
            
            subTypeLabel.grid(column = 0, row = 1,columnspan =2, sticky = 'w', padx = 10)
            
            dropMenu = tk.OptionMenu(self.mainFrame, subTypeVar, *subTypes)
            dropMenu.config(width =14)
            dropMenu.grid(column= 0, row = 2,columnspan =2, sticky = 'w', padx = 10)
            # label changes depending on type of event being created
            if eventType == 'Technology':
                amountLabel = tk.Label(self.mainFrame, text= 'Time (Hours):',bg = '#eae9e9')
            elif eventType == 'Travel':
                amountLabel = tk.Label(self.mainFrame, text= 'Distance (Km):',bg = '#eae9e9')
            
            amountLabel.grid(column = 3, row = 1,columnspan = 2, sticky = 'e', padx = 27)

            amountEntry = tk.Entry(self.mainFrame, width = 20)
            amountEntry.grid(column = 3, row = 2, columnspan = 2, sticky = 'e', padx = 10)

            eventTitleLabel = tk.Label(self.mainFrame, text= 'Event Title:',bg = '#eae9e9')
            eventTitleLabel.grid(column = 0, row = 3, sticky = 'w', padx = 10, pady= 8)
            
            eventTitleEntry = tk.Entry(self.mainFrame,width = 40)
            eventTitleEntry.grid(column = 1, row = 3, columnspan=4, padx= 10, pady = 8, sticky = 'w')

            dateLabel = tk.Label(self.mainFrame, text= 'Date:',bg = '#eae9e9')
            dateLabel.grid(column = 0, row = 4, sticky = 'w', padx = 10, pady= 8)

            dateEntry = tk.Entry(self.mainFrame,width = 40)
            dateEntry.grid(column = 1, row = 4, columnspan=4, padx= 10, pady = 8, sticky = 'w')

            

            descriptionLabel = tk.Label(self.mainFrame, text= 'Event Discription:',bg = '#eae9e9')
            descriptionLabel.grid(column = 0, row = 5, columnspan= 2, padx = 10, pady = 5, sticky = 'w')
            
            descriptionEntry = tk.Text(self.mainFrame, width =40, height = 7, wrap ='word')            
            descriptionEntry.grid(column = 0, row = 6, columnspan = 5, padx = 10)
            
            
            submitButton = tk.Button(self.mainFrame,text = 'Submit', width =12, overrelief = tk.SUNKEN,
                                     command=lambda:eventCreationCheck(firstName, lastName, dateEntry.get(), eventType, subTypeVar.get(),
                                                        amountEntry.get(),eventTitleEntry.get(), descriptionEntry.get('1.0', 'end-1c')))
            submitButton.grid(column = 0, row = 7,columnspan = 2, pady = 8, sticky = 'e')
            
            discardButton = tk.Button(self.mainFrame, text = 'Discard', width = 12, overrelief = tk.SUNKEN,
                               command = lambda:(self.clearPage(self.elements), self.newEventPage(firstName, lastName)))
            discardButton.grid(column = 3, row = 7,columnspan = 2, pady = 8, sticky = 'w')


            

            self.elements = [title, subTypeLabel, dropMenu, amountLabel, amountEntry, eventTitleLabel, dateLabel, dateEntry,
                             eventTitleEntry, descriptionLabel, descriptionEntry, submitButton, discardButton]
            
            def enterKey(event):
                '''
                Stops use of 'enter' key in the description page

                Parameters
                ----------
                event: Event Handler
                    function only runs when the given event occurs

                Returns
                -------
                'break'
                    command to ignore the 'enter' key
                '''
                return 'break'
            descriptionEntry.bind('<Return>', enterKey)            

            
        def eventCreationCheck(firstName, lastName,eventDate, eventType, eventSubType, eventAmount, eventTitle, eventDescription):
            '''
            Checkes for inconsistencies in the inputted data (unfilled fields, negative or alphabetical inputs in number fields) if no inconsistencies are present,
            an event is creted and the user is prompted while being sent to the home page

            Parameters
            ---------
            firstName: str
                First name of the user
            lastName: str
                Last name of the user
            eventDate: str
                Date the event occured
            eventType: str
                Category/type of event
            eventSubType: str
                Subtype of event
            eventAmount: float
                The amount a given subtype was used
            eventTitle: str
                The title of the event
            eventDescription:str
                The description of the event

            Returns
            -------
            None

            Raises
            ------
            ValueError:
                When eventAmount is a string and it can not be converted to a float
            '''
            if len(eventAmount)== 0 or len(eventTitle) == 0 or len(eventDescription) ==0 or len(eventDate) == 0 or eventSubType == 'Select':#if any of the fields are empty an error is shown
                messagebox.showinfo("Fields Missing","Please Fill In The Appropriate Fields")
            else:
                try:
                    eventAmount = float(eventAmount)
                except ValueError: # if the value entered in the amount field is a string, program will throw an error
                    if eventType == 'Technology':
                        messagebox.showinfo("Incorrect Value","Please Enter Number Amount In the Time Field ")
                    elif eventType =='Travel':
                        messagebox.showinfo("Incorrect Value","Please Enter Number Amount In the Distance Field ")
                        return
                if eventAmount < 0: # if the amount is negative and error will be thrown
                    if eventType == 'Technology':
                        messagebox.showinfo("Incorrect Value","Please Enter a Positive Number Amount In the Time Field ")
                    elif eventType =='Travel':
                        messagebox.showinfo("Incorrect Value","Please Enter a Positive Number Amount In the Distance Field ")
                    return
                
                eventCreation(firstName, lastName,eventType, eventSubType, eventDate, eventTitle, eventAmount, eventDescription)
                messagebox.showinfo("Event Success","Event Created")
                self.clearPage(self.elements)
                self.homePage(firstName, lastName)
            
    def eventHistoryPage(self, firstName, lastName, events):
        '''
        Page of the GUI where the user can view all of their previously created event

        Parameters
        ----------
        firstName: str
            First name of user
        lastName: str
            Last name of user
        events: list
            all logged events of user
            
        Returns
        -------
        None
        '''
        root.title('Event History')
        root.geometry('250x400')

        title = tk.Label(self.mainFrame, text ='Your History',font=self.titleFont,bg = '#eae9e9')
        title.grid(column = 0, row= 0, columnspan =2, ipady =15)
        

        scrollBar = tk.Scrollbar(self.mainFrame, orient = tk.VERTICAL)
        scrollBar.grid(column = 1, row= 1, sticky = 'ns')
        
        
        canvas = tk.Canvas(self.mainFrame, bd=0, width = 225, yscrollcommand=scrollBar.set)
        canvas.grid(column = 0, row = 1, pady = 5)
        scrollBar.config(command=canvas.yview)


        
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)
        def configInterior(event):
            '''
            Edits the itnerior of the canvas when the scrollbar is used

            Parameters
            ----------
            event: eventHandler
                function only runs when defined event occurs

            Returns
            -------
            None
            '''
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
        interior.bind('<Configure>', configInterior)

        #lists events from most recently logged to oldest
        events.reverse()
        for i in range(len(events)):
            #populates the canvas with the event objects and using their returnValue functions
            eventTitle = events[i].returnValues()[0][1]
            if len(eventTitle) > 15:
                eventTitle = eventTitle[0:15] + "..."
            tk.Label(self.interior, text = eventTitle, justify = tk.LEFT).grid(column = 0, row = i + 1, ipadx= 20, sticky = 'w')
            tk.Button(self.interior, height=1, width=10, text='Details',overrelief = tk.SUNKEN,
                      command= lambda i=i: eventDetails(events[i])).grid(column = 1, row = i + 1 ,padx=10, pady=5, sticky = 'e')

            
        backButton = tk.Button(self.mainFrame, text = 'Back to Home', overrelief = tk.SUNKEN,
                               command = lambda:(self.clearPage(self.elements), self.homePage(firstName, lastName)))
        backButton.grid(column = 0, row = 2, pady = 10)
        self.elements = [title, scrollBar,canvas, backButton]

        def eventDetails(eventObject):
            '''
            Creates a messagebox with all the event details obtained from the onject methods

            Parameters
            ----------
            eventObject: object
                Event object the user wants to view the details of
                
            Returns
            -------
            None
            
            '''
            if eventObject.returnValues()[3]== 'Technology':
                amountLabel = 'Time Used (Hourse): '
            else:
                amountLabel = 'Distance Travelled (Km): '
            messagebox.showinfo(eventObject.returnValues()[0][1],
                                'Event Type: '+ eventObject.returnValues()[3] +'\n'+
                                'Event Title: ' + eventObject.returnValues()[0][1] + '\n' +
                                'Event Date: '+ eventObject.returnValues()[0][0] +'\n'+
                                'Event Subtype: '+ eventObject.returnValues()[2] +'\n'+
                                amountLabel + eventObject.returnValues()[1] +'\n'+
                                'Waste Created: ' + decimalLimiter(eventObject.calculator()) + 'Kg' + '\n' +
                                'Event Description: ' + '\n'+
                                eventObject.returnValues()[0][2])#message box that displays all event details

    def emissionsOverviewPage(self, firstName, lastName, scoreBreakdown):
        '''
        Page of the GUI where the user can view their total emmisions per category

        Parameters
        ----------
        firstName: str
            First name of user
        lastName: str
            Last name of user
        scoreBreakdown: list
            User scores per cateogory

        Returns
        -------
        None 
        '''
        root.title('Emissions Overview')
        root.geometry('350x320')

        
        title = tk.Label(self.mainFrame, text= 'Score Breakdown (Kg)',
                         font=tkfont.Font(family='Helvetica', size=18, slant = 'italic', weight = 'bold'),bg = '#eae9e9')
        title.grid(column = 0, row = 0,columnspan = 2)

        totalScore = tk.Label(self.mainFrame, text= 'Total Wastage: ' + str(scoreBreakdown[0]), bg = '#eae9e9',
                              font =  tkfont.Font(family='Helvetica', size=14, weight = 'bold'))
        totalScore.grid(column= 0, row= 1, pady = 15, columnspan = 2)

        techonologyScore = tk.Label(self.mainFrame, text= 'Techonology: ' + str(sum(scoreBreakdown[1:5]) ), bg = '#eae9e9',
                              font =  tkfont.Font(family='Helvetica', size=12, slant = 'italic'))
        
        techonologyScore.grid(column = 0, row = 2, sticky = 'w', ipadx = 10)

        phoneScore = tk.Label(self.mainFrame, text = 'Smart Phone: ' + str(scoreBreakdown[1]),  bg = '#eae9e9')
        phoneScore.grid(column = 0 ,row = 3, padx = 50, sticky = 'w', pady = 5)

        computerScore = tk.Label(self.mainFrame, text= 'Computer: ' + str(scoreBreakdown[3]), bg = '#eae9e9')
        computerScore.grid(column = 1, row = 3, padx = 30, sticky = 'w')

        tabletScore = tk.Label(self.mainFrame, text = 'Tablet: ' + str(scoreBreakdown[2]),  bg = '#eae9e9')
        tabletScore.grid(column = 0 ,row = 4, padx = 50, sticky = 'w', pady = 10)

        tvScore = tk.Label(self.mainFrame, text = 'Televison: ' + str(scoreBreakdown[4]),  bg = '#eae9e9')
        tvScore.grid(column = 1, row = 4, padx = 30, sticky = 'w')

        travelScore = tk.Label(self.mainFrame, text= 'Travel: ' + str(sum(scoreBreakdown[5:9])), bg = '#eae9e9',
                              font =  tkfont.Font(family='Helvetica', size=12, slant = 'italic'))
        travelScore.grid(column = 0, row = 5, sticky = 'w', ipadx = 10)
        
        transitScore = tk.Label(self.mainFrame, text = 'Public Transit: ' + str(scoreBreakdown[5]),  bg = '#eae9e9')
        transitScore.grid(column = 0 ,row = 6, padx = 50, sticky = 'w', pady = 5)

        carScore = tk.Label(self.mainFrame, text= 'Car: ' + str(scoreBreakdown[7]), bg = '#eae9e9')
        carScore.grid(column = 1, row = 6, padx = 30, sticky = 'w')

        trainScore = tk.Label(self.mainFrame, text = 'Train: ' + str(scoreBreakdown[6]),  bg = '#eae9e9')
        trainScore.grid(column = 0 ,row = 7, padx = 50, sticky = 'w', pady = 10)

        airplaneScore = tk.Label(self.mainFrame, text = 'Airplane: ' + str(scoreBreakdown[8]),  bg = '#eae9e9')
        airplaneScore.grid(column = 1, row = 7, padx = 30, sticky = 'w')

        backButton = tk.Button(self.mainFrame, text = 'Back', overrelief = tk.SUNKEN, width = 8,
                               command=lambda:(self.clearPage(self.elements), self.homePage(firstName, lastName)))
        backButton.grid(column = 0, row = 8, columnspan =2)
        
        self.elements = [title, totalScore, techonologyScore, phoneScore, computerScore, tabletScore, tvScore,
                         travelScore, transitScore, carScore, trainScore, airplaneScore, backButton]
        
    def leaderboardPage(self, firstName, lastName, scores, userScorePairings, currentUserRank):
        '''
        Page of the GUI where the user can see how their emmissions compare to other users

        Parameters
        ----------
        firstName: str
            First name of user
        lastName: str
            Last name of usr
        scores: list
            Top 10 (or less) scores among all users
        userScorePairings: dictionary
            All user scores associated with the names of the users
        currentUserRank: int
            Current user rank among all users

        Returns
        -------
        None
        '''
        root.title('Leaderboard')
        #size of window depends on number of people on the leaderboard
        windowY = 180 + 20*len(scores)
        root.geometry('310x' + str(windowY))
        
        title = tk.Label(self.mainFrame, text= 'Top Users', font=self.titleFont,bg = '#eae9e9')
        title.grid(column = 0, row = 0, columnspan = 2, pady = 10)

        nameInfoLabel = tk.Label(self.mainFrame, text= 'User:',bg = '#eae9e9')
        nameInfoLabel.grid(column = 0, row = 1, pady = 5)

        scoreInfoLabel = tk.Label(self.mainFrame, text= 'Score (Kg):',bg = '#eae9e9')
        scoreInfoLabel.grid(column = 1, row = 1, pady = 5)        
        
        self.elements = [title, nameInfoLabel, scoreInfoLabel]

        #populates the leaderboard
        for i in range(len(scores)):
            rankingNames = tk.Label(self.mainFrame, text = str(i+1) + ".   " +  userScorePairings[str(scores[i])],bg = '#eae9e9')
            rankingNames.grid(column = 0, row = i+2, sticky = 'w', padx = 25)

            rankingScores = tk.Label(self.mainFrame, text = decimalLimiter(str(scores[i])), bg = '#eae9e9')
            rankingScores.grid(column = 1, row = i+2, sticky = 'w', padx = 20)

            self.elements.append(rankingNames)
            self.elements.append(rankingScores)
            
            if i == len(scores) - 1:#once they last leaderboard entry is filled, creates a back button and displays the users rank
                userRankLabel = tk.Label(self.mainFrame, text = 'Your Rank: ' + str(currentUserRank),bg = '#eae9e9')
                userRankLabel.grid(column = 0, row = i + 3 ,columnspan = 2, pady = 10)
                self.elements.append(userRankLabel)
                
                backButton = tk.Button(self.mainFrame, text = 'Back', overrelief = tk.SUNKEN, width = 15,
                               command=lambda:(self.clearPage(self.elements), self.homePage(firstName, lastName)))
                backButton.grid(column = 0, row = i + 4 ,columnspan = 2, pady = 5)
                self.elements.append(backButton)


        

           

global root

root = Tk()#calls the tcl/tk interpreter

window = GUI(root)#creates the GUI object using the interpreter
root.resizable(width=False, height=False)
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))#places window on center of screen
root.mainloop()#runs the GUI object on a loop using the tcl/tk interpreter
