from pymavlink import mavutil
import time

# Connect to PX4
master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

print("Waiting for heartbeat...")
master.wait_heartbeat()

print(
    f"Connected to System {master.target_system}, "
    f"Component {master.target_component}"
)

# Position-only control
type_mask = (
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_VX_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_VY_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_VZ_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_AX_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_AY_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_AZ_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE
)


def send_setpoint(x, y, z):
    master.mav.set_position_target_local_ned_send(
        0,                                  # time_boot_ms
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        type_mask,
        x, y, z,                            # position
        0, 0, 0,                            # velocity
        0, 0, 0,                            # acceleration
        0,                                  # yaw
        0                                   # yaw rate
    )



print("Streaming setpoints for 5 seconds...")

for i in range(50):
    send_setpoint(
        5.0,    # North
        0.0,    # East
        -3.0    # Up 3m (NED)
    )
    time.sleep(0.1)

print("Setpoint stream started")


print("Arming...")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1,      # ARM
    0,
    0,
    0,
    0,
    0,
    0
)

arm_ack = master.recv_match(
    type='COMMAND_ACK',
    blocking=True,
    timeout=5
)

print("ARM ACK:")
print(arm_ack)

time.sleep(2)


print("Requesting OFFBOARD mode...")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_MODE,
    0,
    1,      # MAV_MODE_FLAG_CUSTOM_MODE_ENABLED
    6,      # PX4 OFFBOARD custom mode (test)
    0,
    0,
    0,
    0,
    0
)

offboard_ack = master.recv_match(
    type='COMMAND_ACK',
    blocking=True,
    timeout=5
)

print("OFFBOARD ACK:")
print(offboard_ack)


print("Keeping Offboard stream alive...")

counter = 0

while True:

    send_setpoint(
        5.0,
        0.0,
        -3.0
    )

    counter += 1

    if counter % 10 == 0:
        print("Streaming setpoints...")

    time.sleep(0.1)