# Write a program that will prompt for a floating-point \ 
# number that stands for gallons of gasoline.


number_str = input('What is the amount of gas in gallons:')
number_float = float(number_str)

number_liters = 3.78541*number_float
number_barrels = number_float/19.5
number_co2 = 20*number_float
equivalent_energy_ethanol = number_float*1.5*75700
number_price = number_float*3


print('Number of liters:', number_liters)
print('Number of barrels required to make this amount:', number_barrels)
print('Number of pounds of co2 produced:', number_co2)
print('the energy amount in ethanol is:', equivalent_energy_ethanol)
print('the price in US dollars is:', number_price)


# Write a program that takes years as input \
# and points out an estimated population.

yrs_str = input('Enter the number of years:')
yrs_int = int(yrs_str)

current_population = 307357870
year = 365*86400

births_year = 4505143
deaths_year = 2425846
immigrant_year = 900971

new_pop = current_population + (births_year - deaths_year + immigrant_year) * yrs_int

print('New population:', new_pop)