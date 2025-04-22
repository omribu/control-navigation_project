# control-navigation_project


## Kinematics
The kinematic model of a mobile robot assumes a rigid frame with non-deformable wheels moving on a flat surface. Two reference frames are used: a global (inertial) frame and a local frame attached to the robot. The robot’s position is defined by the coordinates (x,y) of a point 𝑃 on its chassis and the orientation angle 𝜃 between the global and local frames. The robot's state is represented by a 3×1 vector in either the global or local frame, and its orientation is described using a rotation matrix 𝑅(𝜃).

<p align="center">
  <img src="https://github.com/user-attachments/assets/96da6a00-9469-4c3f-bc65-7a9ab904bb94" alt="equation0" width="30%" />
</p>
In order for the robot to perform all its movements, it must control both motors and combine their speeds. Kinematics defines the relationship between the speeds of the two motors and the overall motion of the robot in 2D. A world reference frame is defined as a fixed coordinate system. The robot is restricted to move in a 2D plane, and its coordinate system is attached to the robot and moves with it (a body-fixed or local reference frame). Therefore, the pose of the robot can be described as the tran slation and rotation of the robot frame with respect to the fixed world frame.
ζ is defined to describe the robot state with respect to the global frame and ζR with respect to the local frame.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9508ef32-53ed-43b8-9592-edb05dc44433" alt="Robot diagram" width="30%" />
</p>
R(θ) defines the relation between frames as follows:
<p align="center">
  <img src="https://github.com/user-attachments/assets/2e24577d-72ce-47e4-9c89-5ccea20757d7" alt="Robot diagram" width="15%" />
</p>


## Differential Kinematics
The differential drive robot has two wheels, each with a diameter r=W_R=W_L. Given a point P centered between the two drive wheels, each wheel is at a distance l = W_S/2 from P . Given r, l, θ, and the spinning speed of each wheel, a forwardkinematic model for the robot’s overall speed in the global
reference frame can be described as
<p align="center">
  <img src="https://github.com/user-attachments/assets/41e8c078-8856-4782-882e-258e90cf8f6f" alt="Robot diagram" width="30%" />
</p>


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
  <img src="https://github.com/user-attachments/assets/9f6451fb-3910-4fb7-b799-c7690d11776a" alt="equation3"  width="30%"/>
</p>

We now combine Equations (1) and (2) and express them in matrix form (W_l and W_r are equal).

<p align="center">
  <img src="https://github.com/user-attachments/assets/6a589f37-f356-40a1-b39b-7729f86842cf" alt="equation5" width="20%"/>
</p>


The matrix M_S maps motor velocities to the robot's velocity, allowing us to compute the robot's motion from the wheel speeds. Since the matrix is invertible, it also enables us to determine the wheel speeds from the robot's velocity.

<p align="center">
  <img src="https://github.com/user-attachments/assets/a97efe0a-198b-4dfc-8447-9d521aa5e138" alt="equation6" width="20%"/>
</p>

The following expression defines the velocity in the world frame as a function of the robot’s velocity in its local reference frame.

<p align="center">
  <img src="https://github.com/user-attachments/assets/375709ec-fee0-4083-b3f6-327283b0cde6" alt="equation7" width="40%" />
</p>

The overall Forward differential kinematics is obtained by combining Equations (3) and (4), solved independently. 

<p align="center">
  <img src="https://github.com/user-attachments/assets/25038492-7c19-4371-83c8-5f68c6b9c20c" alt="equation8" width="40%"  />
</p>

The matrix which defines the relationship between the robot's velocity in the world frame and its local frame is the Jacobian matrix.

## Dynamics
From Newton’s second law, the linear acceleration in the robot's frame is:
<p align="center">
  <img src="https://github.com/user-attachments/assets/d6665c8c-471f-444e-a067-0f23852ac6d3" width="300" />
</p>
<img src="https://github.com/user-attachments/assets/31f23641-6e1f-4317-a72d-2d4f72c9d979" alt="equation11" width="140"/> Therfore, gives:

<p align="center">
  <img src="https://github.com/user-attachments/assets/79732bfd-6ae9-48c0-8c32-64ffe0f88551" width="300" />
</p>
Applying Euler’s rotational dynamics for torque around the center of mass:
<p align="center">
  <img src="https://github.com/user-attachments/assets/36c895dd-ba69-4dd7-ace1-7a1709679859" width="300" />
</p>
which yields:
<p align="center">
  <img src="https://github.com/user-attachments/assets/78500c53-8005-466b-96ae-c1ecffdcb084" width="300" />
</p>

From deriviation of eqation 4:
<p align="center">
  <img src="https://github.com/user-attachments/assets/9d870b31-c423-4ff9-80a6-5e3423d1320d" width="300" />
</p>


![image](https://github.com/user-attachments/assets/9d870b31-c423-4ff9-80a6-5e3423d1320d)



