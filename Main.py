import board
import busio as io
import adafruit_mlx90614
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import sleep
import time
import oxyMeter

mx30 = max30100.MAX30100()
mx30.enable_spo2()

# while 1:



# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)



# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx =adafruit_mlx90614.MLX90614(i2c)
a1=5
listAmbTemp = []
listbt= []
while 1:
    for x in range (a1):

        ambiantTemp ="{:.2f}".format(mlx.ambient_temperature)
        targetTemp ="{:.2f}".format(mlx.object_temperature)
        #print(type(ambiantTemp))
        print("ambiant temperature:", ambiantTemp ,"\N{DEGREE SIGN}C")
        print("body temperature:", targetTemp ,"\N{DEGREE SIGN}C")


        listAmbTemp.append(float(ambiantTemp))
        listbt.append(float(targetTemp))
        #averageAmbiantTemp = (val1+val2)
        mx30.read_sensor()

        mx30.ir,max.red
        hb = int(mx30.inr / 100)
        spo2 = int(mx30.red / 100)


        if mx30.ir != mx30.buffer_ir :
            print("Pulse:",hb);

        if mx.red != mx30.buffer_red :
            print ("SPO2:",spo2);

        # time.sleep(2)


        sleep(2)
    averageAmbiantTemp = ((listAmbTemp[0]+listAmbTemp[1]+listAmbTemp[2]+listAmbTemp[3]+listAmbTemp[4])/5)
    averageAmbiantTemp =round(averageBodyTemp, 2)
    averageBodyTemp = ((listbt[0]+listbt[1]+listbt[2]+listbt[3]+listbt[4])/5)
    averageBodyTemp = round(averageBodyTemp, 2)
    print("average ambient temperature",averageAmbiantTemp)
    print("average Body temperature", averageBodyTemp)
    listAmbTemp.clear()
    listbt.clear()
    # Load default font.
    font = ImageFont.load_default()
    # draw.text((x, top),    'Temp: '+ averageBodyTemp,  font=font, fill=255,)
    # draw.text((x, top+10), 'SpO2: ', font=font, fill=255)
    draw.text((x, top),       "SpO2" + str(spo2),  font=font, fill=255)
    draw.text((x, top+8),    'Temp: '+ str(averageBodyTemp), font=font, fill=255)
    draw.text((x, top+16),    'Bp: Normal',  font=font, fill=255)
    draw.text((x, top+25),    'Pulse: 'str(hb),  font=font, fill=255)


    # Display image.
    disp.image(image)
    disp.display()
    sleep(2)
#print(listAmbTemp[0])

