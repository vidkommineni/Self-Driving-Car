from turtle import *

global i


def intro():
    # intro
    print("***********************************")
    print("** Welcome to the Car Simulator! **")
    print("***********************************")
    # direction_file = input("Please enter the file containing your directions: ")


def screenStartUp():
    """
     sets up the main graphics window / screen

    :return: none
    """

    title('Self Driving Car')  # title of the graphics window
    screen = Screen()  # screen object to customize the screen
    screen.screensize(100, 100)
    screen.bgcolor('darkgreen')  # making the background color of the screen light green
    screen.bgpic('kyle_large.png')  # setting main background of the screen as a street map of kyle field
    screen.register_shape('truck.gif')  # registering the car.gif image as a shape to make the car look like a car
    screen.register_shape('foward_arrow.gif') #registering the forward_arrow.gif image as a shape to look like the forward arrow
    screen.register_shape('back_arrow.gif') #regisstering the back_arrow.gif image as a shape to look like the back arrow


def makeCar(): #calls this function to actually set up the car image
    """
    makes the car that will drive around the screen

    :return: car

    """

    car = Turtle()  # turtle object that will drive around the screen
    car.pensize(width=3)  # increasing the pensize, so you can actually see the trail the car is taking
    car.pencolor('red')  # changing the color to red to it is easier to see
    car.hideturtle()  # Making the turtle disappear, so you don't have to see it when it is aligned
    car.shape('truck.gif')  # making the car object into a car instead of a triangle
    car.penup()  # picking up the pen, so it doesn't make a trail while getting aligned
    car.back(25)  # aligning the car, so it looks like it is starting on the road by kyle field
    car.left(90)
    car.forward(40)
    car.right(90)
    car.speed(1)  # slowing the speed down, so it looks more like the car is driving
    car.pendown()
    car.showturtle()  # making the car appear ready to follow the map directions
    return car


def makeButton(): #This function makes the forward and backward button
    """
    Front and back button objects to go back and forth on path

    :return: fArrow and bArrow

    """

    fArrow = Turtle() #Turtle object at the bottom of the screen that proceeds to the next step
    fArrow.speed(0) #No speed because it is not moving anywhere
    fArrow.hideturtle() #hiding it before adjusting it into position
    fArrow.penup()
    fArrow.shape('foward_arrow.gif') #making the fArrow into the forward arrow button
    fArrow.right(90) #aligning the arrow so it is at the bottom of the screen
    fArrow.forward(290)
    fArrow.left(90)
    fArrow.forward(50)

    bArrow = Turtle() #Turtle object at the bottom of the screen that proceeds to the next step
    fArrow.speed(0)
    bArrow.hideturtle()
    bArrow.penup()
    bArrow.shape('back_arrow.gif') #making the bArrow into the backward arrow button
    bArrow.right(90)
    bArrow.forward(290)
    bArrow.left(90)
    bArrow.back(50)

    fArrow.showturtle() #Shows the forward arrow after it has been placed at the bottom of the screen
    bArrow.showturtle() #Shows the backward arrow after it has been placed at the bottom of the screen

    return fArrow, bArrow


def getDirection(keyString):
    """
    function that checks for keywords in the direction string and
    returns the appropriate direction to take

    :param: keyString:
        String that is being searched for in keywords
    :return: direction:
        direction to take based on the keyword
    :return: -1:
        if there is no keywords & directions that line up in the string
    """

    keyString[0] = keyString[0].lower()  # making string lowercase to prevent keywords from being case-sensitive

    # different keywords to check the string against
    keywords = [
        'head',
        'turn',
        'continue',
        'slight'
    ]

    # print(keyString[0])
    if keywords[0] in keyString[0]: #checking if 'head' from keywords is in the line
        newString = keyString[0].split() #splits the sentance and adds each word to a list
        num = newString.index(keywords[0]) #gets the index value of 'head' in the sentance
        return newString[num + 1] #returns the word in the index of num+1 (That is the place where the directions are located)

    elif keywords[1] in keyString[0]: #checking if 'turn' from keywords is in the line
        newString = keyString[0].split() #splits the sentance and adds each word to a list
        num = newString.index(keywords[1]) #gets the index value of 'head' in the sentance
        return newString[num + 1] #returns the word in the index of num+1 (That is the place where the directions are located)

    elif keywords[2] in keyString[0]: #checking if 'continue' from keywords is in the line
        return keywords[2] #Just returns continue because the direction is not changing (same direction as the most recent line)

    elif keywords[3] in keyString[0]: #checking if 'slight' from keywords is in the line
        newString = keyString[0].split()
        num = newString.index(keywords[3])
        return keywords[3] + " " + newString[num + 1] #returns the key word 'slight' along with the direction at the index num+1

    return -1  # no keywords in the string


def moveDistance(keyString):
    """
    a function that takes a string for its distance and returns the scaled distance

    :param: keyString:
        String that is being searched for the distance and scale
    :return: scaled:
        scaled version of the distance in miles
    """
    
    #key values to check the units for the numebers (mile, ft, seconds)
    dVals = [
        'mi',
        'ft',
        's'
    ]

    scale = 125 #zooms in or out of the map
    print(keyString[len(keyString) - 1])
    if dVals[0] in keyString[len(keyString) - 1]: #checking if 'mi' is in the sentance
        newString = keyString[len(keyString) - 1].split() #splitting the values in the string and saving into a list
        num = newString.index(dVals[0]) #getting the index of 'mi'
        return float(newString[num - 1]) * scale #returning the value before the index (i.e. a number), and multiplying it by scale to move

    elif dVals[1] in keyString[len(keyString) - 1]: #checking if 'ft' is in the sentance
        newString = keyString[len(keyString) - 1].split()
        num = newString.index(dVals[1])
        return (float(newString[num - 1]) / 5280) * scale

    elif dVals[2] in keyString[len(keyString) - 1]: #checking if 's' is in the sentance. 
        if dVals[0] in keyString[len(keyString) - 1]: #checking if 'mi' is in it again bc second is a time so need to check for distance
            newString = keyString[len(keyString) - 1].replace('(', '').replace(')', '').split() #removing the parenthesis
            num = newString.index(dVals[0]) #getting the index value of 'mi'
            return float(newString[num - 1]) * scale

        if dVals[1] in keyString[len(keyString) - 1]: #checking for 'ft' to find the haw far to go in the given seconds
            newString = keyString[len(keyString) - 1].replace('(', '').replace(')', '').split()
            num = newString.index(dVals[1])
            return (float(newString[num - 1]) / 5280) * scale

    return -1 #none of the keywords are in the given string


def followDirections(car, fB, bB, file):
    """
    a function that take the car object and follows the directions
    from the given text file

    :param: car:
        car object that is following the directions while drawing the lines
    :param: file:
        text file to get directions from
    :return:
    """

    # a dictionary with all the directions or direction abbreviations in it
    compasDirections = {'north': 90,
                        'N': 90,
                        'south': 270,
                        'S': 270,
                        'east': 0,
                        'E': 0,
                        'west': 180,
                        'W': 180,
                        'northeast': 45,
                        'NE': 45,
                        'northwest': 135,
                        'NW': 135,
                        'southeast': 315,
                        'SE': 315,
                        'southwest': 225,
                        'SW': 225}

    with open(file, 'r') as file:  # opening the file to read
        data = file.read()
        lines = data.split("\n\n")  # splitting it by every two lines
        # print(line)

        for x in range(len(lines)):
            # splits each index where there is a '/n' and adds that as a list to index lines[i]
            lines[x] = lines[x].split('\n')
        print(lines)

        i = 1

        while i < len(lines): #keeps iterating until i is less than length
            print(lines[i])
            print(getDirection(lines[i]))
            # print(moveDistance(line))

            if getDirection(lines[i]) in compasDirections: #checking to see if the the output from the getDirection function is in the compas
                car.setheading(compasDirections[getDirection(lines[i])]) #sets the direction of the turtle to the angle of the returned direction value
                car.forward(moveDistance(lines[i])) #actually makes the turtle move in the returned direction for the returned distance

#only checks these elif statements if the direction is not in the dictionary (not a cardinal direction)
            elif getDirection(lines[i]) == 'right': #if the direction equals right
                car.right(90) #the turtle's orientation is set to 90 degrees
                car.forward(moveDistance(lines[i])) #the car moves for the returned distance in the given orientation

            elif getDirection(lines[i]) == 'slight right': 
                car.right(45) #setting it to 45 because not a full right turn. 
                car.forward(moveDistance(lines[i]))

            elif getDirection(lines[i]) == 'left':
                car.left(90)
                car.forward(moveDistance(lines[i]))

            elif getDirection(lines[i]) == 'slight left':
                car.left(45) #setting to 45 because not a full left turn
                car.forward(moveDistance(lines[i]))

            elif getDirection(lines[i]) == 'continue':
                car.forward(moveDistance(lines[i])) #Does not change direction, so moves in the same direction for the returned distance.

            fB.onclick(forwardClick(i, car))
            bB.onclick(backwardClick(i, car))
            listen()


def forwardClick(i):
    i += 1


def backwardClick(i, car):
    i -= 1
    car.undo()


def main():
    """
    main section of code where all other parts will be implemented

    :param: none

    :return: none
    """
    # directionsFile = 'Kyle2VetPk.txt'
    directionsFile = 'Easterwood2Coulter.txt'
    # try:
    #     directionsFile = input('Please inter the name of the file with directions. ')
    #     open(directionsFile).close()  # making sure file exists
    # except FileNotFoundError:
    #     print('Cannot find file', FileNotFoundError, 'Resorting to test file', 'Kyle2VetPK.txt')
    #     directionsFile = 'Kyle2VetPK.txt'  # if there is no directions file, revert to the original test file

    intro()
    screenStartUp()  # making the screen
    car = makeCar()  # making the car object to drive around
    fB, bB = makeButton()
    followDirections(car, fB, bB, directionsFile)  # follow the directions in the file
    done()
    Terminator()


if __name__ == '__main__':
    main()
