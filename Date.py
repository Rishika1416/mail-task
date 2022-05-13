from datetime import date
import datetime

from numpy import true_divide
class Date_:
    def __init__(self,date):
        self.date=date
    def find_month(self,month):
        match month:
            case 'January':
                return 1
            case 'February':
                return 2
            case 'March':
                return 3
            case 'April':
                return 4
            case 'May':
                return 5
            case 'June':
                return 6
            case 'July':
                return 7
            case 'August':
                return 8
            case 'September':
                return 9
            case 'October':
                return 10
            case 'November':
                return 11
            case 'December':
                return 12
    def convert_date_in_numbers(self):
        month=self.date.split(' ',1)[0]
        self.month=self.find_month(month)
        temp=self.date.split(', ',1)
        self.day=int(temp[0].split(' ')[1])
        self.year=int(temp[1].split(' ')[0])
    def match_date(self):
        today = str(date.today())
        #print(today)
        datem = datetime.datetime.strptime(today, "%Y-%m-%d")
        #print(type(datem.day))
        if datem.day==self.day and datem.month==self.month and datem.year==self.year:
            return True
        else:
            return False 
        