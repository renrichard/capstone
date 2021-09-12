import os
import os.path as path

import librosa.core as lr

import soundfile as sf

import json

import re

import preprocess.json.vcc_2020_paths as vpaths
import preprocess.json.vcc_2020_constants as cnst


def get_num_to_transcription():
	with open(vpaths.train_transcription_filename) as f:
		transcriptions = f.readlines()

	num_to_transcription = dict()

	for t in transcriptions:
		transcription_pair = t.split(' ', 1)
		num, transcription = transcription_pair[0], transcription_pair[1].rstrip()
		num_to_transcription[num] = transcription

	return num_to_transcription


def create_dir(new_dir_path):
	if not path.exists(new_dir_path):
		os.makedirs(new_dir_path)


def get_resample_data(target_file):
	target_data, _ = lr.load(target_file, cnst.orig_sr)
	resample_data = lr.resample(target_data, cnst.orig_sr, cnst.target_sr)
	return resample_data


def get_duration(data, sr):
	return len(data) / sr


def create_vcc_2020_json():
	num_to_transcription = get_num_to_transcription()

	# create a dir for the json files
	create_dir(vpaths.data_dir)

	for speaker in cnst.speakers:
		target_path = path.join(vpaths.task_path, speaker)

		# create a dir for the resampled files
		resample_dir = path.join(target_path, 'resample')
		create_dir(resample_dir)

		metadata = []

		for f in sorted(os.listdir(target_path)):
			if path.isfile(path.join(target_path, f)):
				file_metadata = dict()

				# get the file paths
				target_file = path.join(target_path, f)
				resample_file = path.join(resample_dir, f)

				# save resample data
				resample_data = get_resample_data(target_file)
				sf.write(resample_file, resample_data, cnst.target_sr)
				file_metadata['audio_filepath'] = resample_file

				# find duration
				duration = get_duration(resample_data, cnst.target_sr)
				file_metadata['duration'] = duration

				# get transcription of the file
				num = f[1:].split('.')[0]
				transcription = num_to_transcription[num]
				file_metadata['text'] = transcription

				metadata.append(file_metadata)

		fp = path.join(vpaths.data_dir, '{}_metadata.json'.format(speaker))
		with open(fp, 'w') as f:
			contents = json.dumps(metadata).strip('[]')
			contents = re.sub('}, {', '}\n{', contents)
			f.write(contents)


if __name__ == '__main__':
	create_vcc_2020_json()
