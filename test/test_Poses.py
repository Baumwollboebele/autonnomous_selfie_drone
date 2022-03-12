import pytest
from source.Pose import Pose


class TestPoseDetection():
  """
  Testing class for the PoseDetection Module
  """
  @pytest.fixture
  def pose_detection(self):
    return Pose()
  
  def test_left_arm_up(self,pose_detection):
    """Testmethod for the function left_arm_up in the PoseDetection Module.

    Args:
        pose_detection (PoseDetection): PoseDetection Object
    """
    assert pose_detection.left_arm_up(0, 0, 0, 0) == False
    assert pose_detection.left_arm_up(60, 50, 40, 50) == True
    assert pose_detection.left_arm_up(40, 50, 60, 50) == False
  

  def test_right_arm_up(self, pose_detection):
    """Testmethod for the function right_arm_up in the PoseDetection Module.

    Args:
        pose_detection (PoseDetection): PoseDetection Object
    """
    assert pose_detection.right_arm_up(0, 0, 0, 0) == False
    assert pose_detection.right_arm_up(60, 50, 40, 50) == False
    assert pose_detection.right_arm_up(40, 50, 60, 50) == True