import os


class ADBCmd(object):
    """Android Dubug Bride Cmd using in system"""

    def swipe_screen(self, start_xy, end_xy, press_time=None):
        """swipe screen"""

        # adb shell input swip x1 y1 x2 y2 press_time
        if press_time == None:
            cmd = "adb shell input swipe " \
                + str(start_xy[0]) + " " + str(start_xy[1]) + " " \
                + str(end_xy[0]) + " " + str(end_xy[1]) + " "
        else:
            cmd = "adb shell input swipe " \
                + str(start_xy[0]) + " " + str(start_xy[1]) + " " \
                + str(end_xy[0]) + " " + str(end_xy[1]) + " " \
                + str(press_time)

        print("cmd: ", cmd)
        os.system(cmd)

    def tap_screen(self, xy):
        """tap screen"""

        # adb shell input tap x y
        cmd = "adb shell input tap " \
            + str(xy[0]) + " " + str(xy[1]) + " " \

        print("cmd: ", cmd)
        os.system(cmd)

    def key_event(self, key):
        """make key event"""

        # adb shell input keyevent key
        cmd = "adb shell input keyevent " + str(key)

        print("cmd: ", cmd)
        os.system(cmd)
