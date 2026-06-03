from pymavlink import mavutil

m = mavutil.mavlink_connection('udp:127.0.0.1:14540')
m.wait_heartbeat()

hb = m.recv_match(type='HEARTBEAT', blocking=True)

print("Autopilot:", hb.autopilot)
print("Vehicle Type:", hb.type)