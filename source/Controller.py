from Constants import Constants
from djitellopy import tello


class Controller():
    def __init__(self) -> None:
        """
        _summary_
        """

        self.const = Constants()

        self.drone = tello.Tello()

        self.up_down_velocity = 0
        self.right_left_velocity = 0
        self.forward_backward_velocity = 0
        self.turn_velocity = 0

    def start(self):
        self.drone.connect()
        self.drone.takeoff()
        self.drone.streamon()

    def battery(self):
        print(f"Battery at {self.drone.get_battery()}%")

    def set_velocity(self, vel):
        self.drone.set_speed(vel)

    def move(self, x, y, distance):
        """
        _summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_
            distance (_type_): _description_
        """

        self.reset()

        # TURN
        if x < - self.const.TOLERANCE_X:
            print("Move drone to the right.")
            self.turn_velocity = - self.const.DRONE_SPEED_TURN

        elif x > self.const.TOLERANCE_X:
            print("Move drone to the left")
            self.turn_velocity = self.const.DRONE_SPEED_TURN
        else:
            print("OK")

        # UP DOWN
        if y < - self.const.TOLERANCE_Y:
            print("move drone up.")
            self.up_down_velocity = self.const.DRONE_SPEED_Y
        elif y > self.const.TOLERANCE_Y:
            print("Move drone down.")
            self.up_down_velocity = - self.const.DRONE_SPEED_Y

        else:
            print("OK")

        # FORWARD BACKWARD
        # if distance < self.const.DISTANCE - self.const.TOLERANCE_DISTANCE:
        #     self.forward_backward_velocity = self.const.DRONE_SPEED_Z
        #     print("Move drone towards person")
        # elif distance > self.const.DISTANCE + self.const.TOLERANCE_DISTANCE:
        #     self.forward_backward_velocity = -self.const.DRONE_SPEED_Z
        #     print("Move drone away from person.")
        # else:
        #     print("OK")

        self.drone.send_rc_control(self.right_left_velocity,
                                   self.forward_backward_velocity,
                                   self.up_down_velocity, self.turn_velocity)

    def move_pose(self, pose):
        """
        _summary_

        Args:
            pose (_type_): _description_
        """

        self.reset()

        if pose == "left":
            self.right_left_velocity = -self.const.DRONE_SPEED_X
            print("POSE DETECTED: Move left.")
        elif pose == "right":
            self.right_left_velocity = +self.const.DRONE_SPEED_X
            print("POSE DETECTED: Move right.")
        else:
            self.right_left_velocity = 0

        self.drone.send_rc_control(self.right_left_velocity, 0, 0, 0)

    def stop(self):
        self.drone.send_rc_control(0, 0, 0, 0)

    def start_height(self):
        self.drone.send_rc_control(0, 0, self.const.START_HEIGHT, 0)

    def reset(self):
        self.up_down_velocity = 0
        self.right_left_velocity = 0
        self.forward_backward_velocity = 0
        self.turn_velocity = 0

    def get_stream(self):
        return self.drone.get_frame_read().frame
