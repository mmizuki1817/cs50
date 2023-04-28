# Pomodoro Timer


### Description

#### Project Description

I created a web application called Pomodoro Timer.
There is a time management technique called the Pomodoro Technique.
This method was developed by an Italian named Francisco Cirillo.

Pomodoro means tomato in Italian, and this is because the kitchen timer that Cirillo used was shaped like a tomato.

In the Pomodoro technique, you alternate between short work periods and short rest periods that you decide.
In concrete terms, this means alternating eight cycles of 25 minutes of work and 5 minutes of rest.
The idea is to break the work into short periods of time and take frequent breaks.
And by keeping track of your work time on a clock,
you will be able to maintain a high level of concentration.

This is the Pomodoro Technique.
Pomodoro Timer is a timer that measures your time using this Pomodoro Technique.


#### Contents and functions of each file created for the project

##### index.html(setting)：

The first page that opens when you access "https://mmizuki1817.pythonanywhere.com/".
The default settings are work time: 25 minutes, interval: 5 minutes, cycle: 8 sets, rest time: 0 minutes, number of rest: 0.
You can also change the numbers yourself.
The difference between intervals and breaks is like the difference between recess and lunch break in school.
Recess is interrupted once per period, but lunch break is only once.
If you need to take a longer break in the cycle, such as a meal, you can tweak the break time and number of breaks.
When the settings are complete, press the decision button.
When the decision button is pressed, you will jump to one of the following pages: ➀apology.html➁home.html➂home1.html


##### apology.html:

When the decision button is pressed, if there is some error, this page will be displayed.
Examples of errors are when the working time is 0 hours and 0 minutes, when the number of cycles is 0, or when the minutes part of the working time exceeds 60.
In this case, a message will be displayed according to the error.
For example, if the number of minutes of work exceeds 60, the message "Please enter the working time. You can enter work time from 0 to 59 minutes." displayed on your screen.


##### home.html：

If there are no errors, the value of the break time is 0, and the number of breaks is 0, and the decision button is pressed, this page will be displayed according to the value you have set in ndex.html.
When the start button is pressed, the work timer starts and a countdown begins.
When the countdown of the work timer reaches zero, the end sound is heard and the countdown of the interval timer starts automatically.
When the interval timer reaches zero, the cycle is added +1, and the work timer starts counting again.
When all cycles have been completed, the screen will display an end alert.
To distinguish whether the work timer or the interval timer is counting, the timer is displayed in white for the work timer and in blue for the interval timer.
In addition, the sound of the alarm that sounds when the work timer reaches zero and when the interval timer reaches zero is also different, so it is possible to judge without looking at the screen.
When you want to change the settings, press the Back button to return to the index.html page.

##### home1.html：

If there are no errors and the break time and number of breaks are greater than or equal to 1, and the decision button is pressed, the page will be displayed according to the values you set in index.html.
The basic function is the same as home.html.
The difference is that a break button is displayed.
If you want to take a long break, you can press this button. The timer will stop counting down, the number of breaks will decrease by one, and the end time of the break will be displayed.
At the end of the break, the same alarm sounds as when the interval timer ended, and the timer starts again.
During a break, it is the same as before the start button is pressed,  the break button cannot be pressed.
When the number of times the rest button is pressed, the display of the rest button will disappear.

##### layout.html：

The framework of header and footer is described.

#### Environment

* python3.9.6
* Windows10
* Google Chorome

#### Author

Creater：M.Mizuki
State：Japan
mail: lepetitbonheur1817@gmail.com

#### Reference
BGM by OtoLogic(CC BY 4.0),
Font "DSEG" by けしかん


