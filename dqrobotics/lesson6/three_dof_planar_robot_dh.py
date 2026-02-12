from dqrobotics.robot_modeling import DQ_SerialManipulatorDH
import numpy as np

class ThreeDofPlanarRobotDH:
    """
    ThreeDofPlanarRobot regarding all methods related to the 3-DoF planar robot.
    """
    
    def kinematics():
        """
        Returns the kinematics of the ThreeDoFPlanarRobot as DQ_SerialManipulatorDH.
        """
        DH_theta=  [0., 0., 0.]
        DH_d =     [0., 0., 0.]
        DH_a =     [1., 1., 1.]
        DH_alpha = [0., 0., 0.]
        DH_type  = [0,  0,  0]
        
        dh_matrix = np.array([
            DH_theta,
            DH_d,
            DH_a,
            DH_alpha,
            DH_type
        ])
        
        return DQ_SerialManipulatorDH(dh_matrix)
    