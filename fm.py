import numpy as np
import matplotlib.pyplot as plt


Ac = float(input("Enter carrier amplitude (Ac): "))
Fc = float(input("Enter carrier frequency (Fc in Hz): "))
Am = float(input("Enter message amplitude (Am): "))
Fm = float(input("Enter message frequency (fm in Hz): "))
beta = float(input("Enter FM modulation index (beta): "))

t = np.linspace(0, 1, 1000)

message = Am * np.cos(2 * np.pi * Fm * t)

carrier = Ac * np.cos(2 * np.pi * Fc * t)

FM_signal = Ac * np.cos(2 * np.pi * Fc * t + beta * np.sin(2 * np.pi * Fm * t))

plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title("Message Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, FM_signal)
plt.title("Frequency Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()