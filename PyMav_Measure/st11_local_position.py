from pymavlink import mavutil

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

while True:

    msg = master.recv_match(
        type='LOCAL_POSITION_NED',
        blocking=True
    )

    print(
        f"x={msg.x:.2f} "
        f"y={msg.y:.2f} "
        f"z={msg.z:.2f}"
    )