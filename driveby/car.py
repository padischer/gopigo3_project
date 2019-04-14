import easygopigo3 as easy
import sys
import time
import logging

class car:

    ismoving = False
    gpg = easy.EasyGoPiGo3()

    def drive(self, instructions):
        try:
            my_linefollower = self.gpg.init_line_follower()
            time.sleep(0.1)
        except:
            logging.error('Line Follower not responding')
            time.sleep(0.2)
            sys.exit()
        logging.info("start driving")
        self.gpg.forward()
        while True:
            logging.debug(my_linefollower.read_position())
            if my_linefollower.read_position() == 'black':
                logging.debug("black detected")
                self.gpg.stop()
                self.gpg.drive_cm(5)


                logging.debug(my_linefollower.read_position())
                if my_linefollower.read_position() in ['center', "left", "right"]:
                    next_instruction = instructions[0]
                    
                    logging.debug("executing next instruction")
                    logging.info(next_instruction)
                    if next_instruction is "left":
                       self.gpg.turn_degrees(270)
                    if next_instruction is "right":
                       self.gpg.turn_degrees(90)
                       logging.debug("going forward")
                    self.gpg.forward()
                    del instructions[0]                


                if my_linefollower.read_position() is "white":
                    self.gpg.stop()
                    self.gpg.turn_degrees(180)
                    time.sleep(1.5)
                    return True

            if my_linefollower.read_position() == 'center':
                self.gpg.forward()
            if my_linefollower.read_position() == 'left':
                self.gpg.left()
                self.gpg.left()
#                self.gpg.left()
            if my_linefollower.read_position() == 'right':
                self.gpg.right()
                self.gpg.right()
 #               self.gpg.right()
 