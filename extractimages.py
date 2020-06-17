from PIL import Image
import cv2
import time

def getimages(im):
    width, height, channel = im.shape
    # The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate.

    # Det her crop finder det kort der er nyt fra bunken.

    crop_newcard = (6 * width / 7, 0, 7 * width / 7, height / 4)
    # Nederste y punkt : øverste y punkt, nederste x punkt, højeste x punkt.
    # Width er cirka 1000px på mit kamera
    # Height er cirka 1900px - Gustav
    # Navngivet fra venstre mod højre
    building_pile1= im[int(width/4):int(width), 0:int((height/7) * 1)]
    building_pile2 = im[int(width / 4):int(width), int(height / 7) * 1:int((height / 7) * 2)]
    building_pile3 = im[int(width / 4):int(width), int(height / 7) * 2:int((height / 7) * 3)]
    building_pile4 = im[int(width / 4):int(width), int(height / 7) * 3:int((height / 7) * 4)]
    building_pile5 = im[int(width / 4):int(width), int(height / 7) * 4:int((height / 7) * 5)]
    building_pile6 = im[int(width / 4):int(width), int(height / 7) * 5:int((height / 7) * 6)]
    building_pile7 = im[int(width / 4):int(width), int(height / 7) * 6:int((height / 7) * 7)]

    # Det her kort er det nye kort der bliver vendt fra bunken.
    pilecard = im[0:int(width/4), int(height/7) * 1:int((height/7) * 2)]
    cv2.imwrite('pilecard.png', pilecard)

    dict0 = {'name': 'Pilecard', 'img': pilecard}
    dict1 = {'Name': 'pile1', 'img': building_pile1}
    dict2 = {'Name': 'pile2', 'img': building_pile2}
    dict3 = {'Name': 'pile3', 'img': building_pile3}
    dict4 = {'Name': 'pile4', 'img': building_pile4}
    dict5 = {'Name': 'pile5', 'img': building_pile5}
    dict6 = {'Name': 'pile6', 'img': building_pile6}
    dict7 = {'Name': 'pile7', 'img': building_pile7}

    imagelist = [pilecard, building_pile1, building_pile2, building_pile3, building_pile4, building_pile5, building_pile6, building_pile7]
    return imagelist
