import pytest
from source.Pose import Pose


class TestPoseDetection():
  """
  Testing class for the Pose Module
  """
  @pytest.fixture
  def pose_detection(self):
    return Pose()

  def test_left_arm_up(self,pose_detection):
    """Testmethod for the function left_arm_up in the Pose Module.

    Args:
        pose_detection (Pose): Pose Object
    """
    assert pose_detection.left_arm_up(0, 0, 0, 0) == False
    assert pose_detection.left_arm_up(60, 50, 40, 50) == False
    assert pose_detection.left_arm_up(40, 50, 60, 50) == True

  def test_right_arm_up(self, pose_detection):
    """Testmethod for the function right_arm_up in the Pose Module.

    Args:
        pose_detection (Pose): Pose Object
    """
    assert pose_detection.right_arm_up(0, 0, 0, 0) == False
    assert pose_detection.right_arm_up(60, 50, 40, 50) == True
    assert pose_detection.right_arm_up(40, 50, 60, 50) == False

  def test_arms_crossed(self, pose_detection):
    """
    Testmethod for the function arms_crossed in the Pose Module

    Args:
        pose_detection (Pose): Pose Object
    """
    assert pose_detection.arms_crossed(0, 0) == False
    assert pose_detection.arms_crossed(40, 0) == True
    assert pose_detection.arms_crossed(20, 80) == False

