---
title: "Lesson 1: Hello Python"
layout: default
---

# Hello Python

So, you want to learn Python? Great, then you've come to the right place. In this book, we will take you from a complete beginner to someone who's able to build several different apps in many different areas.

Be prepared for an exciting journey!

## Introduction

In this chapter we will:

- Understand why Python is a good choice for many different types of domains.
- How to install Python.
- Leverage the REPL to try out Python code and to learn more about keyword in Python and more.

## Narrative: Prologue - leaving Earth

*Earth rapidly became a smaller and smaller blue dot til nothing remained but the darkness of space. The fusion engines slowly pushed the ark ship forward, gliding like a metallic swan. The journey would take 20 years and most of the crew were already in cryo sleep. Only the captain remained awake, doing last minute checks before they would join the others in the dreamless sleep. For the crew, 20 years would pass in an instant, but for the inhabitants of Earth it would be a different story.*

*7 ark ships left the Earth, each with a different mission and different destination. This story takes place on Ark-04 with the mission of reaching the nearest star system, Proxima Centauri.*

<div>
    <img src="./assets/Chapter1.jpeg" alt="Ark ships leaving the Earth" width="600">
</div>

### Rude awakening

*What felt like a sudden jolt, ensign Tabitha, (her friends called her Tab) was shaken from her dreamless slumber. Vision blurry, she could barely make out what was happening, beeping sounds, red and yellow lights flashing. Then the ship's computer voice came on, "System error, level 2 unable to correct, trying fallback, fallback failed".*

**Tabitha**: "What's happening? Computer, status report!"

**Ship**: "Operating system failure, unable to run sub routines, manual intervention required."

**Tabitha**: "What about life support systems, engines etc?"

**Ship**: "Life support systems are stable, engines are offline, unable to restart without manual intervention."

**Tabitha**: "To herself, crap, not good, Ok, computer, recommend actions."

**Ship**: "Subroutines needs rebuilding"

**Tabitha**: "Oh wow, OK, got to start somewhere, Computer start the terminal"*

<div>
    <img src="./assets/Chapter1_2.jpeg" alt="Tabitha waking up from cryo sleep" width="600">
</div>

## Why Python

> **Tabitha**: "Computer, I'm not familiar with the terminal, what language is it using?"
> **Ship**: "It's Python, a high-level programming language, easy to learn and use."
> **Tabitha**: "Great, tell me more about Python."
> **Ship**: "Python is a versatile language, used in many different areas, from web development to machine learning. It's easy to read and write, and has a rich ecosystem of libraries and tools."

According to Slashdata, a reputable institute for developer statistics, there are at least 8.2 million developers in the world using Python.

Python is used in a variety of areas like:

- Web development
- Data science
- Machine learning
- Automation
- Desktop gui
- Embedded applications

> **Tabitha**: "Ok, sounds good, let's hope it covers spaceship repair as well."
> **Ship**: "Yes, Python is a great choice for that as well."

There's many reasons why Python is a great choice for many different domains:

- **Readability** it's readability, Python is very easy to read.
- **Write less code**. Another great reason is that you write less code, for example to read the content of a file, you would use one line of code where it in many other languages would take several.
- **Multi-purpose**. It's used for many different things, everything from building apps to scripting.
- **Ecosystem**. There's a rich ecosystem that will allow you develop many types of apps and also provides great tooling.

In short, it's a great first programming language to learn and it grows with you.

Get ready to learn Python!

> **Tabitha**: "Thanks, I guess".

## Installing Python

> **Ship**: You might need to install Python in some parts of the ship, I can guide you through the process if you want.
> **Tabitha**: "Ok, why not"

To install Python, there are a few different steps to get setup:

1. Go to <https://www.python.org/downloads/>.
2. Download python.
3. Install python
4. Check python version.

It's common that MacOS comes with Python preinstalled but you might need to upgrade that version of Python.

>If you're on Windows, you can also install Python via the Windows Store. [Read more here](https://learn.microsoft.com/en-us/windows/python/beginners) to get the latest details.

### Verify installation

Once you've installed Python, you can check installed version with the command `python --version` in your terminal. You will see an output similar to:

```text
Python 3.10.11
```

Hopefully you're now setup and can begin your journey learning Python.

## Using the REPL

**Ship**: To get started, you can use what's known as a REPL.

A REPL stands for **R**ead **E**valuate **P**rint **L**oop and is a command line program for when you want to try things out and you're not ready to save your code to a text file.

**Tabitha**: "Ok, I'm ready, what do I type?"

### Starting the REPL

To start the REPL, you type `python`, you should see output similar to the below text:

```bash
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

In the preceding code, you see information on installed version, date and time and also `>>>` which a marker that indicates it's ready for you to type Python code.

**Tabitha**: "Got it, **python**, yep that does something, what do I do now?"

### Expressions

You can type expression like `1+1` as well as statements, for example creating a variable `message` like so `message = "hello"`.

Typing a statement makes the REPL evaluate it and return the result:

```python
>>> 1+1
2
```

**Tabitha**: "Ok, I typed `2+2` and it returned `4`, I got this"
**Ship**: "Great, now try creating a variable `message` and assign it the value `hello`"
**Tabitha**: "Ok, how do I do that?"
**Ship**: "Type `message = "hello"`"

```python
message = "hello"
```

Now use the `print()` function to output the value of the variable `message`.

Typing `print(message)` will output your variable's value:

```python
>>> print(message)
hello
```

**Tabitha**: "I gave it the value `Tabitha`, hey look at that, it worked!"

### Using help

**Ship**: A great utility is help, it will give you information on code you're writing. To use `help()`, type it into the REPL with closed parenthesis like so:

```python
>>> help
Type help() for interactive help, or help(object) for help about object.
```

**Tabitha**: "Ok, I typed `help()` and it gave me some information, here's what I got:

```text
Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".
```

**Ship**: We just learned to use `print()` to output content to the terminal, try finding out more about `print()` using `help()` like so:

```python
help(print) 
```

**Tabitha**: "Ok, seems useful. I typed `help(print)` and got this output:

```text
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

**Ship** In the preceding output, it describes what it does "Prints the values to a stream" and how to use it further. Let's try to use `print()` with multiple values.

```python
>>> print("abc", "bcd", "efg")
abc bcd efg
```

**Tabitha**: "Ok, I typed `print("Tabitha", "aced", "this", "course")` :)"

### Separator

**Ship**: The help information on `sep` says we can change how the output happens. Let's try feeding `print()` several text strings and use `sep` like so:

```python
>>> print("abc", "bcd", "efg", sep=",")
abc,bcd,efg
```

Using `sep`, according to `help`, it said "string inserted between values, default a space." that if specify `sep` we can give it another separation character like `:`.

**Tabitha**: "Ok, I typed `print("Tabitha", "aced", "this", "course", sep=",")`. Alright, it worked!"

### Using help as a utility

**Ship**: You saw how you typed `help()` and gave it a topic as parameter. You can also start help as a utility program by typing `help()`.

```text
help()
```

This invocation starts a help prompt like so:

```text
help> 
```

**Tabitha**: "I guess that's useful?"
**Ship**: "Yes, this way you can type your topic straight away."
**Tabitha**: "Cool, let me try that, `ship`"

```text
help> ship

This is the ship module. Here is a list of functions:
 - status() -- Get the status of the ship
 - repair() -- Repair the ship
 - report() -- Report the status of the ship
```

**Ship**: "Great, you found the ship module**

**Tabitha**: "So when can we get started on repairing the ship?"

**Ship**: "Not quite yet, we need to learn some more basics first"

> [!NOTE]
> Did you know that the Apollo 11 spacecraft, which landed the first humans on the Moon, used a computer called the Apollo Guidance Computer (AGC)? It had a user interface called the DSKY (Display and Keyboard), which was essentially the terminal of its time. The AGC had only 2KB of memory for programs and 36KB of read-only memory, yet it was powerful enough to guide the spacecraft to the Moon and back. Astronauts used simple commands like "Verb" and "Noun" to interact with the computer, making it a precursor to modern command-line interfaces. Imagine debugging a spaceship with that kind of hardware!

## Challenge

**Ship**: "Here's a challenge for you."

Try starting `help` as a utility with `help()`, this will provide a list of things you can ask for help on:

```text
To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics"
```

Try typing one of the things above to learn more.

**Tabitha**: "Great, homework :/"

## Assignment, ships status, report

**Ship**: You're now in charge of the ship's status and learning more about the error. Use the REPL to find out more about the error message "System error, level 2 unable to correct, trying fallback, fallback failed".

Remember to use `help()` to learn more about the REPL.

I've got some specific ships code for you to run, to get started, run `python ship.py` in the terminal. See [Ships code](./ship.py)

Task: The command `input` is used to read user input. Can you use `help` to find out more how to use it and write code to capture the user input in a variable and print what the user just typed?

You can use `;` to separate different statements.

**Tabitha**: "Task 1: Run `python ship.py` to learn more about the ship. Task 2, use `input` to capture user input and print it out. Got it!"

## Quiz

**Question**: What are some areas where Python is used?

1. Machine Learning and AI Development
2. Game Development
3. Managing Human Resources in a Company

[Solution quiz](./solutions/solution-quiz.md)

## Solution

Please try to figure out the code before looking at the solution at [Solution](./solutions/solution.py).
