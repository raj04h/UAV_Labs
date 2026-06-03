from pymavlink import mavutil

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

print("Sending DISARM command")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0,  # disarm
    0, 0, 0, 0, 0, 0
)

print("DISARM command sent")