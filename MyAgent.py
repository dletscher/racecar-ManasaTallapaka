class Agent:
    def __init__(self):
        self.low_speed = 0.2
        self.high_speed = 0.8

    def chooseAction(self, observations, possibleActions):
        velocity = observations.get('velocity', 0)
        lidar = observations.get('lidar', [10]*5)

        front = lidar[2]  # front center
        left = lidar[0]
        right = lidar[4]

        # Steering Logic
        if front < 1.0:
            steer = 'left' if left > right else 'right'
        elif left < 1.0:
            steer = 'right'
        elif right < 1.0:
            steer = 'left'
        else:
            steer = 'straight'

        # Speed logic
        if front < 1.0:
            speed = 'brake'
        elif velocity < self.high_speed:
            speed = 'accelerate'
        else:
            speed = 'coast'

        action = (steer, speed)

        # Ensure action is valid
        if action not in possibleActions:
            action = ('straight', 'accelerate')

        print(f"[Agent] Chose action: {action}, velocity: {velocity:.2f}, lidar: {lidar}")
        return action
