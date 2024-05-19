# class TemperatureData:
#     def __init__(self):
#         self.temperature = None

#     def update(self, temp_value):
#         self.temperature = temp_value

#     def is_hot(self):
#         # Assuming the temperature is in Celsius
#         if self.temperature >= 25:
#             return True
#         else:
#             return False

# class MoodData:
#     def __init__(self):
#         self.mood = None

#     def update(self, mood_state):
#         self.mood = mood_state

# class FabricDesign:
#     def __init__(self, color_scheme, pattern_type):
#         self.color_scheme = color_scheme
#         self.pattern_type = pattern_type

# class Predictor:
#     def __init__(self):
#         self.temperature_data = TemperatureData()
#         self.mood_data = MoodData()

#     def update_temperature(self, temp_value):
#         self.temperature_data.update(temp_value)

#     def update_mood(self, mood_state):
#         self.mood_data.update(mood_state)

#     def predict_next_design(self):
#         if self.temperature_data.is_hot() and self.mood_data.mood == "happy":
#             return FabricDesign("Bright", "Stripes")
#         elif self.temperature_data.is_hot() and self.mood_data.mood == "sad":
#             return FabricDesign("Dark", "Floral")
#         else:
#             return FabricDesign("Neutral", "Solid")

# # Example usage
# predictor = Predictor()
# predictor.update_temperature(30)
# predictor.update_mood("happy")
# next_design = predictor.predict_next_design()
# print(next_design.color_scheme)



class EnvironmentalMoodData:
    def __init__(self):
        self.temperature = None
        self.mood = None

    def update(self, temp_value, mood_state):
        self.temperature = temp_value
        self.mood = mood_state

    def get_temperature(self):
        return self.temperature

    def get_mood(self):
        return self.mood

    def classify_temperature(self):
        if self.temperature < 10:
            return "cold"
        elif 10 <= self.temperature <= 30:
            return "neutral"
        else:
            return "hot"
        
class FabricDesign:
    def __init__(self, color_scheme, pattern_type):
        self.color_scheme = color_scheme
        self.pattern_type = pattern_type  


class Predictor:
    def __init__(self):
        self.environmental_data = EnvironmentalMoodData()

    def update_environmental_data(self, temp_value, mood_state):
        self.environmental_data.update(temp_value, mood_state)

    def predict_next_design(self):
        temperature_category = self.environmental_data.classify_temperature()
        if temperature_category == "hot" and self.environmental_data.get_mood() == "happy":
            return FabricDesign("Bright", "Stripes")
        elif temperature_category == "hot" and self.environmental_data.get_mood() == "sad":
            return FabricDesign("Dark", "Floral")
        elif temperature_category == "neutral":
            return FabricDesign("Neutral", "Solid")
        else:
            return FabricDesign("Warm", "Plaid")  # Default for cold temperatures





predictor = Predictor()
predictor.update_environmental_data(15, "happy")  # Neutral temperature, happy mood
next_design = predictor.predict_next_design()
print(next_design)

predictor.update_environmental_data(35, "sad")  # Hot temperature, sad mood
next_design = predictor.predict_next_design()
print(next_design.color_scheme)

predictor.update_environmental_data(-5, "neutral")  # Cold temperature, neutral mood
next_design = predictor.predict_next_design()
print(next_design.pattern_type)
