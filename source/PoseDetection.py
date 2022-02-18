class PoseDetection():
    def __init__(self) -> None:
        pass


    def left_arm_up(self,right_wrist,right_shoulder,left_wrist,left_shoulder) -> bool:
        """
        Function detects when the left arm is held up and the right arm is in an normal position (below the shoulder)

              +--------+      
              |  x   x |      
              |        |      
              |  ----  |      
              |        |      
              +--------+      
                  |         --
                  |       -/  
                  |    --/    
                  |  -/       
             /----|-/         
         ----     |           
                  |           
                  |           
                  |           
                 / \          
               /-   -\        
             /-       -\      
           /-           -\    
          -               -  

        Args:
            right_wrist (int): y value of the right wrist in the video frame
            right_shoulder (int): y value of the right shoulder in the video frame
            left_wrist (int): y value of the left wrist in the video frame
            left_shoulder (int): y value of the left shoulder in the video frame

        Returns:
            bool: True if left arm is up, false if left arm is down.

        >>> left_arm_up(0,0,0,0)
        False

        >>> left_arm_up(50,45,20,46)
        True

        >>> left_arm_up(30,50,60,50)
        False
        """

        if left_wrist  < left_shoulder and right_wrist > right_shoulder:
            return True
        else:
            return False

    
    def right_arm_up(self,right_wrist,right_shoulder,left_wrist,left_shoulder) -> bool:
        """
        Function detects when the right arm is held up and the left arm is in a normal position (below the shoulder)
        
                 +--------+      
                 |  x   x |      
                 |        |      
                 |  ----  |      
                 |        |      
                 +--------+  
         --          |        
           \--       |        
              \-     |        
                \--  |        
                   \-|--------
                     |        
                     |        
                     |        
                     |        
                    / \       
                  /-   -\     
                /-       -\   
              /-           -\ 
             -               -

        Args:
            right_wrist (int): y value of the right wrist in the video frame
            right_shoulder (int): y value of the right shoulder in the video frame
            left_wrist (int): y value of the left wrist in the video frame
            left_shoulder (int): y value of the left shoulder in the video frame

        Returns:
            bool: True if right arm is up, false if right arm is down.
        """

        if right_wrist  < right_shoulder and left_wrist > left_shoulder:
            return True
        else:
            return False
    
    def arms_crossed(self,right_wrist,left_wrist) -> bool:
        """
        #     +--------+      
        #     |  x   x |      
        #     |        |      
        #     |  ----  |      
        #     |        |      
        #     +--------+                    
        #  --     |     --                  
        #    \--  |  --/                    
        #       \---/                       
        #     --/ | \--                     
        #   -/    |    \-                   
        #  +------|------+                  
        #         |                         
        #         |                        
        #         |                         
        #        / \                        
        #      /-   -\                      
        #    /-       -\                    
        #  /-           -\                  
        # -               -     
        """
