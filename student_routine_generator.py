import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta

class DetailedStudentRoutineGenerator:
    def __init__(self):
        self.scaler = StandardScaler()
        self.feature_names = ['sleep_hours', 'study_hours', 'exercise_minutes', 
                            'stress_level', 'assignment_deadline', 'exam_upcoming']
        
        # Define detailed activities with durations and descriptions
        self.activity_details = {
            'wake_up': {'duration': 15, 'description': 'Wake up and freshen up'},
            'meditation': {'duration': 15, 'description': 'Morning meditation and mindfulness'},
            'exercise': {'duration': 45, 'description': 'Physical exercise (mix of cardio and strength)'},
            'breakfast': {'duration': 30, 'description': 'Healthy breakfast and preparation'},
            'study_focused': {'duration': 90, 'description': 'Focused study session with breaks'},
            'class': {'duration': 60, 'description': 'Attend classes/lectures'},
            'lunch': {'duration': 45, 'description': 'Lunch break and short rest'},
            'project_work': {'duration': 90, 'description': 'Work on assignments and projects'},
            'hobby': {'duration': 60, 'description': 'Engage in hobbies or extracurricular activities'},
            'rest': {'duration': 30, 'description': 'Short rest or power nap'},
            'revision': {'duration': 60, 'description': 'Review of daily learning'},
            'dinner': {'duration': 45, 'description': 'Dinner and relaxation'},
            'planning': {'duration': 20, 'description': 'Plan next day activities'},
            'sleep_prep': {'duration': 30, 'description': 'Prepare for sleep, light reading'}
        }
        
        # Initialize the scaler with sample data
        self._init_scaler()

    def _init_scaler(self):
        """Initialize and fit the scaler with sample data"""
        # Generate sample data for fitting the scaler
        sample_data = {
            'sleep_hours': np.random.normal(7, 1, 100),
            'study_hours': np.random.normal(6, 2, 100),
            'exercise_minutes': np.random.normal(30, 10, 100),
            'stress_level': np.random.randint(1, 6, 100),
            'assignment_deadline': np.random.randint(0, 2, 100),
            'exam_upcoming': np.random.randint(0, 2, 100)
        }
        sample_df = pd.DataFrame(sample_data)
        self.scaler.fit(sample_df)

    def generate_detailed_routine(self, user_input):
        """Generate a detailed next day routine based on user input"""
        # Convert user input to DataFrame with feature names
        features_df = pd.DataFrame([user_input], columns=self.feature_names)
        features_scaled = self.scaler.transform(features_df)
        
        # Calculate wake-up time based on sleep hours
        wake_time = datetime.strptime("06:00", "%H:%M")  # Default wake time
        if user_input['sleep_hours'] < 6:
            wake_time = datetime.strptime("07:00", "%H:%M")  # Extra hour of sleep if tired
        
        # Factor in stress level and upcoming deadlines
        study_intensity = "high" if (user_input['stress_level'] > 3 or 
                                   user_input['assignment_deadline'] or 
                                   user_input['exam_upcoming']) else "normal"
        
        # Generate detailed schedule
        schedule = self._create_detailed_schedule(wake_time, study_intensity, user_input)
        return schedule

    def _create_detailed_schedule(self, start_time, study_intensity, user_input):
        """Create a detailed schedule with specific activities and recommendations"""
        schedule = []
        current_time = start_time
        
        # Early Morning Routine
        schedule.append(self._create_activity_block(current_time, 'wake_up', 
                                                  "Start with deep breathing exercises"))
        current_time = self._advance_time(current_time, 15)
        
        if user_input['stress_level'] > 3:
            schedule.append(self._create_activity_block(current_time, 'meditation',
                                                      "Focus on stress-reducing meditation"))
            current_time = self._advance_time(current_time, 15)
            
        # Morning Exercise
        if user_input['exercise_minutes'] < 30:
            schedule.append(self._create_activity_block(current_time, 'exercise',
                                                      "Priority on physical activity today"))
            current_time = self._advance_time(current_time, 45)
            
        schedule.append(self._create_activity_block(current_time, 'breakfast',
                                                  "Include protein-rich foods for sustained energy"))
        current_time = self._advance_time(current_time, 30)
        
        # Morning Study/Class Block
        if user_input['exam_upcoming']:
            schedule.append(self._create_activity_block(current_time, 'study_focused',
                                                      "Focus on exam preparation"))
            current_time = self._advance_time(current_time, 90)
        else:
            schedule.append(self._create_activity_block(current_time, 'class',
                                                      "Active participation in class"))
            current_time = self._advance_time(current_time, 60)
            
        # Lunch Break
        schedule.append(self._create_activity_block(current_time, 'lunch',
                                                  "Take a proper break, eat mindfully"))
        current_time = self._advance_time(current_time, 45)
        
        # Afternoon Block
        if user_input['assignment_deadline']:
            schedule.append(self._create_activity_block(current_time, 'project_work',
                                                      "Focus on completing pending assignments"))
            current_time = self._advance_time(current_time, 120)
        else:
            schedule.append(self._create_activity_block(current_time, 'study_focused',
                                                      "Review and practice sessions"))
            current_time = self._advance_time(current_time, 90)
            
        # Evening Activities
        if study_intensity == "normal":
            schedule.append(self._create_activity_block(current_time, 'hobby',
                                                      "Engage in relaxing activities"))
            current_time = self._advance_time(current_time, 60)
            
        schedule.append(self._create_activity_block(current_time, 'dinner',
                                                  "Light and healthy dinner"))
        current_time = self._advance_time(current_time, 45)
        
        # Night Routine
        schedule.append(self._create_activity_block(current_time, 'planning',
                                                  "Plan for tomorrow, set goals"))
        current_time = self._advance_time(current_time, 20)
        
        schedule.append(self._create_activity_block(current_time, 'sleep_prep',
                                                  "Prepare for restful sleep"))
        
        return schedule

    def _create_activity_block(self, start_time, activity, recommendation):
        """Create a structured activity block with time and recommendations"""
        duration = self.activity_details[activity]['duration']
        end_time = self._advance_time(start_time, duration)
        
        return {
            'time': start_time.strftime("%H:%M"),
            'end_time': end_time.strftime("%H:%M"),
            'activity': activity,
            'duration': duration,
            'description': self.activity_details[activity]['description'],
            'recommendation': recommendation
        }

    def _advance_time(self, current_time, minutes):
        """Advance time by specified minutes"""
        return current_time + timedelta(minutes=minutes)

def validate_input(prompt, input_type=float, min_val=None, max_val=None):
    """Validate user input with error handling"""
    while True:
        try:
            value = input_type(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print(f"Please enter a valid {input_type.__name__} value")

def display_routine(routine):
    """Display the routine in a formatted way"""
    print("\n=== Detailed Schedule for Tomorrow ===")
    print("\nNote: This schedule is adaptive and can be adjusted based on your needs.\n")
    
    for block in routine:
        print(f"\n{block['time']} - {block['end_time']}: {block['activity'].replace('_', ' ').title()}")
        print(f"Duration: {block['duration']} minutes")
        print(f"Description: {block['description']}")
        print(f"Recommendation: {block['recommendation']}")
        print("-" * 50)

def main():
    # Initialize generator
    generator = DetailedStudentRoutineGenerator()
    
    # Get user input with validation
    print("\nPlease provide information about your day:")
    user_input = {
        'sleep_hours': validate_input("Hours of sleep last night (0-24): ", float, 0, 24),
        'study_hours': validate_input("Hours spent studying today (0-24): ", float, 0, 24),
        'exercise_minutes': validate_input("Minutes spent exercising today (0-300): ", float, 0, 300),
        'stress_level': validate_input("Stress level (1-5): ", int, 1, 5),
        'assignment_deadline': validate_input("Assignment due tomorrow? (0/1): ", int, 0, 1),
        'exam_upcoming': validate_input("Exam tomorrow? (0/1): ", int, 0, 1)
    }
    
    # Generate and display detailed routine
    routine = generator.generate_detailed_routine(user_input)
    display_routine(routine)

if __name__ == "__main__":
    main()