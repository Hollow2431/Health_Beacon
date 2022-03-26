import board
import busio as io
import adafruit_mlx90614
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import sleep

RST = 24

DC = 23
SPI_PORT = 0
SPI_DEVICE

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1',(width,height))
draw = ImageDraw.Draw(image)

paddin

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

        sleep(2)
    averageAmbiantTemp = ((listAmbTemp[0]+listAmbTemp[1]+listAmbTemp[2]+listAmbTemp[3]+listAmbTemp[4])/5)
    averageAmbiantTemp =round(averageBodyTemp, 2)
    averageBodyTemp = ((listbt[0]+listbt[1]+listbt[2]+listbt[3]+listbt[4])/5)
    averageBodyTemp = round(averageBodyTemp, 2)
    print("average ambient temperature",averageAmbiantTemp)
    print("average Body temperature", averageBodyTemp)

    sleep(20)
#print(listAmbTemp[0])
