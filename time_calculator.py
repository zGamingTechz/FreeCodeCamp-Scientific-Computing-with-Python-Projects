def add_time(start, duration, dayOfWeek=None):

  #variables
  try:
    startArr = start.split(' ')
    startTime = startArr[0].split(':')
    ampm = 'AM'
    durationTime = duration.split(':')
  
    dayNames = {
      'monday':0,
      'tuesday':1,
      'wednesday':2,
      'thursday':3,
      'friday':4,
      'saturday':5,
      'sunday':6
    }
    
    tmpEndHour = (int(startTime[0]) + int(durationTime[0]))
  except ValueError:
    raise ValueError("Error: Start time must be in the 12 hour clock format (ending in AM or PM)\nEg. 12:00 AM")
  
  if startArr[1] == 'PM':
      tmpEndHour += 12
  
  tmpEndMinute = (int(startTime[1]) + int(durationTime[1]))
  
  if(tmpEndMinute > 59):
      tmpEndHour += 1
 
  days = int(tmpEndHour//24)
  endHour = tmpEndHour % 24

  if endHour > 11:
      ampm = 'PM'
  
  if endHour > 12:
      endHour -= 12
  elif endHour == 0:
      endHour = 12
  
  endMinute = tmpEndMinute % 60

  new_time = str(endHour) + ':' + str(endMinute).zfill(2) + ' ' + ampm

  #checking if user inputted 3rd arguement
  if dayOfWeek is not None:
    week = dayOfWeek.lower()
    weekdayNum = dayNames[week]
    newWeekdayNum = (days + weekdayNum) % 7
    newWeek = list(dayNames.keys())[list(dayNames.values()).index(newWeekdayNum)]
    new_time += ', ' + newWeek.capitalize()
  
  if days > 1:
    new_time += ' (' + str(days) + ' days later)'
  elif days > 0:
    new_time += ' (next day)'
  
  return new_time
