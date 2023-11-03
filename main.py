import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt


SPEED_OF_SOUND = 343
MAX_ROOM_LENGTH = 15

fs, signal = wavfile.read('data/gen01.wav')


if signal[:,0] is not None:
    channel1 = signal[:,0]
else:
    print('Zvukový signál nebyl nalezen nebo se ho nepovedlo načíst!')
if signal[:,1] is not None:
    channel2 = signal[:,1]
else:
    print('Zvukový signál má pouze jeden kanál!')

time = np.arange(len(channel1)) / fs

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, channel1, color='b')
plt.title('Mikrofon 1')
plt.xlim([0, time[-1]])
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [dB]')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(time, channel2, color='r')
plt.title('Mikrofon 2')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [dB]')
plt.xlim([0, time[-1]])
plt.grid()

plt.tight_layout()
plt.show()

check = (np.argmax(np.fft.ifft(np.conj(np.fft.fft(channel1)) * np.fft.fft(channel2)))/fs)*SPEED_OF_SOUND
if check > MAX_ROOM_LENGTH:
    channel1 = signal[:, 1]
    channel2 = signal[:, 0]

# převod singálu na furierovy obrazy pomocí rychlé furierovi transformace
f_channel1 = np.fft.fft(channel1)
f_channel2 = np.fft.fft(channel2)

# korelace
corr = np.conj(f_channel1) * f_channel2
# nalezení indexu s maximem a zpětná furierova transformace
max = np.argmax(np.fft.ifft(corr))
delay = max / fs
dist = delay * SPEED_OF_SOUND

print(f"Časový posun: {delay:.5} s")
print(f"Vzdálenost dvou mikrofonů: {dist:.5} m")
