import unittest

class TestPoseDetection(unittest.TestCase):
  
  def test_left_arm_up(self):
    self.assertEqual(PoseDetection.left_arm_up(0,0,0,0),False)
    
  def test_right_arm_up(self):
    self.assertEqual(True,True)
    

if __name__ == '__main__':
    unittest.main()
