import unittest
from source.PoseDetection import PoseDetection

class TestPoseDetection(unittest.TestCase):
  
  def setUp(self):
    self.pd = PoseDetection
  
  def test_left_arm_up(self):
    
    self.assertEqual(pd.left_arm_up(0,0,0,0),False)
    self.assertEqual(pd.left_arm_up(60,50,40,50),True)
    
  def test_right_arm_up(self):
    self.assertEqual(True,True)
    

if __name__ == '__main__':
    unittest.main()
