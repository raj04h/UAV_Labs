from pymavlink import mavutil
import math

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

while True:

    msg = master.recv_match(
        type='ATTITUDE',
        blocking=True
    )

    print(
        f"Roll={math.degrees(msg.roll):.1f} "
        f"Pitch={math.degrees(msg.pitch):.1f} "
        f"Yaw={math.degrees(msg.yaw):.1f}"
    )

