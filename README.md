# student-routine-generator

# Features
# User Input Validation: 
Ensures user inputs are within the acceptable range.
#Customizable Schedule: 
Generates a tailored daily routine based on user inputs.
# Activity Recommendations:
Provides detailed activity descriptions and recommendations to improve productivity.
# Scalable:
Uses the StandardScaler from scikit-learn to normalize input features.
# Comprehensive Schedule Generation:
Factors in various aspects such as sleep, study hours, exercise, stress levels, and upcoming deadlines.

# Prerequisites
Python 3.x
Required Python libraries:
pandas
numpy
scikit-learn

# CODE OVERVIEW
__init__(self): Initializes the class, sets up the feature scaler, and defines detailed activities with durations and descriptions.

_init_scaler(self): Initializes and fits the scaler with sample data to normalize user input features.

generate_detailed_routine(self, user_input): Generates a detailed routine based on user inputs. Factors in sleep hours, stress levels, and upcoming deadlines.

_create_detailed_schedule(self, start_time, study_intensity, user_input): Creates a detailed schedule with specific activities and recommendations based on the user's input.

_create_activity_block(self, start_time, activity, recommendation): Creates a structured activity block with time, duration, description, and recommendations.

_advance_time(self, current_time, minutes): Advances the given time by a specified number of minutes.

Functions
validate_input(prompt, input_type=float, min_val=None, max_val=None): Validates user input with error handling to ensure values are within specified ranges.

display_routine(routine): Displays the generated routine in a formatted manner.
