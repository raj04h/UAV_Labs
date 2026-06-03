from pymavlink import mavutil

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

print("Connected")

while True:

    msg = master.recv_match(
        type='GLOBAL_POSITION_INT',
        blocking=True
    )

    print(
        f"Lat: {msg.lat / 1e7:.6f}, "
        f"Lon: {msg.lon / 1e7:.6f}, "
        f"Alt: {msg.relative_alt / 1000:.2f} m"
    )

