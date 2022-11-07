def Leap_Year(year=2023):
    """Returns whether the year
    is leap year or not.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return ('Leap Year.')
            else:
                return ("Not Leap Year.")
        else:
            return ('Leap Year.')
    else:
        return ('Not leap year.')