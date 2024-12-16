# Meal time problem
# author: jguerreiro

def main():
    time = input("What time is it? ")
    meal = mealTime(convert(time))
    
    print(meal)


def convert(time):
    """
      Converts time, a str in 24-hour format, to the corresponding number of hours as a float. 
      For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), 
      convert should return 7.5 (i.e., 7.5 hours).
    """
    # Find and set a time delimiter, ":"
    time_delimiter_index = time.find(":")
    # Store values from left to right until delimiter ":"
    hour = time[:time_delimiter_index]
    minutes = time[time_delimiter_index + 1:]

    # Cast float and round the strings
    hour_float = round(float(hour),1)
    minutes_float = round(float(minutes),1)

    # Ex: To transform 30 into 0.5, you need to divide 30 by 60
    minutes_to_fraction = minutes_float / 60

    converted_time = hour_float + minutes_to_fraction

    return converted_time

def mealTime(time):
    """
      Breakfast between 7:00 and 8:00
      Lunch between 12:00 and 13:00
      Dinner between 18:00 and 19:00
      Output: breakfast time, lunch time, or dinner time
    """
    meal_message = ""
    if time >= 7 and time <= 8:
        meal_message = "Breakfast time! 🍳"
    elif time >= 12 and time <= 13:
        meal_message = "Lunch time! 🍲"
    elif time >= 18 and time <= 19:
        meal_message = " Dinner time! 🍝"
    else:
        meal_message = " Not a meal time "

    return meal_message

if __name__ == "__main__":
    main()

