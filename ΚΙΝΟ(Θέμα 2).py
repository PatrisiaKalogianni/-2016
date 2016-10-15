# p15049 Patrisia Kalogianni
# Lesson : "Introduction to Computer Science"
# Project 2 : Find 7 most frequent and 7 least frequent numbers drawn in kino

def makeJump(timesDrawHour, timeDrawMin):
    timeDrawMin += 5                        # 5 minits for each draw
    if(timeDrawMin == 60):                  # if 60 mins have past add  1 to hour
        timesDrawHour += 1
        timeDrawMin = 0
    return timesDrawHour, timeDrawMin
    
def constructURL(day, month, year):         #url construction
    import urllib2, json
    x = str(day)
    y = str(month)
    z = str(year)
    global url
    url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/" + x + "-" + y +"-"+z+".json"
    return url

#adds a 0 in front of one-digit numbers in order to constuct "curDrawDate" the same as "drawTime" on the website
def addZero(x): 
    if x <10 :
        x= "0" + str(x)
        return x
    else:
        return x

    
def makeList():
    import urllib2, json, datetime
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    hour = now.hour
    minute = now.minute
    
    day2 = addZero(day)
    month2 = addZero(month)
    hour2 = addZero(hour)
    minute2 = addZero(minute)
    
    curDrawDate = str(day2) + "-" + str(month2) + "-" + str(year) + "T" + str(hour2) + ":" + str(minute2) + ":" + "00" # need if to put in front of <10 numbers
    
    print "first draw date =" + curDrawDate
  
    if (hour >= 9 and minute > 5):
        timeDrawHour = 9                          # firsy draw time 9.00                                                                  
        timeDrawMin = 0
        index = 0
        intList = [0 for x in range(0,80)]        # initialize empty list to count times a number is drawn
        jsonUrl = constructURL(day, month, year)                                                    
        results = urllib2.urlopen(jsonUrl)                                                          
        resultsRead = results.read()                                                                    
        fetch = json.loads(resultsRead)
        while (((hour - timeDrawHour) != 0) or ((minute - timeDrawMin) < 4)):
            for x in range (0,80):
                for i in range (0,20):
                    if (fetch["draws"]["draw"][index]["results"][i] == x):
                        intList[x] += 1
            timeDrawHour, timeDrawMin = makeJump(timeDrawHour, timeDrawMin)
            curDrawDate = str(day) + "-" + str(month) + "-" + str(year) + "T" + str(timeDrawHour) + ":" +str(timeDrawMin) + ":" + str(0) + str(0)
            index += 1
    
 
    print intList

makeList()
