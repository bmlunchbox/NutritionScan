from PIL import Image
import pytesseract
import difflib

im = Image.open("2.png")
nutrientslist = ["Calories", "Total Fat", "Saturated Fat", "Cholesterol", "Sodium", "Total Carbohydrates",
                 "Dietary Fiber", "Sugars", "Protein", "Vitamin A", "Vitamin C", "Calcium", "Iron", "Potassium"]

text = pytesseract.image_to_string(im, lang= 'eng')

if text.__contains__("%") == False: #if the label does not have a percentage sign such as sugars and protein
  value = ''.join(x for x in text if x.isdigit())
  nutrient  = ''.join(x for x in text if x.isalpha())
  valuen = int(value)
  nutrient = difflib.get_close_matches(nutrient,nutrientslist,1)[0]
  if (valuen>100 & valuen<200000 & valuen%9 ==0):
    print (nutrient + " "+value[:-1]+ "g")
  else:
      print (text)


else: #if the label has a percentage sign
  print(text.replace("9 ", "g "))