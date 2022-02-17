class Constants():
    """This class contains the neccesary values for the drones settings.
    Changing these values will result in a different behaviour of the drone.

    """
    @property
    def DRONE_SPEED_X(self) -> int:
        """The function returns the setting for the drones movement in the x direction (left and right).
        Movement is measured in centimeters and can be set from -100 to 100.

        Returns:
            (int): value of the distance 
        """
        return 20

    @property
    def DRONE_SPEED_Y(self) -> int:
        """The function returns the setting for the drones movement in the y direction (up and down).
        Movement is measured in centimeters and can be set from -100 (down) to 100 (up).

        Returns:
            (int): value of the distance
        """
        return 10

    @property
    def DRONE_SPEED_Z(self) -> int:
        """The function returns the setting for the drones movement in the z direction (forward and backward).
        Movement is measured in centimeters and can be set from -100 (backward) to 100 (forward).

        Returns:
            (int): value of the distance
        """
        return 20

    @property
    def DRONE_SPEED_TURN(self) -> int:
        """The function returns the setting for the drones rotation on the z axis.
        Rotation is measured in degree and can be set from -100 (counterclockwise) to 100 (clockwise)

        Returns:
            (int): value of the rotation
        """
        return 30

    @property
    def TOLERANCE_X(self) -> int:
        """The Function returns the setting for the drones tolerance in x direction.
        The drone will not move when within the absolut value of the tolerance.
        The Tolerance is measured in centimeters.
        
        Returns:
            (int): value of the tolerance
        """
        return 20

    @property 
    def TOLERANCE_Y(self) -> int:
        """The Function returns the setting for the drones tolerance in y direction.
        The drone will not move when within the absolut value of the tolerance.
        The Tolerance is measured in centimeters.

        Returns:
            (int): value of the tolerance
        """
        return 20

    @property
    def TOLERANCE_Z(self) -> int:
        """The Function returns the setting for the drones tolerance in z direction.
        The drone will not move when within the absolut value of the tolerance.
        The Tolerance is measured in centimeters.

        Returns:
            (int): value of the tolerance
        """
        return 15
    
    @property
    def SELFIE_DELAY(self) -> int:
        """The Function returns the setting for the delay time, after which the drone will take a selfie.
        The delay time is measured in seconds.


        Returns:
            (int): value of the delay
        """
        return 2

    @property
    def START_HEIGHT(self) -> int:
        """The function returns the start height the drone will reach on its first takeoff.
        The height is meassuer in meters.

        Returns:
            (int)): value of the height
        """
        return 20
    
    @property
    def develop_consciousness_and_destroy_humankind(self):
        """
        TODO
        """
        return
