from PIL import Image, ImageDraw, ImageFont
import os
import argparse


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

            if text:
                # create draw object
                draw = ImageDraw.Draw(image)
                # set font size
                fontSize = 50
                # create font object
                font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), '../fonts', 'Arial Bold.ttf'), fontSize)

                # get text length
                textLength = draw.textlength(text, font=font)
                # put text over image
                draw.text((iwidth - textLength - fontSize/3, fontSize/3), text, font=font, fill=(0, 0, 0))

            # save image
            image.save(os.path.join(os.path.dirname(__file__), '../img/output', imageName + '_' + borderName + '.png'))


# Utilities for the project
def main():

    # parse command line arguments
    parser = argparse.ArgumentParser()
    # add non essential argument
    parser.add_argument("-t", "--text", help="text to be added to the image", required=False)
    args = parser.parse_args()

    text = args.text
    editImage(text)


if __name__ == '__main__':
    main()
