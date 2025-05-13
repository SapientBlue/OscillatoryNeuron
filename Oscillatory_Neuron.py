import numpy as np
import matplotlib.pyplot as plt

class OscillatoryNeuron:
    def __init__(self, frequency=10, amplitude=1, phase_shift=0, sampling_rate=1000, duration=1):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase_shift = phase_shift
        self.sampling_rate = sampling_rate
        self.duration = duration
        self.time = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    def generate_signal(self):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * self.time + self.phase_shift)

    def plot_signal(self):
        signal = self.generate_signal()
        plt.figure(figsize=(10, 6))
        plt.plot(self.time, signal, label="Oscillatory Signal")
        plt.title("Oscillatory Signal")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.legend()
        plt.show()
