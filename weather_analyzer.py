#importing random module
import random

#lists
previous_month_daily_temperatures = [random.randint(0,35) for _ in range(30)]
daily_temperatures = [random.randint(0,35) for _ in range(30)]
daily_rainfall = [random.randint(0,10) for _ in range(30)]

lowest_temp = daily_temperatures[0]
highest_temp = daily_temperatures[0]
temp_above_20 = []
temp_below_10 = []
temp_increased = []
hotter = []
n = 0
bad_weather = 0
average_weather = 0
good_weather = 0 

#finding the lowest/highest temperature
for temp in daily_temperatures:
  if temp < lowest_temp: #1)finding the lowest temperature
    lowest_temp = temp
  if temp > highest_temp: #1)finding the highest temperature
    highest_temp = temp

for index, temp in enumerate(daily_temperatures):
    if temp > 20:
        temp_above_20.append(index+1) #1)finding days where temperature was above 20 degrees
    if temp < 10:
       temp_below_10.append(index+1) #1)finding days where temperature was below 10 degrees

#1)finding the highest temperature
for index, temp in enumerate(daily_temperatures[:-1]):
  if temp < daily_temperatures[n+1]:
    temp_increased.append(index+2)

#1)finding days where the temperature was hotter than any of the days previous in the month
for index, temp in enumerate(daily_temperatures):
  if temp > previous_month_daily_temperatures[index]:
    hotter.append(index+1)

#2)finding bad weather, average weather and good weather
for index, temp in enumerate(daily_temperatures):
  if temp < 10 and daily_rainfall[index] > 3:
    bad_weather+=1
  if 9 < temp < 19 and 0 < daily_rainfall[index] < 6:
    average_weather+=1
  if temp > 18 and daily_rainfall[index] < 2:
    good_weather+=1


#Outputs
print("Temperatures list: " + str(daily_temperatures))
print("The lowest temperature was " + str(lowest_temp) + " degrees Celsius")
print("The highest temperature was " + str(highest_temp) + " degrees Celsius")
print("Temperature was above 20 degrees Celsius on the following days: " + str(temp_above_20))
print("Temperature was below 10 degrees Celsius on the following days: " + str(temp_below_10))
print("These are the days where the temperature increased from the day before: " + str(temp_increased))
print("These are the days where the temperature was hotter than any of the days previous in the month: " + str(hotter))
print("The amount of 'bad weather' days is: " + str(bad_weather))
print("The amount of 'average weather' days is: " + str(average_weather))
print("The amount of 'good weather' days is: " + str(good_weather))