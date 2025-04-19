# control-navigation_project

## Kinematics
In order for the robot to perform all its movements, it must control both motors and combine their speeds. Kinematics defines the relationship between the speeds of the two motors and the overall motion of the robot in 2D. A world reference frame is defined as a fixed coordinate system. The robot is restricted to move in a 2D plane, and its coordinate system is attached to the robot and moves with it (a body-fixed or local reference frame). Therefore, the pose of the robot can be described as the tran slation and rotation of the robot frame with respect to the fixed world frame.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0a2b919-d5b9-4451-badb-ad53ede80cff" alt="Robot diagram" />
</p>

This is the homogeneous representation of the coordinate transformation between the fixed world frame and the robot's reference frame. Tx and Ty is the pose of the robot in the fixed world frame, and theta is the orientation of the robot relative to the fixed world frame.

## Differential Kinematics
### Linear and Angular Velocity
The **linear velocity** is calculated as follows:

<p align="center">
  <img src="https://github.com/user-attachments/assets/226e56d0-9293-4b05-aec5-727fdec692d2" alt="Velocity equation" width="30%" />
  <img src="https://github.com/user-attachments/assets/271a0a82-28c8-48de-8899-117c11d27fe3" alt="Second equation" width="30%" />
</p>

The linear velocity is calculated as follows:
<p align="center">
  <img src="https://github.com/user-attachments/assets/992f897c-cfc1-4bc7-bff7-e6fe26434f45" alt="equation1" />
</p>

 By adding the two expressions for V_C, we get:
 
 <p align="center">
  <img src="https://github.com/user-attachments/assets/6954fdb1-fb3c-41b0-ad4a-3b5a5d935ecb" alt="equation2" />
</p>

Where R_{C/A} and R_{C/B} are in opposite directions and equal in magnitude, thus cancel each other out.
Finally, substituting V_A and V_B into the equation, the linear velocity of the robot becomes:

<p align="center">
  <img src="https://github.com/user-attachments/assets/2e394267-dbe6-4835-ac3f-73587b185f8a" alt="equation1"/>
</p>

The **angular velocity** is calculated by subtracting the two V_C equations:

<p align="center">
  <img src="https://github.com/user-attachments/assets/f34925b1-c342-4c70-bfa2-553fb42b8976" alt="equation3" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/ade9dddf-991e-4bac-97e0-0a999baf0dc3" alt="equation4" />
</p>

We now combine Equations (1) and (2) and express them in matrix form (W_l and W_r are equal).

<p align="center">
  <img src="https://github.com/user-attachments/assets/ef90aa2c-f2fc-481b-ac57-36359a6cf13b" alt="equation5" />
</p>

The matrix M_S maps motor velocities to the robot's velocity, allowing us to compute the robot's motion from the wheel speeds. Since the matrix is invertible, it also enables us to determine the wheel speeds from the robot's velocity.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a97efe0a-198b-4dfc-8447-9d521aa5e138" alt="equation6" />
</p>

The following expression defines the velocity in the world frame as a function of the robot’s velocity in its local reference frame.

<p align="center">
  <img src="https://github.com/user-attachments/assets/375709ec-fee0-4083-b3f6-327283b0cde6" alt="equation7" />
</p>

The overall Forward differential kinematics is obtained by combining Equations (3) and (4), solved independently. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/9db389a6-e4e7-42ae-9b38-5fdabd0ca6f0" alt="equation8" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/a652ee2c-21da-463c-89f4-431d7e1144c9" alt="equation9" />
</p>
The matrix which defines the relationship between the robot's velocity in the world frame and its local frame is the Jacobian matrix.

## Dynamics
Applying Newton's second law for linear motion:
<p align="center">
  <img src="https://github.com/user-attachments/assets/d6665c8c-471f-444e-a067-0f23852ac6d3" alt="equation10" />
</p>
<p >
  <img src="https://github.com/user-attachments/assets/31f23641-6e1f-4317-a72d-2d4f72c9d979" alt="equation10" />
</p>


