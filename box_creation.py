import cv2
import numpy

def detect_lines (src): #src is the image
    src = cv2.imread(src)
    ret, src = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)

    shape = src.shape
    height = shape[0]
    width = shape[1]
    horizontal_lines = helper(src,height,width,True)
    vertical_lines = helper(src, height, width, False)
    # print(horizontal_lines)
    # print(vertical_lines)
    sub_sections = []
    for i in range(len(horizontal_lines) -1):
        section = src[horizontal_lines[i]:horizontal_lines[i+1],vertical_lines[0]:vertical_lines[1]]
        sub_sections.append(section)
    return sub_sections

def helper(src,height,width,horizontal): # if horizontal is true, helper will scan for horizontal lines
    if horizontal == True:
        horizontallines = []
        i = 0
        while i < height: #iterate through the picture horizontally
            colour = src.item(i, int(width / 2), 0)  # channel 1
            colour1 = src.item(i, int(width / 2), 1)  # channel 2
            colour2 = src.item(i, int(width / 2), 2)  # channel 3

            if ((colour == 0) & (colour1 == 0) & (colour2 == 0)):  # if they are black
                i = i + 40 #skip 40 pixels because there tend to be blocks in nutritional labels
                # check whether or not they are lines
                for j in range(-300, 300):
                    colour3 = src.item(i - 40, (int(width / 2) + j), 0)
                    colour4 = src.item(i - 40, (int(width / 2) + j), 1)
                    colour5 = src.item(i - 40, (int(width / 2) + j), 2)

                    if ((colour3 != 0) & (colour4 != 0) & (colour5 != 0)):
                        pass
                    else:
                        horizontallines.append(i - 40)
            else:
                i = i + 1

        horizontallines = numpy.array(horizontallines)
        unique, counts = numpy.unique(horizontallines, return_counts=True)
        dictionary = dict(zip(unique, counts)) #a dictionary of values, the coordinates with the most values are the lines
        dictionary = dict((k, v) for k, v in dictionary.items() if v > 500) #check for the coordinate which has the most values
        horizontallines = list(dictionary.keys())
        return horizontallines
    else:
        verticallines = []
        i = 0
        while i < width:
            colour = src.item(int(height / 2), i, 0)  # channel 1
            colour1 = src.item(int(height / 2), i, 1)  # channel 2
            colour2 = src.item(int(height / 2), i, 2)  # channel 3

            if ((colour == 0) & (colour1 == 0) & (colour2 == 0)):  # if they are black
                i = i + 40
                for j in range(-300, 300):
                    colour3 = src.item((int(width / 2) + j), i - 40, 0)
                    colour4 = src.item((int(width / 2) + j), i - 40, 1)
                    colour5 = src.item((int(width / 2) + j), i - 40, 2)

                    if ((colour3 != 0) & (colour4 != 0) & (colour5 != 0)):
                        pass
                    else:
                        verticallines.append(i - 40)
            else:
                i = i + 1

        verticallines = numpy.array(verticallines)
        unique, counts = numpy.unique(verticallines, return_counts=True)
        dictionary = dict(zip(unique, counts))
        dictionary = dict((k, v) for k, v in dictionary.items() if v > 500)
        verticallines = list(dictionary.keys())
        return verticallines


