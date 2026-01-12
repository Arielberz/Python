# מבחן מה״ט 2024 אביב ב` שאלה 9:
class AIQData:
    def __init__(self, date, city,popul,aiq):
        self.date = date
        self.city = city
        self.popul = popul
        self.aiq = aiq

    def raiting(self):
        if self.aiq < 50:
            return "Good"
        elif self.aiq < 100:
            return "Moderate"
        elif self.aiq < 150:
            return "Unhealthy for Sensitive Groups"
        elif self.aiq < 200:
            return "Unhealthy"
        return "Hazardous"
    def print_dangerous(arr,check_date):
        result = []
        for data in arr:
            if data.date == check_date and data.raiting() in ["Unhealthy", "Hazardous"]:
                result.append(f"City: {data.city}, AQI: {data.aiq}, Rating: {data.raiting()}")
        print(result)

    def print_cities(arr,cities):
        for city in cities:
             countbed = 0
             countgood = 0
             for data in arr:
                    if data.city == city:
                         r = data.raiting()
                         if r == "Hazardous": countbed += 1
                         elif r == "Good": countgood += 1                 
             print(f"City: {city},days off Hazardous: {countbed}, days of Good: {countgood}")           
        