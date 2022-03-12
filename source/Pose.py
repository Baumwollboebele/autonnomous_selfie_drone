"""
This Module handles pose detection related tasks.
"""


class Pose():
    """
    Handles the functions needed for the pose detection
    """

    @staticmethod
    def left_arm_up(right_wrist, right_shoulder, left_wrist,
                    left_shoulder) -> bool:
        """
        Function detects when the left arm is held up and the right
        arm is in an normal position (below the shoulder)

        Args:
            right_wrist (int): y value of the right wrist in the video frame

            right_shoulder (int): y value of the right shoulder
            in the video frame

            left_wrist (int): y value of the left wrist in the video frame

            left_shoulder (int): y value of the left shoulder
            in the video frame

        Returns:
            bool: True if left arm is up, false if left arm is down.
        """

        if left_wrist > left_shoulder and right_wrist < right_shoulder:
            return True
        return False

    @staticmethod
    def right_arm_up(right_wrist, right_shoulder, left_wrist,
                     left_shoulder) -> bool:
        """
        Function detects when the right arm is held up and the left arm is in a
        normal position (below the shoulder)

        Args:
            right_wrist (int): y value of the right wrist in
            the video frame

            right_shoulder (int): y value of the right shoulder in 
            the video frame

            left_wrist (int): y value of the left wrist in the video frame

            left_shoulder (int): y value of the left shoulder
            in the video frame

        Returns:
            bool: True if right arm is up, false if right arm is down.
        """

        if right_wrist > right_shoulder and left_wrist < left_shoulder:
            return True
        return False

    @staticmethod
    def arms_crossed(right_wrist_x, left_wrist_x):
        """
        Function detects when bot arms are held in a cross position.

        Args:
            right_wrist_x (int): x value of the right wrist in the
            video frame

            left_wrist_x (int): x value of the left wrist in the
            video frame

        Returns:
            bool: True if wrists are crossed.
            Right wrist on the left side of the left wrist.
        """

        if right_wrist_x > left_wrist_x:
            return True
        else:
            return False
