from pymavlink import mavutil

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

print("Connected")

# Arm first
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1,
    0,0,0,0,0,0
)

ack = master.recv_match(
    type='COMMAND_ACK',
    blocking=True
)

print("ARM ACK:", ack.result)

# Start Mission
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_MISSION_START,
    0,
    0, 0, 0, 0, 0, 0, 0
)

ack = master.recv_match(
    type='COMMAND_ACK',
    blocking=True
)

print("MISSION ACK:", ack.result)