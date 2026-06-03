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

    mode = mavutil.mode_string_v10(msg)

    print("Mode:", mode)

