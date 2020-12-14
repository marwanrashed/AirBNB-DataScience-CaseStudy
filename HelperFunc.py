# Import nessecary packages and libararies

import pandas as pd
import numpy as np
from datetime import datetime
import re
import sklearn as sk

class HelperFunction ():

    def desired_features (self,listing_df, columns_list):
        '''
        Input: 
        listing_df: the listings dataframe for the given city.
        column_list: list of features to be removed. 
        -----------------------------------------------------
        Output:
        returns a dataframe with the desired features.
        '''
        return listing_df.drop(columns = columns_list)

    def fix_price (self,x):
        '''
        Input: price with alphanumeric and character signs. (string) 
        Output: price without any alphanumeric sign. (float)
        '''
        trans_string = x.split('$')[1].split('.')[0]
        return     self.to_float(self.remove_alphanum(trans_string))

    def fix_rate (self,x):
        '''
        Input: rate with alphanumeric and character signs. (string) 
        Output: rate without any alphanumeric sign. (int)
        '''
        return     self.to_int(self.remove_alphanum(x))

    def remove_alphanum (self,x):
        '''
        Input: string with alphanumeric and character signs. 
        Output: string without any alphanumeric sign.
        '''    
        return     re.sub(r'[^\w]','', x)

    def to_int (self,x):
        '''
        Input: string 
        Output: int
        '''    
        return     int(x)
    def to_float (self,x):
        '''
        Input: string 
        Output: float
        '''    
        return     float(x)    
    def weekday (self,x):
        '''
        Input: weekday number from 0 to 6. (int)
        Output: returns the corresponding day name. (string)
        '''
        week_dict = {0:'Monday', 1: 'Tuesday', 2: 'Wednesday'
        , 3: 'Thursday',4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        if x not in week_dict.keys() : 
            raise Exception("Wrong entry: Not a weekday valid number")
        for day_num, day_name in week_dict.items(): 
            if x == day_num: return day_name