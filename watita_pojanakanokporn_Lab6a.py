

# main function
def main():
    # var
    MILES_TO_KM = 1
    GAL_TO_LIT = 2
    POUNDS_TO_KG = 3
    INCHES_TO_CM = 4
    FAH_TO_CEL = 5
    
    outfile = open('conversion.txt', 'w')

    # getting input from user
    for num in range(3):
        try:
            menuInput = int(input('What would you like to convert? \n'
                    'Type 1 if you want to convert miles to kilometers. \n'
                    'Type 2 if you want to convert gallons to liters. \n'
                    'Type 3 if you want to convert pounds to kilograms. \n'
                    'Type 4 if you want to convert inches to centimeters. \n'
                    'Type 5 if you want to converts fahrenheit to celsius. \n: '))
            if menuInput not in [MILES_TO_KM, GAL_TO_LIT, POUNDS_TO_KG, INCHES_TO_CM, FAH_TO_CEL]:

                raise Exception(str(menuInput) + ' is an invalid option.') # error message if the input is an invalid option
                    
            else:
                if menuInput ==  MILES_TO_KM:
                    milesToKm()
                    break
                elif menuInput == GAL_TO_LIT:
                    galToLit()
                    break
                elif menuInput == POUNDS_TO_KG:
                    poundsToKg()
                    break
                elif menuInput == INCHES_TO_CM:
                    inchesToCm()
                    break
                elif menuInput == FAH_TO_CEL:
                    fahToCel()
                    break
        except Exception as err:
            print('Error:', err, '\n')
            if num == 2:
                print('You have exceeded the limit. Program has terminated.')
                            
        

#  function to convert miles to kilometers
def milesToKm():
    for num in range(10):
        try:
            miles = float(input('\nPlease tell me how many miles you want converted to kilometers: '))
            if miles < 0:
                print('You cannot enter a negative number, please enter again.')
            if miles >= 0:
                outfile = open('conversion.txt', 'a') # adding result
                outfile.write(str(miles))
                outfile.write(' miles = ')
                kilometers = (miles * 1.6)
                outfile.write(str(format(kilometers, '.2f')))
                outfile.write(' kilometers\n')
                outfile.close
                print(miles, ' miles is equal to ', 
                    format(kilometers,'.2f'), ' kilometers.', sep = '')
        except Exception as err:
            print('Error:', err)
                
    
# function to convert gallons to liters
def galToLit():
    for num in range(10):
        try:
            gallons = float(input('\nPlease tell me how many gallons you want converted to liters: '))
            if gallons < 0:
                print('You cannot enter a negative number, please enter again.')
            if gallons >= 0:
                outfile = open('conversion.txt', 'a') # adding result
                outfile.write(str(gallons))
                outfile.write(' gallons = ')
                liters = (gallons * 3.9)
                outfile.write(str(format(liters, '.2f')))
                outfile.write(' liters\n')
                outfile.close
                print(gallons, ' gallons is equal to ', 
                    format(liters,'.2f'), ' liters.', sep = '')
        except Exception as err:
            print('Error:', err)

    
# function to convert pounds to kilograms    
def poundsToKg():
    for num in range(10):
        try:
            pounds = float(input('\nPlease tell me how many pounds you want converted to kilograms: '))
            if pounds < 0:
                print('You cannot enter a negative number, please enter again.')
            if pounds >= 0:
                outfile = open('conversion.txt', 'a') # adding result
                outfile.write(str(pounds))
                outfile.write(' pounds = ')
                kilograms = (pounds * 0.45)
                outfile.write(str(format(kilograms, '.2f')))
                outfile.write(' kilograms\n')
                outfile.close
                print(pounds, ' pounds is equal to ', 
                    format(kilograms,'.2f'), ' kilograms.', sep = '')
        except Exception as err:
            print('Error:', err)
            
    
# function to convert inches to centimeters    
def inchesToCm():
    for num in range(10):
        try:
            inches = float(input('\nPlease tell me how many inches you want converted to centimeters: '))
            if inches < 0:
                print('You cannot enter a negative number, please enter again.')
            if inches >= 0:
                outfile = open('conversion.txt', 'a') # adding result
                outfile.write(str(inches))
                outfile.write(' inches = ')
                centimeters = (inches * 2.54)
                outfile.write(str(format(centimeters, '.2f')))
                outfile.write(' centimeters\n')
                outfile.close
                print(inches, ' inches is equal to ', 
                    format(centimeters,'.2f'), ' centimeters.', sep = '')
        except Exception as err:
            print('Error:', err)
            
            
# function to convert fahrenheit to celsius
def fahToCel():
    for num in range(10):
        try:
            fahrenheit = float(input('\nPlease tell me how many fahrenheit you want converted to celsius: '))
            if fahrenheit > 1000:
                print('You cannot enter number greater than 1000, please enter again.')
            if fahrenheit <= 1000:
                outfile = open('conversion.txt', 'a') # adding result
                outfile.write(str(fahrenheit))
                outfile.write(' fahrenheit = ')
                celsius = (fahrenheit - 32) * 5 / 9
                outfile.write(str(format(celsius, '.2f')))
                outfile.write(' celsius\n')
                outfile.close
                print(fahrenheit, ' fahrenheit is equal to ', 
                    format(celsius,'.2f'), ' celsius.', sep = '')
        except Exception as err:
            print('Error:', err)
            
            
# call to main function
main()