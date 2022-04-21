#!/usr/bin/env python3
# -*- coding: utf-8 -*-
######################

import datetime
import time

def getDateRangeFromWeek(p_year,p_week):

    firstdayofweek = datetime.datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastdayofweek = firstdayofweek + datetime.timedelta(days=6.9)

    return firstdayofweek, lastdayofweek

if __name__ == '__main__':

    year = '2022'
    week = '10'

    #Call function to get dates range 
    firstdate, lastdate =  getDateRangeFromWeek(year,week)

    print('Date range for %s week in %s year: %s - %s' %(week,year,firstdate,lastdate))
