

# main function
def main():
    
    AVG_GRADE_1 = 0
    AVG_GRADE_2 = 100
    
    # checking exception using try/except statement
    try:
        grades_file = open('grades.txt', 'w') # write on grades file
        # run 12 students
        for student in range(12):
            print('Student number', student + 1)
            print('Name', end = '')
            name = str(input(': '))
            print('Grade', end ='')
            score = int(input(': '))

            # limit score to be between 0 and 100 only
            if score >= AVG_GRADE_1 and score <= AVG_GRADE_2:
                grades_file.write(name + '\t')
                grades_file.write(str(score))
                grades_file.write('\n')
                grades_file.write('---------------------')
                grades_file.write('\n')
                
            else:
                while score < AVG_GRADE_1 or score > AVG_GRADE_2:
                    print('Please enter a valid grade', end = '')
                    score = int(input(': '))
                    if score >= AVG_GRADE_1 and score <= AVG_GRADE_2:
                        grades_file.write(name + '\t')
                        grades_file.write(str(score))
                        grades_file.write('\n')
                        grades_file.write('---------------------')
                        grades_file.write('\n')   
        # close grades file
        grades_file.close()
        
        # open grades file in read mode
        grades_file = open('grades.txt', 'r') 
        file_contents = grades_file.read()
        grades_file.close()

        # display the content of the file
        print()
        print('_____(end record)_____\n\n')
        print(file_contents)

    # exception: error messages                    
    except ValueError:
        print('Invalid entry: Grades can only be numeric. Please try again.')
    except IOError:
        print('File does not exist.\n')
        print('Please enter the correct file name.')
    except:
        print('An error occurred. Please try again.')

    
# call to main function
main()
