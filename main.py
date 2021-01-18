import os, webptools, copy, json, plistlib, time
from PIL import Image


# despite the fact that the images say they're png, they're webp files and need to be converted
def convertImages():

    
    for filename in os.listdir('./input'):
        if '.png' in filename:
            webptools.dwebp('./input/'+filename, './input/'+filename, '-o')

def transformImages():
    if not os.path.isdir('./output'):
        os.mkdir('./output')
    
    for filename in os.listdir('./input'):
        if ".plist" in filename:
            with open("./input/"+filename, 'rb') as listfile:
                pl = plistlib.load(listfile)
                img = Image.open("./input/"+filename.split('.')[0]+".png")
                count = 0
                for key, value in pl['frames'].items():
                    count += 1
                    if count != 1:
                        print ("\033[A                             \033[A")
                    print("{} ({}/{}) - {}".format(filename, count, len(pl['frames']), key))
                    time.sleep(0.05)
                    im = copy.copy(img)
                    textureRect = json.loads(value['textureRect'].replace('{', '[').replace('}', ']'))

                    left = textureRect[0][0]
                    top = textureRect[0][1]
                    right = textureRect[0][0] + textureRect[1][0]
                    bottom = textureRect[0][1] + textureRect[1][1]
                    if not value['textureRotated']:
                        seperated = im.crop((left, top, right, bottom))
                    else:
                        right = textureRect[0][0] + textureRect[1][1]
                        bottom = textureRect[0][1] + textureRect[1][0]
                        seperated = im.crop((left, top, right, bottom))
                        seperated = seperated.rotate(90, expand=True)

                    seperated.save('./output/'+key, "PNG")
def main():
    convertImages()
    transformImages()

main()