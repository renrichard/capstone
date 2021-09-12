from os import listdir, makedirs
from os.path import isdir, isfile, join, exists

from librosa.core import load, resample
from soundfile import write

from json import dumps

from re import sub

from preprocess.json.vcc_2020_paths import task_path, train_transcription_filename, data_dir
from preprocess.json.vcc_2020_constants import vcc_2020_orig_sr, vcc_2020_target_sr, speakers


def get_num_to_transcription():
	with open(train_transcription_filename) as f:
		transcriptions = f.readlines()

	num_to_transcription = dict()

	for t in transcriptions:
		transcription_pair = t.split(' ', 1)
		num, transcription = transcription_pair[0], transcription_pair[1].rstrip()
		num_to_transcription[num] = transcription

	return num_to_transcription


def create_dir(new_dir_path):
	if not exists(new_dir_path):
		makedirs(new_dir_path)



def get_resample_data(target_file):
	target_data, _ = load(target_file, vcc_2020_orig_sr)
	resample_data = resample(target_data, vcc_2020_orig_sr, vcc_2020_target_sr)
	return resample_data


def get_duration(data, sr):
	return len(data) / sr


def create_vcc_2020_json():
	num_to_transcription = get_num_to_transcription()

	# create a dir for the json files
	create_dir(data_dir)

	for speaker in speakers:
		speaker_path = join(task_path, speaker)

		# create a dir for the resampled files
		resample_dir = join(speaker_path, 'resample')
		create_dir(resample_dir)

		metadata = []

		for f in sorted(listdir(speaker_path)):
			if isfile(join(speaker_path, f)):

				file_metadata = dict()

				# get the file paths
				speaker_file = join(speaker_path, f)
				resample_file = join(resample_dir, f)

				# save resample data
				resample_data = get_resample_data(speaker_file)
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

		fp = join(data_dir, '{}_metadata.json'.format(speaker))
		with open(fp, 'w') as f:
			contents = dumps(metadata).strip('[]')
			contents = sub('}, {', '}\n{', contents)
			f.write(contents)


if __name__ == '__main__':
	create_vcc_2020_json()
