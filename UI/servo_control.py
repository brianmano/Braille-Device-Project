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
        text_results = {
            '0' : [2, 4, 5],
            '1' : [1],
            '2' : [1, 2], 
            '3' : [1, 4],
            '4' : [1, 4, 5],
            '5' : [1, 5],
            '6' : [1, 2, 4],
            '7' : [1, 2, 4, 5],
            '8' : [1, 2, 5], 
            '9' : [2, 4], 
            'default' : [] #default, no motors turn on 
        }

        # retrieve the value associated with the key ('text'), otherwise returns default
        # send holds the list of commands to be sent based on the value of 'text' in the dictionary
        send = text_results.get(text, text_results['default'])

        # send commands to servo
        for commands in send:
            self.send_command(commands)


    def close_connection(self):
        self.ser.close()