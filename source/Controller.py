from Constants import Constants
from djitellopy import tello


class Controller():
    def __init__(self) -> None:
        """
        Initialoization of class variables.
        """

        self.const = Constants()

        self.drone = tello.Tello()

        self.up_down_velocity = 0
        self.right_left_velocity = 0
        self.forward_backward_velocity = 0
        self.turn_velocity = 0

    def start(self):
        """
        Function starts the drone, it's video recording.
        """
        self.drone.connect()
        self.drone.takeoff()
        self.drone.streamon()

    def battery(self):
        """
        Function prints the current battery level of the drone in percent.
        """
        print(f"Battery at {self.drone.get_battery()}%")

    def set_velocity(self, vel):
        """
        Function sets the veolitiy of the drone in cm/s

        Args:
            vel (int): speed of the drone in cm/s
        """
        self.drone.set_speed(vel)

    def move(self, x, y):
        """
        Function utilizes the vector from the center of the camera
        to the detected nose.
        Depending on the x values orientation the drone is
        either turned left or right.
        Deoending on the y values orientation the drone is either
        moved up or down.

        Args:
            x (int): x component of the vector
            (Centre of camera image to nose)

            y (int): y component of the vecgtor
            (centre of camera image to nose)
        """

        self.reset()

        # TURN
        if x < - self.const.TOLERANCE_X:
            self.turn_velocity = - self.const.DRONE_SPEED_TURN

        elif x > self.const.TOLERANCE_X:
            self.turn_velocity = self.const.DRONE_SPEED_TURN
        else:
            pass

        # UP DOWN
        if y < - self.const.TOLERANCE_Y:
            self.up_down_velocity = self.const.DRONE_SPEED_Y
        elif y > self.const.TOLERANCE_Y:
            self.up_down_velocity = - self.const.DRONE_SPEED_Y
        else:
            pass

        self.drone.send_rc_control(self.right_left_velocity,
                                   self.forward_backward_velocity,
                                   self.up_down_velocity, self.turn_velocity)

    def move_pose(self, pose):
        """
        Function moves the drone if a pose is detected:
            - Right arm up
            - Left arm up
            - Arms crossed

        Args:
            pose (string): String identifier of the pose.
        """

        self.reset()

        if pose == "left":
            self.right_left_velocity = -self.const.DRONE_SPEED_X
        elif pose == "right":
            self.right_left_velocity = +self.const.DRONE_SPEED_X
        else:
            self.right_left_velocity = 0

        self.drone.send_rc_control(self.right_left_velocity, 0, 0, 0)

    def stop(self):
        """
        Function stops the drones movement.
        """
        self.drone.send_rc_control(0, 0, 0, 0)

    def start_height(self):
        """
        Function sets the starting height of the drone.
        """
        self.drone.send_rc_control(0, 0, self.const.START_HEIGHT, 0)

    def reset(self):
        """
        Function resets all velocity values of the drone.
        """
        self.up_down_velocity = 0
        self.right_left_velocity = 0
        self.forward_backward_velocity = 0
        self.turn_velocity = 0

    def get_stream(self):
        """
        Function returnes the current frame of the video stream.

        Returns:
            (frame): Current Frame of the video stream.
        """
        return self.drone.get_frame_read().frame
