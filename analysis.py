"""
Team Members:
Swapnil Agarwal - 2017B3A71343H
Thribhuvan Reddy M - 2017B3A71116H
Arundhan Reddy M - 2017B3A70889H
Uttam Singh - 2017B4A70683H
Srinivas Konduri - 2017B3A70746H
"""


#!/usr/bin/env python

import matplotlib.pyplot as plt

print("Using file size: 1.0 MB")

# Delay vs Time taken
delay   = [0, 1, 2, 3, 4, 5] 
time    = [7.788
, 8.064
, 8.443
, 8.729
, 9.425
, 9.579
]
plt.title("Delay vs Time")
plt.ylabel("Time taken (in sec)")
plt.xlabel("Delay (in sec)")
plt.plot(delay,time)
# plt.legend()
# plt.grid(True)
plt.show()

# Delay vs Throughput

delay       = [0, 1, 2, 3, 4, 5]
throughput  = [134.64731
, 130.02882
, 124.19394
, 120.13140
, 111.25959
, 109.47165
]
plt.title("Delay vs Throughput")
plt.ylabel("Throughput (KB/s)")
plt.xlabel("Delay (in sec)")
plt.plot(delay,throughput)
plt.show()

### Loss % vs Time taken

loss = [0, 10, 30, 50, 70, 90]
time = [5.693
, 6.225
, 6.504
, 9.447
, 10.228
, 10.562
]
plt.title("Loss % vs Time")
plt.ylabel("Time taken (in sec)")
plt.xlabel("Loss %")
plt.plot(loss,time)
plt.show()

# Loss % vs Throughput

loss = [0, 10, 30, 50, 70, 90]
throughput = [184.19021
, 168.43255
, 161.21205
, 110.99779
, 102.52251
, 99.28025
]
plt.title("Loss % vs Throughput")
plt.ylabel("Throughput (KB/s)")
plt.xlabel("Loss %")
plt.plot(loss, throughput)
plt.show()

### Corruption % vs Time taken

corrupt = [0, 10, 30, 50, 70, 90]
time = [7.628
, 7.759
, 7.994
, 8.345
, 8.491
, 8.633
]
plt.title("Corrupt % vs Time")
plt.ylabel("time (in sec)")
plt.xlabel("Corrupt %")
plt.plot(corrupt, time)
plt.show()

### Corruption % vs Throughput

corrupt = [0, 10, 30, 50, 70, 90]
throughput = [137.4700754
, 135.1390306
, 131.1635132
, 125.6536345
, 123.4991354
, 121.4634218
]
plt.title("Corrupt % vs Throughput")
plt.ylabel("Throughput (KB/s)")
plt.xlabel("Corrupt %")
plt.plot(corrupt, throughput)
plt.show()

### Packet Reorder vs Time taken
reorder = [0, 10, 30, 50, 70, 90]
time = [5.337
, 5.738
, 5.356
, 5.283
, 6.164
, 5.946
]

plt.title("Reorder(in 1000ms delay) % vs Time")
plt.ylabel("Time taken (in sec)")
plt.xlabel("Reorder %")
plt.plot(reorder, time)
plt.show()

### Packet Reorder vs Throughput
reorder = [0, 10, 30, 50, 70, 90]
throughput = [2.196475989
, 0.1827553843
, 0.1957714886
, 0.1984698078
, 0.1701231209
, 0.1763411377
]
plt.title("Reorder(in 1000ms delay) % vs Throughput")
plt.ylabel("Throughput (in KB/s)")
plt.xlabel("Reorder %")
plt.plot(reorder, throughput)
plt.show()


# Jitter vs Time taken
jitter   = [0, 1, 2, 3, 4, 5]
time    = [6.87
, 7.15
, 7.25
, 7.59
, 7.92
, 8.88
]
plt.title("Jitter vs Time")
plt.ylabel("Time taken (in sec)")
plt.xlabel("jitter (in sec)")
#plt.ylim(0, 4)
plt.plot(jitter,time)
plt.show()

# Jitter vs Throughput
jitter       = [0, 1, 2, 3, 4, 5]
throughput  = [152.59265
, 146.59813
, 144.55593
, 138.12889
, 132.33249
, 118.03034
]
plt.title("Jitter vs Throughput")
plt.ylabel("Throughput (KB/s)")
plt.xlabel("Jitter (in sec)")
#plt.ylim(0, 18)
plt.plot(jitter,throughput)
plt.show()