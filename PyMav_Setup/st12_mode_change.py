from pymavlink import mavutil

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

mode = 'AUTO.LOITER'

mode_id = master.mode_mapping().get(mode)

print("Mode ID:", mode_id)

master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    mode_id
)