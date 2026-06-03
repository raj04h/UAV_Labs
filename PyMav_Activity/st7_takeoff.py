from pymavlink import mavutil
import time

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

print("Connected")

# Arm & wait
master.arducopter_arm()
master.motors_armed_wait()

print("Vehicle Armed")

time.sleep(2)

print("Sending Takeoff Command")


# takeoff
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0, 0, 0, 0,
    0, 0,
    10 # height
)

ack = master.recv_match(
    type='COMMAND_ACK',
    blocking=True,
    timeout=5
)

print("ACK:", ack)