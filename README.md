Pomodoro Timer

This is a simple Pomodoro timer application written in Python using the Tkinter GUI toolkit.

How to use

1.Clone the repository and open the pomodoro.py file in a Python IDE.

2.Run the file.

3.The timer will start with a 25-minute work session.

4.When the timer runs out, it will sound an alarm and switch to a 5-minute break session.

5.After four work sessions, the timer will switch to a 20-minute break session.

6.To reset the timer, click the "Reset" button.

Constants

The following constants are used in the code:

PINK: The color of the text for the break sessions.

RED: The color of the text for the long break sessions.

GREEN: The color of the text for the work sessions.

YELLOW: The background color of the window.


FONT_NAME: The name of the font used for the text.

WORK_MIN: The number of minutes in a work session.

SHORT_BREAK_MIN: The number of minutes in a short break session.

LONG_BREAK_MIN: The number of minutes in a long break session.


Functions

The following functions are used in the code:

reset_timer(): Resets the timer to 00:00.

start_timer(): Starts the timer for the next work session.

count_down(): Counts down the timer in seconds and updates the text on the screen.


UI

The UI of the application consists of a window with a canvas, a start button, a reset button, a heading label, and a check mark label.

The canvas contains an image of a tomato and a text label that displays the current time in the countdown.

The start button starts the timer.

The reset button resets the timer to 00:00.

The heading label displays the current status of the timer (e.g., "Work", "Break", or "Long Break").

The check mark label displays the number of work sessions that have been completed.
