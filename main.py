import box_creation
import OCR
import cv2


def main():
    list_of_sections = box_creation.detect_lines("nutritional_label.jpg")
    for i in range(len(list_of_sections)):
        OCR.read_words(list_of_sections[i])

main()

