import datetime
import turtle

# function to draw an analog clock
def analog_clock(hour, minute):
    # draw clock edge
    t = turtle.Pen()
    t.circle(200)
    t.penup()
    t.left(90)
    t.forward(200)
    t.pendown()
    # draw minute hand
    t.right(minute * 6)
    t.forward(170)
    t.backward(170)
    t.left(minute * 6)
    # draw hour hand
    t.right(hour * 30)
    t.forward(100)
    t.backward(100)
    t.left(hour * 30)
    t.penup()
    # draw hour numbers
    for x in range(1, 13):
        t.right(30)
        t.forward(150)
        t.pendown()
        t.write(str(x), align='center', font=("Arial", 20, "bold"))
        t.penup()
        t.backward(150)
        

# Ask the user for the hour and minute to make an alarm clock
hour_user = int(input('Choose your hour (24-hour clock):'))
minute_user = int(input('Choose your minute:'))
# Ask the user for the message to be displayed when the alarm clock is triggered
message_displayed_user = input('''What message you would like to be
displayed when the alarm is triggered?\n''')
# Wait until the current time is equal to the user given time
while(True):
    hour_now = int(datetime.datetime.today().strftime("%H"))
    minute_now = int(datetime.datetime.today().strftime("%M"))
    # Get out of the loop when the current time is equal to the user given time
    if (hour_user == hour_now) and (minute_user == minute_now):
        break

# Display the alarm message and the clock    
print(message_displayed_user)
analog_clock(hour_user, minute_user)
