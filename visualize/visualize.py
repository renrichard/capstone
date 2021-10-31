from librosa.core import load, resample
import matplotlib.pyplot as plt

from preprocess.json.vcc_2020_constants import vcc_2020_orig_sr, vcc_2020_target_sr


def visualize_waves(filenames, sample_rates):
	for i in range(len(filenames)):
		data, _ = load(filenames[i], sample_rates[i])
		plt.plot(data)
	plt.show()


if __name__ == '__main__':
	visualize_waves(['/Users/richardren/data/VCC2020-database/extract/target_task1/TEF1/E20021.wav',
	                 '/Users/richardren/data/VCC2020-database/extract/target_task1/TEF1/resample/E20021.wav'],
	                [vcc_2020_orig_sr, vcc_2020_target_sr])
