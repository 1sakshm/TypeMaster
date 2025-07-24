# TypeMaster

A Python-based typing speed test application with a graphical user interface that measures your words per minute (WPM) and accuracy.

## Features

- **Typing Speed Test**: Test your typing speed with 30 randomly selected words
- **Real-time Performance Tracking**: Measures WPM and accuracy automatically
- **Leaderboard System**: Stores and displays top scores with names
- **User-friendly GUI**: Clean interface built with Tkinter
- **Persistent Storage**: Uses SQLite database to save scores

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)
- SQLite3 (included with Python)

## Installation

1. Clone or download the project files
2. Ensure you have the following files in your project directory:
   - `main.py` (or your main script file)
   - `db.py` (database functions)
   - `words.txt` (word list file)

## File Structure

```
typemaster/
├── main.py          # Main application file
├── db.py            # Database operations (init_db, ins, gts functions)
├── words.txt        # Text file containing words for the typing test
└── README.md        # This file
```

## Setup

### Creating the words.txt file

Create a `words.txt` file in the same directory with words separated by spaces or newlines. Example:

```
the quick brown fox jumps over lazy dog and runs through forest with great speed while birds sing in trees above ground level making beautiful sounds that echo throughout entire woodland area
```

### Database Setup

The application automatically creates a SQLite database when first run. Make sure your `db.py` file contains these functions:
- `init_db()` - Initialize the database
- `ins(name, wpm, accuracy)` - Insert a new score
- `gts()` - Get top scores for leaderboard

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. **Starting the Test**:
   - The application displays 30 random words from your word list
   - Click in the text box and start typing
   - The timer starts automatically with your first keystroke

3. **Taking the Test**:
   - Type the displayed words exactly as shown
   - Words should be separated by single spaces
   - The test measures both speed and accuracy

4. **Finishing the Test**:
   - Click the "Finish" button when done
   - Enter your name when prompted
   - View your results (WPM and accuracy percentage)

5. **Viewing Leaderboard**:
   - Click "View Leaderboard" to see top scores
   - Scores are ranked by WPM and show accuracy percentages

## How It Works

- **WPM Calculation**: `(number_of_words / elapsed_time_in_seconds) * 60`
- **Accuracy Calculation**: `(correct_words / total_words) * 100`
- **Scoring**: Only words that match exactly (case-sensitive) are counted as correct

## Features Breakdown

### Timer System
- Automatically starts when you begin typing
- Measures elapsed time from first keystroke to finish button click

### Accuracy Checking
- Compares each typed word with the corresponding target word
- Case-sensitive matching
- Partial credit not given (word must be exactly correct)

### Database Storage
- Stores player name, WPM, accuracy, and timestamp
- Persistent leaderboard across sessions
- Top scores displayed in ranking order

## Customization

- **Change word count**: Modify `self.word_count = 30` in the `__init__` method
- **Adjust window size**: Change `self.root.geometry("700x500")`
- **Font customization**: Modify font settings in Label and Text widgets
- **Word list**: Edit `words.txt` to use different words

## Troubleshooting

### Common Issues

1. **"Please start typing first!" message**:
   - Make sure you're actually typing in the text box
   - Ensure the text box has focus (click on it first)

2. **Import errors**:
   - Verify all required files are in the same directory
   - Check that `db.py` contains the required functions

3. **Database errors**:
   - Delete the database file and restart to reset
   - Ensure `init_db()` function is working properly

4. **Words.txt not found**:
   - Create the words.txt file in the same directory
   - Ensure it contains words separated by spaces

## Contributing

Feel free to contribute improvements such as:
- Better UI design
- Additional statistics tracking
- Different test modes (time-based, custom word lists)
- Sound effects and visual feedback
- Dark mode support

## License

This project is open source and available under the MIT License.