from roboclaw_3 import Roboclaw
import time

# --- CONFIGURACIÓN ---
# En Raspberry Pi 3/4/5, el serial suele ser /dev/ttyS0 o /dev/ttyAMA0
puerto_serial = "/dev/ttyS0" 
baudrate = 38400  # Debe coincidir con la configuración de tu RoboClaw (por defecto es 38400)
address = 0x80    # Dirección por defecto del RoboClaw (128)

# Inicializar el objeto RoboClaw
rc = Roboclaw(puerto_serial, baudrate)
rc.Open()

print("Intentando conectar con RoboClaw...")

# --- MOVIMIENTO ---
try:
    # 1. MOVER ADELANTE
    # El valor va de 0 a 127. (64 es media velocidad, 127 es máxima)
    print("Motor 1: Adelante (Velocidad 64/127)")
    rc.ForwardM1(address, 64) 
    
    time.sleep(4) # Esperar 4 segundos

    # 2. PARAR
    print("Parando...")
    rc.ForwardM1(address, 0) # 0 significa detenido

except Exception as e:
    print(f"Error: {e}")