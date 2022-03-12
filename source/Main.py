import cv2
import mediapipe as mp
import time

import doctest

from Controller import Controller
from Pose import Pose
from Constants import Constants


def main():
    """
    Function initializes the classes and handles the pose estimation
    """

    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    mpDraw = mp.solutions.drawing_utils

    taking_picture = False
    pic_countdown = None
    img_count = 0

    pTime = 0

    # Start Drone #
    controller = Controller()
    controller.start()
    controller.battery()
    controller.set_velocity(100)
    controller.start_height()

    pose_detection = Pose()
    const = Constants()

    while True:
        img = controller.get_stream()
        results = pose.process(img)
        h, w, _ = img.shape

        if results.pose_landmarks:
            landmarks = [lm for lm in results.pose_landmarks.landmark]
            mpDraw.draw_landmarks(img, results.pose_landmarks,
                                  mpPose.POSE_CONNECTIONS)

            right_wrist_x = int(landmarks[16].x*w)
            right_wrist_y = int(landmarks[16].y*h)

            left_wrist_x = int(landmarks[15].x*w)
            left_wrist_y = int(landmarks[15].y*h)

            right_shoulder_y = int(landmarks[12].y*h)
            left_shoulder_y = int(landmarks[11].y*h)

            # Taking pictures
            if (pose_detection.arms_crossed(right_wrist_x, left_wrist_x)
               and not taking_picture):

                taking_picture = True
                pic_countdown = time.time()

            if taking_picture:
                cv2.putText(img, "Taking Picture", (50, 350),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

                if (time.time() - pic_countdown) > const.PIC_COUNTDOWN:
                    cv2.imwrite(f"images/img{img_count}.png",
                                controller.get_stream())
                    img_count += 1
                    taking_picture = False

            # Reaction to poses
            if pose_detection.right_arm_up(right_wrist_y, right_shoulder_y,
                                           left_wrist_y, left_shoulder_y):
                controller.move_pose("right")
                cv2.putText(img, "Pose: Left", (50, 250),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            elif pose_detection.left_arm_up(right_wrist_y, right_shoulder_y,
                                            left_wrist_y, left_shoulder_y):
                controller.move_pose("left")
                cv2.putText(img, "Pose: Right", (50, 250),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            # Autonomous movement
            else:

                nose_x, nose_y = int(landmarks[0].x*w), int(landmarks[0].y*h),

                cv2.circle(img, (nose_x, nose_y), 5, (255, 0, 0), cv2.FILLED)
                cv2.arrowedLine(img, (round(w/2), round(h/2)), (round(nose_x),
                                round(nose_y)), (0, 255, 0), 3)

                arrowerd_line_length = ((abs((w/2)-nose_x)**2) +
                                        (abs((h/2)-nose_y)**2))**.5

                cv2.putText(img, f"X: {nose_x}", (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(img, f"Y: {nose_y}", (50, 150),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(img, f"Vector Length: {arrowerd_line_length}",
                            (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0), 3)
                cv2.putText(img, "Pose: None", (50, 250),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0), 3)

                distance_to_x = (nose_x) - (w/2)
                distance_to_y = (nose_y) - (h/2)

                controller.move(distance_to_x, distance_to_y)

        else:
            controller.stop()

        cv2.circle(img, (round(w/2), round(h/2)), 5, (0, 255, 0), cv2.FILLED)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 0, 0), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    doctest.testmod()
    main()
