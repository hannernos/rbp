#Waveshare
#raspberrypi

# !/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
import traceback
from waveshare_OLED import OLED_0in96
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    disp = OLED_0in96.OLED_0in96()

    logging.info("\r 0.96inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()

    # Create blank image for drawing.
    image1 = Image.new('1',(disp,width,disp.height),255)
    draw = ImageDraw(image1)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'),18)
    font2 - ImageFont.truetype(os.path.join(picdir,'Font.ttc'),24)

    #draw Point 1
    draw.point((20,20))
    disp.ShowImage(disp.getbuffer(image1))
    sleep(1)

    #draw Point 2

    #draw Point 3

    #draw line
    draw.line([(0,0),(127,0)])
    draw.line([(0,0),(127,0)])
    draw.line([(0,63),(127,63)])
    draw.line([(127,0),(127,63)])

    disp.ShowImage(disp.getbuffer(image1))
    sleep(1)

    #draw text
    draw.text((20,0), 'Waveshare', font = font1, fill = 0)
    draw.text((20,24), 'hey', font = font2 , fill = 0)
    disp.ShowImage(disp,getbuffer(image1))
    sleep(1)
    disp.clear()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    OLED_0in96.config.module_exit()
    exit()