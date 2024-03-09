import serial 
import time


class ServoControl: 
    #'COMx' is our Arduino's port, replace later
    def __init__(self, port='COMx', baud_rate=9600):
        self.ser = serial.Serial(port, baud_rate)
        time.sleep(2)

    def send_command(self, command):
        self.ser.write(str(command).encode())
        #allow arduino to process the command
        time.sleep(1)
 
    def control_servos(self, text):
        if '0' in text:
            self.send_command(2)
            self.send_command(4)
            self.send_command(5)
        elif '1' in text:
            self.send_command(1)
        elif '2' in text:
            self.send_command(1)
            self.send_command(2)
        elif '3' in text:
            self.send_command(1)
            self.send_command(4)
        elif '4' in text:
            self.send_command(1)
            self.send_command(4)
            self.send_command(5)
        elif '5' in text:
            self.send_command(1)
            self.send_command(5)
        elif '6' in text:
            self.send_command(1)
            self.send_command(2)
            self.send_command(4)
        elif '7' in text:
            self.send_command(1)
            self.send_command(2)
            self.send_command(4)
            self.send_command(5)
        elif '8' in text:
            self.send_command(1)
            self.send_command(2)
            self.send_command(5)
        elif '9' in text:
            self.send_command(2)
            self.send_command(4)
        else:
            self.send_command()

    def close_connection(self):
        self.ser.close()