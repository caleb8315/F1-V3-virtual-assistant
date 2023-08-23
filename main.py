import speech_recognition as sr
import pyttsx3
import pyaudio
import webbrowser as wb
import datetime
import time
import os 
import random
from words import *
import pyjokes
import platform
import pyautogui
import psutil
import turtle







engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
                        
    try:
        print("Calibrating...")
        query = r.recognize_google(audio, language= 'en-in')
        print(query)

    except Exception as e:
        print(e)
        print("Could not understand sir")

        return 'none'
    return query
#time/day

def hour():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak('good morning')
    elif hour >=12 and hour <17:
        speak('good afternoon')
    elif hour >=17 and hour <20:
        speak('good evening')
    else:
        speak(random.choice(goodnight))
def timer():
    Time = datetime.datetime.now().strftime('%I:%M')
    speak("The current time is")
    speak(Time)

#searches
def google():
    wb.open_new_tab('http://google.com')
def youtube():
    wb.open_new_tab('http://youtube.com')
def school():
    wb.open_new_tab('https://lms.fcps.org/home')
def news():
    wb.open_new_tab('https://www.cbsnews.com/live/cbsn-local-ny/')
def vpn():
    path = "/Applications/ProtonVPN.app"
    os.system(f"open {path}")
def music():
    path = "/Applications/Spotify.app"
    os.system(f"open {path}")
def doing():
    query = takeCommand().lower()
    if query in nothing:
        speak('go do something')
    else:
        speak(random.choice(dope))
def jokes():
    speak(pyjokes.get_joke())
def screenshot():
    img = pyautogui.screenshot()
    img.save('img.png')
 # info
def system():
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    speak("system info is posted sir")
def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+ usage)

def shutdown():
    os.system("sudo shutdown -h now")

def info11():
    query = takeCommand().lower()
    speak('do you want to put in password or speak')
    if 'speak' in query:
        speak('what is the password')
        passwordd = takeCommand()
        if passwordd == 'maggie':
            print('this is info')
        else:
            speak('access denied')
    elif 'put in' in query:
        pw1 = input('password: ')
        if 'maggie2004' in pw1:
            print('this is info')
        else:
            print('access denied')
            speak('wrong password sorry')

# games

def madlibs():
    speak('Welcome to madlibs')
    print("""
                    HEllO!
                This is madlibs game!
            in this gane we will take you over a funny story!
            YOU fill in the blanks!
        """)
    print("lets begin")
    Name = input('enter a Name: ')
    Job = input('enter a job name:')
    salary = input('amount of salary:')
    speak(Name+ ' got a new job as a ' +Job+ ' and makes a salary of ' +salary)


def snake_game():
    colorss = ['red', 'green', 'blue']
    shapesss = ['square', 'circle', 'triangle']
    delay = 0.1
    score = 0
    high_score = 0

    wn = turtle.Screen()
    wn.title("SNAKE GAME 01")
    wn.bgcolor('blue')

    wn.setup(width = 600, height = 600)
    wn.tracer(0)

    head = turtle.Turtle()
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0,0)
    head.direction = 'Stop'

    food = turtle.Turtle()
    colors = random.choice(colorss)
    shapes = random.choice(shapesss)
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0,100)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('white')
    pen.penup()
    pen.goto(0,250)
    pen.write('score : 0 High score : 0', align='center', font=('condara', 24, 'bold'))


    def group(): 
        if head.direction != "down": 
            head.direction = "up"

    def godown():
        if head.direction != 'up':
            head.direction = 'down'

    def goleft():
        if head.direction != 'right':
            head.direction = 'left'
    def stop():
        quit()

    def goright():
        if head.direction != 'left':
            head.direction = 'right'

    def move(): 
        if head.direction == "up": 
            y = head.ycor() 
            head.sety(y+20) 
        if head.direction == "down": 
            y = head.ycor() 
            head.sety(y-20) 
        if head.direction == "left": 
            x = head.xcor() 
            head.setx(x-20) 
        if head.direction == "right": 
            x = head.xcor() 
            head.setx(x+20)
        
        
    
    
    wn.listen() 
    wn.onkeypress(group, "w") 
    wn.onkeypress(godown, "s") 
    wn.onkeypress(goleft, "a") 
    wn.onkeypress(goright, "d") 
    wn.onkeypress(stop, 'p')


    segments = []

    while True:
        wn.update()
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'Stop'
            colors = random.choice(colorss)
            shapes = random.choice(shapesss)
            for segment in segments:
                segment.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write("score : {} High Score : {}".format(score, high_score), align=('center'), font=('candara', 24, 'bold'))
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x,y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color('orange')
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
                pen.clear()
                pen.write("score : {} High score : {}".format(score, high_score), align="center", font=("candara", 24, "bold"))
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)
        move()
        for segment in segments:
            if segment.distance(head) <20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = ('stop')
                colors = random.choice(colorss)
                shapes = random.choice(shapesss)
                for segment in segments:
                    segment.goto(1000,1000)
                    segment.clear()

                    score = 0
                    delay = 0.1
                    pen.clear()
                    pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        time.sleep(delay)

    wn.mainloop()
    

query = takeCommand().lower()



if __name__ == '__main__':
    
    while True:
        query = takeCommand().lower()

        

        #greetings/how you...

        if query in greetings_h1:
            speak(random.choice(greetings_f1))
        elif query in r_u_there:
            speak(random.choice(r_u_there_f ))
        elif 'f1' in query:
            speak("yes")
        elif query in dais_noches:
            hour()

            






        # search/google

        elif query in price:
            search_term = query.split("for")[-1]
            url = 'https://google.com/search?q=' + search_term
            wb.get().open(url)
            speak('Here is what i found for' + search_term + "on google")
        elif query in google1:
            google()
            speak('done')
        elif query in youtube1:
            youtube()
            speak('done')
        elif query in school1:
            school()
            speak('done')
        elif query in news1:
            news()
            speak('done')
        elif 'look up' in query or 'search' in query:
            speak("what would you like me to look up?")
            safaripath = '/Applications/Safari.app'
            search = takeCommand()
            wb.get('safari').open_new_tab(search + '.com')
            speak('done')


        # info
        elif query in systemm:
            system()
        elif 'what is my cpu' in query:
            cpu()
        elif query in info:
            info11()


        #name/remember
        elif query in remind:
            speak("what would you like me to remind you?")
            data = takeCommand()
            speak('you told me to remind you' + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif query in remind2:
            remember = open('data.txt', 'r')
            speak(random.choice(remindf) + data)
        elif query in name_h:
            speak('what do you want me to call you? ')
            name = takeCommand()
            speak('i will call you' + name)
            rm = open('name.txt', 'w')
            rm.write(name)
            rm.close() 
        elif query in what_name:
            rr = open('name.txt', 'r')
            speak('your name is' + name)




        #doing/hows

        elif query in how_you:
                speak(random.choice(emotions_f))
                speak('how about you')
        elif query in emotions_hgood:
            speak("that is good!")
        elif query in emotions_hbad:
            speak("i am sorry to hear that.")
        elif query in up_to:
            speak(random.choice(what_doing_action))
            speak('how about you?')
            take = takeCommand()                 
            speak('thats awesome')
        
        elif query in up_to:
            speak(random.choice(what_doing_action))
            speak('and what are you doing')
            doing()
        elif query in bored:
            speak(random.choice(should_do))
        elif 'what should i do' in query:
            speak(random.choice(should_do))
        #thanks/welcome
        elif query in thank:
            speak(random.choice(welcome))
        elif 'open vpn' in query:
            speak('okay')
            vpn()
        elif 'play music' in query:
            speak("right on it")
            music()
     
        #help

        elif 'help' in query:
            print("""
                                Type the # what you need help with

                            1. What is F1
                            2. list of commands
                            3. Other
                """)
            help1 = input('Type # here:   ')
            if '1' in help1:
                print("""
                                                    WHAT IS F1-V2?

                                f1-v2 is a virtual assistant freind made by Caleb Phillips.
                                f1-v2 stands for freind1-verison2. 
                                The purpose of F1 is to be your freind when no one else is there!
                                    WHY?
                                well becuase You can trust him/ you can talk to him PLUS he is loyal!
                    """)
            elif '2' in help1:
                print("""
                                                LIST OF COMMANDS
                                JUST TALK! there is really no list of commands! 
                                V2 is still learning and developing. 
                                He can be slow sometimes, but just take care of him just as your real friends!

                                IF YOU NEED ANYMORE HELP CONTACT ME AT 
                                        calebwalton10@gmail.com
                    """)
            elif '3' in help1:
                print("Hey! do you need help? well contact me at calebwalton10@gmail.com")





        #fun/games
        elif query in joke:
            jokes()
        elif query in screenshott:
            screenshot()

        
        elif 'snake game' in query:
            snake_game()

        elif query in madlibs1:
            madlibs()







            
            
        # goodbye/end program

        elif 'shutdown' in query:
            shutdown()
        
        elif query in goodbye_h:
            speak(random.choice(goodbye_f))
            quit()
    

