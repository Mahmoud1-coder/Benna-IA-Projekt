from datetime import datetime
import requests


class BennaAI:

    def __init__(self):
        self.fragrances = {"fresh": ["Citrus", "Green"],
                           "warm": ["Vanilla","Amber"],
                           "relax": ["Lavender", "Chamomile"],
                           "luxury": ["Woody", "Floral"]  
                           } 
        #this fragrances are choosen by IA and could be changed at anytime oder personalised by the user

    def get_temperature(city):
        
        api_key = "c8293c68ee0965af6b59a7fd1a970046"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
        response = requests.get(url)
        data = response.json()

        # Debug print to see what's returned
        print(data)

        # Check if request was successful
        if response.status_code != 200:
            raise Exception(f"API error: {data.get('message', 'Unknown error')}")

        # Safely access temperature
        return data.get("main", {}).get("temp", None)


    temp = get_temperature("Darmstadt")
    

    def get_season(self,month) :
        if month in [12,1,2]:
            return "winter"
        elif month in [3,4,5]:
            return "spring"
        elif month in [6,7,8]:
            return "summer"
        else :
            return "autumn"
        
    def get_day_type(self, weekday):
        if weekday >= 5:
            return "weekend"
        return "workday"

    def get_time_of_day(self, hour):
        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 18:
            return "afternoon"
        elif 18 <= hour < 23:
            return "evening"
        else:
            return "night"
        
    def get_temperature_category(self, temp):
        if temp < 10:
            return "cold"
        elif 10 <= temp < 20:
            return "mild"
        else:
            return "warm"
        
    #lets start to think

    def recommend(self, mood, preference=None):
        now = datetime.now()

        season = self.get_season(now.month)
        time_of_day = self.get_time_of_day(now.hour)
        day_type = self.get_day_type(now.weekday())
        temp_category = self.get_temperature_category(self.temp)

        print(f"[DEBUG] Season: {season}, Time: {time_of_day}, Day: {day_type}, Temp: {temp_category}")
    
    
    # Priority 1: Direct preference
        if preference:
            if preference in self.fragrances:
                return self._select(preference)

    # Priority 2: Mood-based decision
        if mood == "tired":
            return self._select("relax")

        elif mood == "stressed":
            return self._select("relax")

        elif mood == "happy":
            return self._select("fresh")
        
        
    # Priority 3: Context-aware decision
        if season == "winter":
            return self._select("warm")

        elif season == "summer":
            return self._select("fresh")

        # Time-based refinement
        if time_of_day == "morning":
            return self._select("fresh")

        elif time_of_day == "evening":
            return self._select("warm")

        # Weekend luxury mode
        if day_type == "weekend":
            return self._select("luxury")

        return self._select("fresh")

    #Priorety 4: analyse the temp
        if temp_category == "cold":
            return self._select("warm")

        elif temp_category == "warm":
            return self._select("fresh")
    
    def _select(self, category) :
        scents = self.fragrances.get(category, [])
        if not scents:
            return "Defoult scent"
        
        return f"Recommended Blend: {scents[0]} + {scents[-1]}"
    
if __name__ == "__main__":
    ai = BennaAI()

    print(ai.recommend(mood="tired",preference=None))

