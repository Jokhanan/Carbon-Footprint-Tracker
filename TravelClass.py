#--------------------------------------------------------------------------------------------------------
# Name: Travel Event (TravelClass.py)
# Purpose: Using the parent class to create travel events for users
#
#
# Author: Nisarg Shah
# Created: 4-Jan-2018
# Updated: 17-Jan-2019
#--------------------------------------------------------------------------------------------------------
from EventClass import Event
class TravelEvent(Event):
    '''
    Travel event object which inherits from the Event class

    Attributes
    ----------


    Methods
    -------
    calculator()
        Calculates the amount of CO2 produced for a given event
    returnValues()
        Returns the attributes of the object
    '''

    def __init__(self, date, title, description, travelDistance, subType):
        '''
        Constructor funtion
        
        Parameters
        ----------
        date: str
            Date the event occured
        title: str
            Title of the event
        description: str
            Description of the event
        travelDistance: float
            Distance travelled with given mode of transportation
        subType: str
            Mode of transportation
        '''
        self.travelDistance = travelDistance
        self.subType = subType
        super().__init__(date, title, description)

    def calculator(self):
        '''
        Calculates the amount of CO2 produced for a given event

        Parameters
        ----------
        None

        Returns
        -------
        wastage: float
            The amount of CO2 created in Kg
        '''        
        #multiplication factors are Kg of CO2 produced per Km of Travel on average by these modes of travel
        if self.subType == 'Public Transit':
            wastage = float(self.travelDistance)*0.07
            return wastage
        if self.subType == 'Car':
            wastage = float(self.travelDistance)*0.1185
            return wastage
        if self.subType == 'Train':
            wastage = float(self.travelDistance)*0.028
            return wastage
        if self.subType == 'Airplane':
            wastage = float(self.travelDistance)*0.115
            return wastage

    def returnValues(self):
        '''
        Returns the attributes of the object

        Parameters
        ----------
        None

        Returns
        -------
        super.values(): list
            Inherited attributes
        self.travelDistance: float
            Distance Travelled using mode of transportation
        self.subType: float
            Mode of transportation used
        'Travel': str
            Type of event
        
        '''        
        return super().values(), self.travelDistance, self.subType, 'Travel'

