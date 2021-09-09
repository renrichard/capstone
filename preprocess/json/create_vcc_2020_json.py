from os import listdir, makedirs
from os.path import isdir, isfile, join, exists

from librosa.core import load, resample
from soundfile import write

from json import dumps

from preprocess.json.vcc_2020_paths import targets_path, train_transcription_filename
from preprocess.json.vcc_2020_constants import vcc_2020_orig_sr, vcc_2020_target_sr


def get_num_to_transcription():
	with open(train_transcription_filename) as f:
		transcriptions = f.readlines()

	num_to_transcription = dict()

	for t in transcriptions:
		transcription_pair = t.split(' ', 1)
		num, transcription = transcription_pair[0], transcription_pair[1].rstrip()
		num_to_transcription[num] = transcription

	return num_to_transcription


def get_resample_data(target_file):
	target_data, _ = load(target_file, vcc_2020_orig_sr)
	resample_data = resample(target_data, vcc_2020_orig_sr, vcc_2020_target_sr)
	return resample_data


def get_duration(data, sr):
	return len(data) / sr


def main():
	num_to_transcription = get_num_to_transcription()
	targets = sorted([join(targets_path, d) for d in listdir(targets_path) if isdir(join(targets_path, d))])

	for target in targets:

		# create a dir for the resampled files
		resample_dir = join(target, 'resample')
		if not exists(resample_dir):
			makedirs(resample_dir)

		metadata = []

		for f in sorted(listdir(target)):
			if isfile(join(target, f)):

				file_metadata = dict()

				# get the file paths
				target_file = join(target, f)
				resample_file = join(target, 'resample', f)

				# save resample data
				resample_data = get_resample_data(target_file)
				write(resample_file, resample_data, vcc_2020_target_sr)
				file_metadata['audio_filepath'] = resample_file

				# find duration
				duration = get_duration(resample_data, vcc_2020_target_sr)
				file_metadata['duration'] = duration

				# get transcription of the file
				num = f[1:].split('.')[0]
				transcription = num_to_transcription[num]
				file_metadata['text'] = transcription

				metadata.append(file_metadata)


		fp = join(target, 'resample/metadata.json')
		with open(fp, 'w') as f:
				f.write(dumps(metadata).strip('[]') + "\n")
		return


if __name__ == '__main__':
	main()
