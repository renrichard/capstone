from librosa.core import load, resample
import matplotlib.pyplot as plt

from preprocess.json.vcc_2020_constants import vcc_2020_orig_sr, vcc_2020_target_sr


def visualize_waves(filenames, sample_rates, alphas, labels, title):
	for i in range(len(filenames)):
		data, _ = load(filenames[i], sample_rates[i])
		plt.plot(data, alpha=alphas[i], label=labels[i])

	plt.title(title)
	plt.legend()
	plt.show()


if __name__ == '__main__':
	# visualize_waves(['/Users/richardren/data/VCC2020-database/extract/target_task1/TEF1/E20021.wav',
	#                  '/Users/richardren/data/VCC2020-database/extract/target_task1/TEF1/resample/E20021.wav'],
	#                 [vcc_2020_orig_sr, vcc_2020_target_sr])

	visualize_waves(['/Users/richardren/Downloads/FP_TEF2_1k.wav', '/Users/richardren/Downloads/FP_TEM1_1k.wav'],
	                [vcc_2020_target_sr, vcc_2020_target_sr],
	                [0.5,0.5],
	                ['Female', 'Male'],
	                'Noise comparison of Generated Female vs Male Speakers')
