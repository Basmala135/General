import rospy
from geometry_msgs.msg import Twist, Point
from std_msgs.msg import Header
from turtle_battle.msg import AttackCommand, GameState
  

class GameEngine:
    def __init__(self):
        # Initialize ROS node
        rospy.init_node('game_engine', anonymous= True)   #true 3shan law 3amlna node tania b nfs el asm wla haga mydrbsh mnna  
        
        # Game state variables
        self.turtle1_health = 100
        self.turtle2_health = 100
        self.turtle1_attacks_remaining = 10
        self.turtle2_attacks_remaining = 10
        
        # Subscribers for turtle commands
        rospy.Subscriber('/turtle1/attack_cmd', AttackCommand, self.handle_turtle1_attack)
        rospy.Subscriber('/turtle2/attack_cmd', AttackCommand, self.handle_turtle2_attack)
        
        # Publisher for game state
        self.game_state_pub = rospy.Publisher('/game_state', GameState, queue_size=10)   #topic name: game state publishing: GameState created message  
        
        # Main loop
        self.run_game()

    def handle_turtle1_attack(self, msg):
        # hnkb hena code attack turtle 1
        pass

    def handle_turtle2_attack(self, msg):
        # hena turtle 2 
        pass

    #hyt3mal hena bardo def l ba2eet el functions el health w kda 

    def run_game(self):
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            # Update game state and publish hyfdal y3mel pub. lel kalam da 
            game_state_msg = GameState(
                turtle1_health=self.turtle1_health,
                turtle2_health=self.turtle2_health,
                turtle1_attacks_remaining=self.turtle1_attacks_remaining,
                turtle2_attacks_remaining=self.turtle2_attacks_remaining
            )
            self.game_state_pub.publish(game_state_msg)
            
            rate.sleep()

if __name__ == '__main__':
    try:
        engine = GameEngine()
    except rospy.ROSInterruptException:
        pass
