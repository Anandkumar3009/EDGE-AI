import socket
import csv
import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import collections
from datetime import datetime
# matplotlib.use("TkAgg")

# -----------------------------
# CONFIG
# -----------------------------
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
DATA_DIR = "imu_data"
# -----------------------------
 
activity = input("Enter activity label (e.g., walk, sit, stand): ")
 
os.makedirs(DATA_DIR, exist_ok=True)
filename = f"{activity}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
filepath = os.path.join(DATA_DIR, filename)
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(False)
 
print(f"Listening on UDP port {UDP_PORT}")
print(f"Saving to {filepath}")
 
window_size = 10
# Data Buffers
ax_d = collections.deque([0]*window_size, maxlen=window_size)
ay_d = collections.deque([0]*window_size, maxlen=window_size)
az_d = collections.deque([0]*window_size, maxlen=window_size)
gx_d = collections.deque([0]*window_size, maxlen=window_size)
gy_d = collections.deque([0]*window_size, maxlen=window_size)
gz_d = collections.deque([0]*window_size, maxlen=window_size)

# Setup Figure with 2 Subplots
fig, (ax_plot, gyro_plot) = plt.subplots(2, 1, figsize=(8, 6))
# plt.subplots_adjust(hspace=0.4)
x = list(range(window_size))

# Accelerometer Lines
line_ax, = ax_plot.plot(x, ax_d, label='Ax', color='r')
line_ay, = ax_plot.plot(x, ay_d, label='Ay', color='g')
line_az, = ax_plot.plot(x, az_d, label='Az', color='b')
ax_plot.set_ylim(-3, 3) 
ax_plot.set_title("Accelerometer (Linear Motion)")
ax_plot.set_ylabel("G-Force")
ax_plot.legend(loc='upper right')

# # Gyroscope Lines
line_gx, = gyro_plot.plot(x, gx_d, label='Gx', color='c')
line_gy, = gyro_plot.plot(x, gy_d, label='Gy', color='m')
line_gz, = gyro_plot.plot(x, gz_d, label='Gz', color='y')
gyro_plot.set_ylim(-500, 500) 
gyro_plot.set_title("Gyroscope (Rotation)")
gyro_plot.set_ylabel("Degrees/sec")
gyro_plot.legend(loc='upper right')

f = open(filepath, "w", newline="")
writer = csv.writer(f)
writer.writerow(["timestamp", "ax", "ay", "az", "gx", "gy", "gz"])

def update(frame):
    try:
        while True:
            data, _ = sock.recvfrom(1024)
            decoded = data.decode().strip()
            row = decoded.split(",")
            # row.append(activity)
            # print(row)
            
            # Update Buffers
            if len(row) == 7:
                writer.writerow(row)
                vals = [float(i) for i in row]
                ax_d.append(vals[1]); ay_d.append(vals[2]); az_d.append(vals[3])
                gx_d.append(vals[4]); gy_d.append(vals[5]); gz_d.append(vals[6])
                
    except BlockingIOError:
        pass
        # print("\nStopped. File saved.")
    
    # Update Plot Lines
    line_ax.set_ydata(ax_d); line_ay.set_ydata(ay_d); line_az.set_ydata(az_d)
    line_gx.set_ydata(gx_d); line_gy.set_ydata(gy_d); line_gz.set_ydata(gz_d)    
    return line_ax, line_ay, line_az, line_gx, line_gy, line_gz

ani = FuncAnimation(fig, update, interval = 20, blit = True, cache_frame_data=False)

try:
    # print('finish')
    plt.tight_layout()
    plt.show()
finally:
    print('\n closing the csv and socket.')
    f.close()
    sock.close()
    print("data collection stopped.")