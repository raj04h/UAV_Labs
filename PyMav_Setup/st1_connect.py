from pymavlink import mavutil

print("Connecting to PX4...")

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

print("Waiting for heartbeat...")

master.wait_heartbeat()

print(
    f"Connected! System={master.target_system}, "
    f"Component={master.target_component}"
)
