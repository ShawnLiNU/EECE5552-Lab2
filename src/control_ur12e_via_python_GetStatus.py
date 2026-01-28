import time
from datetime import datetime
from rtde import RTDE

# Define the robot's IP address and port
ROBOT_IP = "0.0.0.0"
RTDE_PORT = 30004

def format_values(values):
    return [f"{v:.2f}" for v in values]

def get_ur_status():
    rtde = RTDE(ROBOT_IP, RTDE_PORT)

    # Define the output recipe explicitly
    output_names = [
        "actual_q",
        "actual_qd",
        "actual_TCP_pose",
        "actual_TCP_speed"
    ]
    output_types = [
        "VECTOR6D",
        "VECTOR6D",
        "VECTOR6D",
        "VECTOR6D"
    ]

    rtde.connect()
    rtde.send_output_setup(output_names, output_types, frequency=5)
    rtde.send_start()

    try:
        while True:
            state = rtde.receive()
            if state is None:
                continue

            joint_positions = state.actual_q
            joint_speeds = state.actual_qd
            tcp_pose = state.actual_TCP_pose
            tcp_speed = state.actual_TCP_speed

            current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]

            print(f"[{current_time}] Joint Positions: {format_values(joint_positions)}", flush=True)
            print(f"[{current_time}] TCP Pose: {format_values(tcp_pose)}", flush=True)
            print(f"[{current_time}] Joint Speeds: {format_values(joint_speeds)}", flush=True)
            print(f"[{current_time}] TCP Speed: {format_values(tcp_speed)}", flush=True)
            print("-" * 50, flush=True)

            time.sleep(0.2)

    finally:
        rtde.send_pause()
        rtde.disconnect()

if __name__ == "__main__":
    get_ur_status()
