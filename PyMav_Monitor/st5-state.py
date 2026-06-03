from pymavlink import mavutil

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

while True:

    msg = master.recv_match(
        type='HEARTBEAT',
        blocking=True
    )

    armed = bool(
        msg.base_mode &
        mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED
    )

    print("ARMED" if armed else "DISARMED")