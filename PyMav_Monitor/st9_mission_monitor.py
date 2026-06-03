from pymavlink import mavutil

master=mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

while True:
    msg=master.recv_match(
        type="MISSION_CURRENT",
        blocking=True
    )

    print(
        f"Current Mission Item: "
        f"{msg.seq}"
    )