#--------------------------------------------------------------------------------------------------------
# Name: Event Parent Class (EventClass.py)
# Purpose: Parent Class for all event objects
#
#
# Author: Nisarg Shah
# Created: 4-Jan-2018
# Updated: 17-Jan-2019
#--------------------------------------------------------------------------------------------------------
class Event:
    '''
    A class which can be used to define any event object

    Attributes
    ----------
    date: str
        Date the event occured
    title: str
        Title of the event
    description: str
        Description of the event

    Methods
    -------
    values()
        Returns the attributes of the event object
    '''
    def __init__(self, date, title, description):
        self.date = date
        self.title = title
        self.description = description


                
    def values(self):
        '''
        Returns the attributes of the event object

        Parameters
        ----------
        None

        Returns
        -------
        self.date: str
            Date the event occured
        self.title: str
            Title of the event
        self.description: str
            Description of the event
        '''
        return self.date, self.title, self.description



