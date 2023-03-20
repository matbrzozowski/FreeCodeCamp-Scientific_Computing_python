def add_time(start, duration, days = None):

    week_days = {   "Monday" : 0, 
                    "Tuesday" : 1, 
                    "Wednesday" : 2, 
                    "Thursday" : 3, 
                    "Friday" : 4, 
                    "Saturday" : 5, 
                    "Sunday" : 6}

    new_time = ""

    am_pm = start.split()[1]
    start_time = start.split()[0]
    start_hours = int(start_time.split(":")[0])
    start_minutes = int(start_time.split(":")[1])

    add_hours = int(duration.split(":")[0])
    add_minutes = int(duration.split(":")[1])


    # Start time in 24h format (hours)

    if am_pm == "PM":
        start_hours += 12

    # Total number of hours and minutes calculation

    hours = start_hours + add_hours + (start_minutes + add_minutes)//60
    minutes = (start_minutes + add_minutes)%60

    # Number of days

    number_days = hours//24

    # AM or PM

    if hours % 24 <= 11:
        am_pm = "AM"
    else:
        am_pm = "PM"

    # Trasnforming hours back to 12h format 

    hours = (hours % 24)%12

    if hours == 0:
        hours = 12

    hours = str(hours)
    
    # Transforming minutes to 2 digits format always

    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
   
    
    final_time = hours + ":" + minutes + " " + am_pm
    
    
    
    # Final time with number of days

    if days == None:
        if number_days == 0:
            new_time = final_time
            return new_time
        
        elif number_days == 1:
            new_time = final_time + " (next day)"
            return new_time
        
        elif number_days > 1:
            new_time = final_time + " (" + str(number_days) + " days later)"
            return new_time
        
    else:
        day_of_the_week = (week_days[days.lower().capitalize()] + number_days) % 7

        for x,y in week_days.items():
            if y == day_of_the_week:
                day_of_the_week = x
                break

        if number_days == 0:
            new_time = final_time + ", " + day_of_the_week
            return new_time
        if number_days == 1:
            new_time = final_time + ", " + day_of_the_week + " (next day)"
            return new_time
        
        new_time = final_time + ", " + day_of_the_week + " (" + str(number_days) + " days later)"


    return new_time
