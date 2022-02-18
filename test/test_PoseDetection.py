import unittest
from source.PoseDetection import PoseDetection

class TestPoseDetection(unittest.TestCase):
  
  def test_left_arm_up(self):
    pd = PoseDetection()
    self.assertEqual(pd.left_arm_up(0,0,0,0),False)
    
  def test_right_arm_up(self):
    self.assertEqual(True,True)
    

if __name__ == '__main__':
    unittest.main()
