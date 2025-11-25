# Archivo: ~/ros2_ws/src/prueba/prueba/mi_nodo.py

import rclpy
from rclpy.node import Node

class HolaMundoNode(Node):
    def __init__(self):
        super().__init__('nodo_hola_mundo')
        # Esta es la forma correcta de imprimir en ROS 2
        self.get_logger().info('¡Hola Mundo! Estás usando ROS 2.')

def main(args=None):
    rclpy.init(args=args)
    node = HolaMundoNode()
    
    # Mantiene el nodo vivo (aunque aquí solo imprime una vez)
    rclpy.spin(node) 
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()