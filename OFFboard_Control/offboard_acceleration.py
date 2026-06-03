from pymavlink import mavutil
import time

master = mavutil.mavlink_connection(
    'udp:127.0.0.1:14540'
)

master.wait_heartbeat()

print("Connected")

type_mask = (
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_X_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_Y_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_Z_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_VX_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_VY_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_VZ_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_IGNORE |
    mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE
)


def send_acceleration(ax, ay, az):

    master.mav.set_position_target_local_ned_send(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,

        type_mask,

        0,0,0,      # position

        0,0,0,      # velocity

        ax,ay,az,   # acceleration

        0,0
    )


print("Streaming acceleration setpoints")

for _ in range(50):
    send_acceleration(
        0.5, #north
        0.0,
        0.0
    )
    time.sleep(0.1)

print("arming")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1,
    0,0,0,0,0,0
)
time.sleep(2)
print("offboard")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_MODE,
    0,
    1, #arm
    6, # offboard
    0,
    0,
    0,
    0,
    0
)

while True:

    send_acceleration(
        0.5,
        0.0,
        0.0
    )

    time.sleep(0.1)


