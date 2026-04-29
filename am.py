import numpy as np
import matplotlib.pyplot as plt


Ac = float(input("Enter Carrier Amplitude (Ac): "))
fc = float(input("Enter Carrier Frequency (fc in Hz): "))
Am = float(input("Enter Message Amplitude (Am): "))
fm = float(input("Enter Message Frequency (fm in Hz): "))
mu = float(input("Enter Modulation Index (μ): "))

t = np.linspace(0, 5 / fm, 5000)


message = Am * np.cos(2 * np.pi * fm * t)


carrier = Ac * np.cos(2 * np.pi * fc * t)


am_signal = Ac * (1 + mu * np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * fc * t)


plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.title("Message Signal")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.title("Amplitude Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()