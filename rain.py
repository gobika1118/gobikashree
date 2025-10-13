import matplotlib.pyplot as plt

#sample weather data
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temperature = [30,32,31,29,28,27,26]
humidity = [70,65,60,75,80,85,90]
rainfall = [0,5,0,10,20,15,30]

# 1. Line chart - Temperature
plt.figure(figsize=(8,5))
plt.plot(days, temperature, marker=0, color="red", label="Temperature(c)")
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar chart - Humidity
plt.figure(figsize=(8,5))
plt.bar(days,humidity,color="blue")
plt.xlabel("Days")
plt.ylabel("Humidity(%)")
plt.show()

# 3. Scatter plot - Rainfall
plt.figure(figsize=(8,5))
plt.scatter(days,rainfall,color="green",s=100)
plt.title("Weekly Rainfall")
plt.xlabel("Days")
plt.ylabel("Rainfall (mm)")
plt.show()
