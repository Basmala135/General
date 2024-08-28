import rospy
from turtlesim.msg import Pose
from std_msgs.msg import Bool
from pynput import keyboard

class GameEngine:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('game_engine', anonymous=True)
        
        # Game state variables
        self.turtle1_health = 100
        self.turtle2_health = 100
        self.turtle1_attacks_remaining = 10
        self.turtle2_attacks_remaining = 10
        self.attack_range = 4  # range of attack for example
        
        # Initialize positions
        self.turtle1_pos = (5.4, 5.4)  # Default value for turtle1 position
        self.turtle2_pos = (2, 7)  # Default value for turtle2 position

        # Initialize attacks
        self.turtle1_attack = False
        self.turtle2_attack = False


        # Subscribers
        self.turtle1_sub = rospy.Subscriber('/turtle1/pose', Pose, self.turtle1_pose_callback)
        self.turtle2_sub = rospy.Subscriber('/turtle2/pose', Pose, self.turtle2_pose_callback)
        self.turtle1_attack_sub = rospy.Subscriber('/turtle1/attack', Bool, self.turtle1_attack_callback)
        self.turtle2_attack_sub = rospy.Subscriber('/turtle2/attack', Bool, self.turtle2_attack_callback)

        # Main loop
        self.main_loop()

    def turtle1_pose_callback(self, msg: Pose):
        self.turtle1_pos = (msg.x, msg.y)
    
    def turtle2_pose_callback(self, msg: Pose):
        self.turtle2_pos = (msg.x, msg.y)
    
    def turtle1_attack_callback(self, msg: Bool):
        self.turtle1_attack = msg.data
    
    def turtle2_attack_callback(self, msg: Bool):
        self.turtle2_attack = msg.data

    def attack(self, attacker_pos, enemy_pos):
        rospy.sleep(1)
        if attacker_pos and enemy_pos:
            x_attack, y_attack = attacker_pos
            x_enemy, y_enemy = enemy_pos
            
            # Check if the enemy is within the attack range
            if abs(x_enemy - x_attack) <= self.attack_range and abs(y_enemy - y_attack) <= self.attack_range:
                return True
        return False

    def main_loop(self):
        while not rospy.is_shutdown():
            flag=True   #represents if attack is pressed
            if self.turtle1_attack:
                self.turtle1_attacks_remaining-=1
                if self.turtle1_attacks_remaining==0:
                    rospy.loginfo(" turtle 2 wins!!")
                    rospy.signal_shutdown("turtle 2 wins!!")
                    break
                if self.attack(self.turtle1_pos, self.turtle2_pos):
                    self.turtle2_health -= 50
                    rospy.loginfo(f"Turtle2 hit by Turtle1! Turtle2's health is now {self.turtle2_health}")
                    if self.turtle2_health<=0:
                        rospy.loginfo(" turtle 1 wins!!")
                        rospy.signal_shutdown("turtle 1 wins!!")
                        break
            elif self.turtle2_attack:
                self.turtle2_attacks_remaining-=1
                if self.turtle2_attacks_remaining==0:
                    rospy.loginfo(" turtle 1 wins!!")
                    rospy.signal_shutdown("turtle 1 wins!!")
                    break
    
                if self.attack(self.turtle2_pos, self.turtle1_pos):
                    self.turtle1_health -= 50
                    rospy.loginfo(f"Turtle1 hit by Turtle2! Turtle1's health is now {self.turtle1_health}")
                    if self.turtle1_health<=0:
                        rospy.loginfo(" turtle 2 wins!!")
                        rospy.signal_shutdown("turtle 2 wins!!")
                        break

              

if __name__ == '__main__':
    try:
        game_engine = GameEngine()
        rospy.spin()  # Keep the node running
    except rospy.ROSInterruptException:
        pass
