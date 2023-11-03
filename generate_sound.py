import numpy as np
from scipy.io import wavfile

OUTPUT_FILENAME = 'data/gen01.wav'
sample_rate = 200
duration = 3
amplitude = 0.5
signal = np.random.uniform(-amplitude, amplitude, int(sample_rate * duration))
left_channel = signal
right_channel = signal

silence = np.zeros(int(0.1 * sample_rate))

channel1 = np.hstack((silence, left_channel, silence))
channel2 = np.hstack((right_channel, silence, silence))

stereo_signal = np.column_stack((channel1, channel2))

wavfile.write(OUTPUT_FILENAME, sample_rate, stereo_signal)

print(f"Uloženo do: data/{OUTPUT_FILENAME}")
