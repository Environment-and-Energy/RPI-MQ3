from adafruit_circuitplayground.express import cpx
import time
import analogio
import board

cpx.pixels[0] = (0, 90, 0)  # coded red, green, blue
cpx.pixels[1] = (0, 0, 90)  # pixel 1 blue when collecting data

print("sensor is running.....")

mq3 = analogio.AnalogIn(board.A1)

# run sensor for one minutes
count = 0

with open("/data.csv", "a") as fp:
    # adds a set heading
    fp.write("alcohol concentration \n")
    fp.close()

while count < 120:
    alcohol = mq3.value
    try:
        with open("/data.csv", "a") as fp:

            print(alcohol)
            fp.write(str(alcohol)+'\n')
            # fp.flush()
            time.sleep(1)
            count += 1
            # set pixel to green to show done
    # handle error exception
    except OSError as e:
        if e.args[0] == 30:  # device is read only
            message_color = (181, 90, 0)
            cpx.pixels[1] = (0, 0, 0)           # Blank NeoPixel 1
            message_color = (99, 0, 0)          # Red for generic problem
        if e.args[0] == 28:                     # Device out of space
            message_color = (228, 160, 40)      # set to Orange
        elif e.args[0] == 30:                   # Device is read only
            message_color = (181,  90,  0)      # set to Yellow
        for x in range(1, 3):                   # Flash message 3 seconds
            cpx.pixels[0] = message_color
            time.sleep(1)
            cpx.pixels[0] = (0, 0, 0)
# Turn LED to green when finished data collecting
cpx.pixels[1] = (0, 90, 0)
