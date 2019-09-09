#--------------------------------------------------------------------------------------------------------
# Name: Technology Event (TechnologyClass.py)
# Purpose: Using the parent class to create techonology events for users
#
#
# Author: Nisarg Shah
# Created: 4-Jan-2018
# Updated: 17-Jan-2019
#--------------------------------------------------------------------------------------------------------

from EventClass import Event
class TechnologyEvent(Event):
    '''
    Technology event object which inherits from the Event class

    Attributes
    ----------


    Methods
    -------
    calculator()
        Calculates the amount of CO2 produced for a given event
    returnValues()
        Returns the attributes of the object
    '''

    def __init__(self, date, title, description, usageTime, subType):
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
        usageTime: float
            Hours the technology was used for
        subType: str
            Which tecnology was used
        '''
        self.usageTime = usageTime
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
        # 1 kwh = 0.554Kg of Co2 Produced, therfore waste procuded is 0.554*time(hours)*wattage/1000
        # all wattage values are approximate
        if self.subType == 'Smartphone':
            #28 watts (8 watts device, 20 watts router + cellular towers) 
            wastage = float(self.usageTime)*0.554*28/1000
            return wastage
        if self.subType == 'Tablet':
            #60 watts (50 watts device, 10 watts router)
            wastage = float(self.usageTime)*0.554*60/1000
            return wastage
        if self.subType == 'Computer':
            #110 watts (100 watts device, 10 watts router)
            wastage = float(self.usageTime)*0.554*110/1000
            return wastage
        if self.subType == 'Television':
            #400 watts (400 watts device)
            wastage = float(self.usageTime)*400/1000
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
        self.usageTime: float
            Hours device was used
        self.subType: float
            Type of device used
        'Technology': str
            Type of event
        
        '''
        return super().values(), self.usageTime ,self.subType, 'Technology'

