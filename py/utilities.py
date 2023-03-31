from PIL import Image, ImageDraw, ImageFont
import os


# Add border and text to input images
def editImage(text):

    # iterate through input images
    for imageFile in os.listdir(os.path.join(os.path.dirname(__file__), '../img/input')):
    # for imageName in filenames:

        if imageFile == '.DS_Store':
            continue

        # iterate through borders
        for borderFile in os.listdir(os.path.join(os.path.dirname(__file__), '../img/borders')):

            # open image
            image = Image.open('../img/input/' + imageFile) 
            # get current image size
            iwidth, iheight = image.size
            # strip file extension
            imageName = imageFile.split('.')[0]

            # open border
            border = Image.open('../img/borders/' + borderFile)
            # get border size
            bwidth, bheight = border.size
            # strip file extension
            borderName = borderFile.split('.')[0]
            # shrink border to be the same size as the image
            border = border.resize((iwidth, iheight), Image.LANCZOS)
            # put border over image
            image.paste(border, (0, 0), border.convert('RGBA'))

            # create draw object
            draw = ImageDraw.Draw(image)
            # set font size
            fontSize = 50
            # create font object
            font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), '../fonts', 'Arial Bold.ttf'), fontSize)
            # put text over image
            draw.text((iwidth - 400, fontSize/3), text, font=font, fill=(0, 0, 0))

            
            # save image
            image.save(os.path.join(os.path.dirname(__file__), '../img/output', imageName + '_' + borderName + '.png'))


# Utilities for the project
def main(text):
    editImage(text)
    return


if __name__ == '__main__':
    main("BLACK FRIDAY")
