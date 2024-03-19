import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    # Add your API key here
    api_key = "e33d93d92c26d657c9955fb87511d562"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
        else:
            messagebox.showerror("Error", f"Error {response.status_code}: Unable to fetch weather data")
    except Exception as e:
        messagebox.showerror("Error", f"Exception: {e}")


# Create the main window
page = tk.Tk()
page.title("Weather App")

page.geometry("400x300") 
# Create and configure widgets
city_label = tk.Label(page, text="City:")
city_label.pack()
city_entry = tk.Entry(page)
city_entry.pack()

fetch_button = tk.Button(page, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

weather_label = tk.Label(page, text="")
weather_label.pack()

# Start the GUI main loop
page.mainloop()
