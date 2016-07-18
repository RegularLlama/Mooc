#http://www.codeskulptor.org/#user41_xLgVKmri7z_5.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
correct = 0
total = 0
d = 0
flag = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d
    a = t // 600
    b = (t % 600) // 100
    c = t % 600 // 10 % 10
    d = t % 10
    string = str(a) + ":" + str(b) + str(c) + "." + str(d)
    return string

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global flag
    timer.start()
    flag = False

def stop():
    global counter, correct, total, flag
    if(flag==True):
        timer.stop()
        if counter % 10 == 0 and counter != 0:
            correct += 1
            total += 1
        else:
            total += 1
        flag = False

def reset():
    stop()
    global counter,total,correct
    counter = total = correct = 0


# define event handler for timer with 0.1 sec interval
def tick():
    global counter, flag
    counter += 1
    flag = True


# define draw handler
def sec(canvas):
    global counter, correct, total
    canvas.draw_text(format(counter), [200, 250], 38, 'green')
    canvas.draw_text(str(correct), [100, 150], 30, 'blue')
    canvas.draw_text(" / ", [110, 150], 30, 'blue')
    canvas.draw_text(str(total), [120, 150], 30, 'blue')
# create frame
frame = simplegui.create_frame('test', 500, 500)

# register event handlers
timer = simplegui.create_timer(100,tick)
frame.add_button('Start', start)
frame.add_button('Stop', stop)
frame.add_button('Reset', reset)
frame.set_draw_handler(sec)

# start frame
frame.start()

# Please remember to review the grading rubric