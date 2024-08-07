# Concepts:
### Kinematics
**Motion in one dimension**
- Position
- displacement
- average velocity
- instantaneous velocity and speed
	- position-vs-time graph
	- velocity-vs-time graph
- average and instantaneous acceleration
- Motion with constant acceleration
	- $x = x_0 + vt$
	- $v = v_0 + at$
	- (from constant acceleration integral) $x = x_0 + v_0t + \frac{1}{2} at^2$
- free fall (for human-sized objects near earth a = g = 9.81 m/s^2)

**Motion in 2D and 3D**
- Position as a vector
- Displacement as a vector
- Velocity as a vector
	- Independence of perpendicular motion
- Acceleration vector
- Projectile motion
- Uniform circular motion
- Relative motion

# Script
## Motion in one dimension

> Projectile motion, two-object pursuit, gravity, circular motion and a lot more are described by kinematics, which is basically the math of how things move.

> we'll start with an object that can only move in two directions: forwards and backwards. Now to keep track of it's position we'll call this the x-axis, and then its position is just a number, which corresponds to the x-axis value of its location.
> Specifically, we'll say that its position is at the center of mass, which is basically the point where the object would balance if you were to hold it just there.

> Now what happens if I take this object and I move it to the right? Well we can say that it moved some number of units to the right. To be more precise, we can measure its final x-position and its original x-position, and subtract the two. Doing so gives us the object's displacement, which is basically a direction that it has moved in.

> But to really talk about how things move we also have to introduce time into the equation. The faster something is going, the less time it takes for a certain amount of displacement to occur; so we divide the displacement by the change in time, and this gives us **velocity**. So if we move 5 meters to the right in 2 seconds then our velocity is 2.5 meters per second to the right.

> If we want the exact velocity at some single instance in time, then we just need to take the limit as our timestep gets infinitesimally small. In other words, take the derivative of position with respect to time.

> Now since velocity is the ratio of two changes, we can also show it as a slope. The vertical axis represents the object's position, and the horizontal axis represents time. So over time, we can see the object's position, and the slope of this graph will tell us the object's velocity at that point.

> Now if we want to fully describe the motion of objects, then we'll need one more quantity: acceleration. Acceleration is like the velocity of velocity. Basically, it's just the change in velocity over change in time. So if you go from a low velocity to a high velocity in a short amount of time, then you have a high acceleration. To get the instantaneous acceleration, just take the limit as our timestep approaches zero. And just like the position vs time graph, we can find the acceleration from the slope of the velocity vs. time graph.

> Now it's time to put some equations to this.
> So we know that the average velocity is the change in position over the change in time, which is the same as the current position minus the initial position over the final time minus the initial time. It doesn't matter what we decide to let our initial time be: zero, two, five hundred; as long as we're consistent, the change in time will be the same. Because of this, we'll let our initial time be equal to zero, so it drops out of the equation. 

> Now we can multiply across the final time, and add across the initial position, and we get that the final position is equal to the initial position plus the average velocity times the change in time.

> Since position and velocity have the exact same relationship as velocity and acceleration, the same equation is also true for velocity and acceleration.

> But what if we have both acceleration and velocity?
> Remember that the slope of position is velocity and that for velocity is acceleration. This also means that we can get velocity from acceleration times a change in time, or position from velocity times a change in time.

> If we assume constant acceleration, a, then our velocity is just the acceleration times some change in time, plus a constant C. plugging in t=0 shows us that the constant C is actually just the initial velocity.

> We can also go from velocity to position the same way. And once again, the extra constant is just our initial velocity.

> Now we have a parabola describing an object with position, velocity, and constant acceleration.
> Now it turns out that for human-sized objects near the surface of the earth, gravity acts with nearly constant acceleration (-9.81 m/s^2). If we plug this into our equation we can model the height of an object over time.

> An apple is dropped from a height of 100 m off the ground with no initial velocity. Ignore air resistance. How long does it take for the apple to land? We'll say the apple starts moving at t=0. We're given the initial velocity, and the initial position, and we know gravity. Since we want to know when the apple hits the *ground*, we'll set the y-position equal to zero: the height of the ground. Now we only have one unknown in this equation -- the time. Solving for time gives us this. And now if we plug in the known quantities, we get 4.52 seconds. We know our time will be in seconds, not minutes or hours or something, because our acceleration is given in terms of seconds.

> Likewise, if we have two objects with their own initial positions, velocities, and accelerations. We can model their position over time. If we want to know when an object in pursuit will reach another one, we just set these equations equal to each other and solve for time. So when the two position curves cross, they're at the same x-position at the same time.


## Motion in 2D and 3D
> But what about objects that move in more than one direction? In that case, we're going to need more dimensions to model their motion.

> Let's start with position. For two-dimensional motion, we'll need two axes, and two numbers to represent the object's position: the x-position and the y-position. To make things easier, we bundle these two into the object's **position vector** pointing from the origin to the object's position. Notice that this is just a different way of writing the same information: we still have the x-position and the y-position of the object available.

> Now the reason this is useful is because now when we want to get the displacement we just have to subtract the final position vector from the original position vector. The way we do that is basically just by subtracting each component of the vector, like this.

> And now for the velocity. Again all we have to do is divide the displacement by the change in time, which, as you might expect, basically just involves dividing each component by the change in time.

> And for acceleration it's the same thing, just, divide the velocity by the change in time.

> If you need the instantaneous velocity or acceleration, you can take the limit as the change in time becomes infinitesimally small.

> Now here's something interesting:
> The x-component and y-component of velocity and acceleration are completely independent of each other.
> If you were to drop a bullet from your hand or fire it out of a gun, it would take the same amount of time to reach the floor (ignoring air resistance) because the only difference between these two scenarios is the x-component of the velocity, not the y-component. In fact, the mythbusters have a video on this exact topic.

> Now that makes life easier for us because it means we can solve for the x-components and y-components separately.

### Cannon example
> So let's take the example of firing a cannon. In this case we're given the angle of the cannon, which we'll call theta, and the initial firing velocity.

> Starting with the x-component because it's a bit easier to calculate, we know that the cosine of the angle theta is equal to the ratio of the horizontal component of the velocity -- the adjacent -- and the total velocity. So multiplying this by the launch velocity will give us the x-component of our initial velocity. We're assuming no air resistance and no wind or something like that, which means no acceleration in the x-direction. Also, we'll go ahead and say that the muzzle of the cannon is the origin, so our initial x-position is zero. So that's it, the x-position of the cannonball just looks like this. 

> Now for the y-component we have to deal with the acceleration of gravity.
> The sine of the launch angle is equal to the ratio of the vertical component of the velocity to the total velocity; so once again multiplying this by launch velocity gives us the y-component. The initial y-position is zero since we're starting at the origin. And our acceleration from gravity is downward, in the negative y-direction, so we can plug it in there.

> Now with these two equations, we could, for example, figure out how far away the cannonball lands. First, we use the y equation to solve for the time when the cannonball hits the ground; and then we plug that into the x equation, so we know the x-position when the cannonball hits the ground.

### Circular motion
> But what if our motion is constrained to a circle?
> Instead of defining velocity with a velocity vector, we can define it based on how the angle of our position is changing over time. Our angular velocity, omega, is equal to the change in angle over change in time, or our angle is equal to omega times t for uniform motion.

> If we're using the radians angle system, then the angle theta is defined as the ratio of the arc length to the radius. When the object is moving in a circle, the radius isn't changing, but the arc length is changing by the velocity of the outside object. In other words, the angular velocity is equal to the linear velocity divided by the radius.

> With these two ideas in mind we can define the position vector as the radius times either the sine or the cosine of the object angle, which we know is equal to the angular velocity times the change in time. Notice that the magnitude of this vector is just the radius.

> Now we can get our velocity vector from the derivative of position, which looks like this. Now the magnitude is r times omega, which if we rewrite, we can see is the same as the linear velocity, as expected.

> Now lastly we can get the acceleration from the derivative of velocity. Look what happens if we pull out the negative omega squared: the acceleration is a negative multiple of the position vector. This means that it will always point in the opposite direction as the position vector, from the outside of the circle in.

> Also, its magnitude is equal to omega squared r, which after some rewriting looks like this. This is the equation for centripetal acceleration.

### Reference frames
> Lastly we have to talk about reference frames
> So far, we've just been kind of taking the velocity as an absolute thing. But it's not, it depends on who is observing it.

> For example, let's say you're on an airplane going 900 kilometers per hour, relative to the earth. From someone standing on the ground, the airplane is going at 900 kilometers per hour. *But*, relative to *you*, the airplane isn't moving at all. Instead, the earth is moving behind you at 900 kilometers per hour.

> Neither of these perspectives are more true than the other. It all just depends on where you're measuring from.

> If you're in a car going 100 kilometers per hour in the direction opposite the airplane, as measured from someone standing on the earth, then relative to you, the airplane is going at 1000 kilometers per hour, and the earth is going by at 100 kilometers per hour.

> But actually the earth is going around the sun at like 30 kilometers per second.

> But wait, the solar system is going around the center of the galaxy at like 200 kilometers per second.

> So which perspective is correct?
> ***none of them.***

(more physics)
