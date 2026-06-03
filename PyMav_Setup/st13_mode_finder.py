from pymavlink import mavutil

m = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

m.wait_heartbeat()

print(m.mode_mapping())   