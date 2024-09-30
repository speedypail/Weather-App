import sys
import requests, json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

# Weather app class using PyQt5
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Setting up the window
        self.setWindowTitle("Colorful Weather App")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #2d2d2d;")  # Dark background

        
        self.layout = QVBoxLayout()

        
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.setFixedHeight(40)
        self.city_input.setStyleSheet("background-color: #fff; color: #000; font-size: 18px; padding: 10px;")
        self.layout.addWidget(self.city_input)

        # Search button
        self.search_button = QPushButton("Get Weather", self)
        self.search_button.setFixedHeight(40)
        self.search_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px;")
        self.search_button.clicked.connect(self.get_weather)
        self.layout.addWidget(self.search_button)

        # Label to display weather result
        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("color: white; font-size: 16px; padding: 10px;")
        self.layout.addWidget(self.result_label)

        # Set layout
        self.setLayout(self.layout)

    def get_weather(self):
        # Fetch the weather information
        city = self.city_input.text()
        if city:
            api_key = "20f34a4af93f6f1a8e5abc53c3f2b46c"  
            base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            
            try:
                response = requests.get(base_url)
                data = response.json()

                if data["cod"] == 200:
                    temp = data["main"]["temp"]
                    description = data["weather"][0]["description"]
                    humidity = data["main"]["humidity"]
                    wind_speed = data["wind"]["speed"]

                    # Format the result
                    weather_info = (
                        f"Weather in {city.capitalize()}:\n\n"
                        f"Temperature: {temp}°C\n"
                        f"Description: {description.capitalize()}\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s"
                    )

                    self.result_label.setText(weather_info)
                    self.result_label.setStyleSheet("color: #4CAF50; font-size: 16px; padding: 10px;")
                else:
                    self.result_label.setText("City not found. Please enter a valid city.")
                    self.result_label.setStyleSheet("color: #FF0000; font-size: 16px; padding: 10px;")
            except Exception as e:
                self.result_label.setText("Error fetching weather data.")
                self.result_label.setStyleSheet("color: #FF0000; font-size: 16px; padding: 10px;")
        else:
            self.result_label.setText("Please enter a city name.")
            self.result_label.setStyleSheet("color: #FF0000; font-size: 16px; padding: 10px;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
