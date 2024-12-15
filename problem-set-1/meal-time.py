# eat breakfast between 7:00 and 8:00
# lunch between 12:00 and 13:00
# dinner between 18:00 and 19:00
# breakfast time, lunch time, or dinner time
# 24-hour time as #:## or ##:##

def main():
    #time = input("What time is it?")
    convert("7:30")


def convert(time):
    """
      Converts time, a str in 24-hour format, to the corresponding number of hours as a float. 
      For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), 
      convert should return 7.5 (i.e., 7.5 hours).
    """
    # Find and set a time delimiter, ":"
    timeDelimiterIndex = time.find(":")
    # Store values from left to right until delimiter ":"
    hour = time[:timeDelimiterIndex]
    minutes = time[timeDelimiterIndex + 1:]

    # Cast float and round the strings
    hourFloat = round(float(hour),1)
    minutesFloat = round(float(minutes),1)

    # Ex: To transform 30 into 0.5, you need to divide 30 by 60
    minutesToFraction = minutesFloat / 60

    convertedTime = hourFloat + minutesToFraction

    return convertedTime

if __name__ == "__main__":
    main()

