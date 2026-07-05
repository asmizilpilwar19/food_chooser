# What Should We Eat?

What Should We Eat? is a desktop application built with **Python** and **Tkinter** that helps eliminate the common dilemma of deciding where to eat. Users can create a personalized list of their favorite restaurants, save them locally, and let the application randomly choose a destination through a fun animated selection process.

Designed with a cute pastel-inspired interface, the application offers a lightweight and enjoyable way to make dining decisions for individuals, friends, and families.

---

## Overview

Choosing where to eat can often be surprisingly difficult, especially when multiple options are available. This application simplifies the process by allowing users to maintain a personal restaurant list and randomly selecting one whenever they need inspiration.

Restaurant data is stored locally using JSON, ensuring that saved locations remain available between sessions without requiring an internet connection or external database.

---

## Features

### Restaurant Management

- Add favorite restaurants
- Remove restaurants from the list
- View all saved restaurants
- Automatically save data locally

### Random Restaurant Picker

- Randomly selects a restaurant from your saved list
- Animated selection effect before revealing the final choice
- Instant decision-making with a single click

### User Interface

- Cute pastel-themed design
- Beginner-friendly layout
- Custom animated buttons with hover effects
- Simple restaurant management interface
- Large highlighted result display

### Local Storage

- Saves restaurant list using JSON
- Automatically loads saved restaurants on startup
- No internet connection required

---

## Technologies Used

- Python 3
- Tkinter
- JSON
- Random Module
- Object-Oriented Programming (OOP)

---

## How It Works

1. Add your favorite restaurants.
2. Build your personal restaurant list.
3. Click **Pick For Me**.
4. Watch the animated random selection.
5. Receive a randomly chosen restaurant recommendation.

The restaurant list is automatically saved and restored each time the application is opened.

---

## Project Structure

```
What-Should-We-Eat/
│
├── main.py
├── restaurants.json
├── README.md
└── screenshots/
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/What-Should-We-Eat.git
```

Navigate into the project

```bash
cd What-Should-We-Eat
```

Run the application

```bash
python main.py
```

---

## Learning Outcomes

This project demonstrates:

- Desktop application development with Tkinter
- Object-Oriented Programming
- Event-driven programming
- JSON file handling
- Data persistence
- Randomized selection algorithms
- GUI design and layout management
- Simple animation using Tkinter's `after()` method

---

## Future Improvements

- Restaurant categories (Fast Food, Café, Fine Dining, Desserts)
- Cuisine filters
- Budget filters
- Favorite and recently visited restaurants
- Restaurant ratings
- Meal type selection (Breakfast, Lunch, Dinner)
- Google Maps integration
- Random wheel spinner animation
- Restaurant notes
- Search functionality
- Import and export restaurant lists
- Dark mode
- Custom themes
- Cloud synchronization
- Multiple restaurant collections

---

## Screenshots

Add screenshots of your application here.

```
screenshots/home.png
screenshots/random_picker.png
```

---

## Why This Project?

What Should We Eat? transforms everyday decision-making into a fun and interactive experience. Instead of endlessly debating dining options, users can maintain a personalized restaurant collection and let the application make the choice for them with an engaging animated picker. The project also demonstrates practical concepts such as local data storage, GUI development, event-driven programming, and simple animations using Python and Tkinter.

---

## Author

**Asmi**

A fun desktop application built with Python and Tkinter that makes choosing where to eat faster, easier, and more enjoyable through interactive random restaurant selection.
```
