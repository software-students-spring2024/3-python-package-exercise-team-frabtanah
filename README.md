# Python Mood Enhancer (pyMood)

![Build Status](https://img.shields.io/github/actions/workflow/status/software-students-spring2024/3-python-package-exercise-team-frabtanah/event-logger.yml)

Replace the contents of the [README.md](./README.md) file with a beautifully-formatted Markdown file including a plain-language **description** of your project and **clear instructions**, including exact **code examples**, for:

- how a developer who wants to import your project into their own code can do so - include documentation for all functions in your package and a link to an example Python program that uses each of them.
- how a developer who wants to contribute to your project can set up the virtual environment, install dependencies, and build and test your package for themselves.

## Description

pyMood is a python package designed to give a quick mood boost to programmers. With simple commands, users can get positive affirmations, quick jokes, or even a virtual high five among other things. It's perfect for when you need a quick pick-me-up during a coding session.

## Instructions

For any developers who want to import pyMood into their own code, follow the steps below:

To install the module from PyPI, run the command:

``pip install pyMood``

### Contributions

A virtual environment is required to build and test.
To start the virtual environment, first you must install pipenv and then run:
```pip install pipenv```
```pipenv shell```

Then install pyMood in your virtual environment
```pipenv install pyMood```

To install the dependencies of pyMood:
```pip install requirements.txt```

## Usage

We have several functions to use from within pyMood.

```python

relaxation_tip(category)
# Returns a random relaxation tip from a specified category to help the user relax.
# If no category is specified, return a random tip.
```

```python
tell_me_a_joke()
# Returns a random joke to lighten up the user's mood
```

```python
get_affirmation()
# Returns a random positive affirmation to boost the user's mood and confidence
```

```python
coffee_suggestion()
# Returns a random cup of coffee as a suggestion, to help motivate the user.
```

```python
cat_mood_generator()
# Returns a random cat emotion.
```

## Team Members

- Francisco Cunningham - [fctico11](https://github.com/fctico11)
- Ahmad Almesned - [ahmadhcs](https://github.com/ahmadhcs)

Link to [pyMood](link) on the PyPI website.
