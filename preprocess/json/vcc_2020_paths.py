from os.path import expanduser

home = expanduser('~')

data_path = home + '/data/VCC2020-database'

extract_path = home + '/data/VCC2020-database/extract'

transcription_path = home + '/data/VCC2020-database/extract/vcc2020_database_transcriptions'
train_transcription_path = home + '/data/VCC2020-database/extract/vcc2020_database_transcriptions/transcriptions_training'
train_transcription_filename = home + '/data/VCC2020-database/extract/vcc2020_database_transcriptions/transcriptions_training/vcc2020_database_training_Eng_transcriptions.txt'

task_path = home + '/data/VCC2020-database/extract/target_task1'
data_dir = home + '/data/VCC2020-database/extract/target_task1/json'
filelist_dir = home + '/data/VCC2020-database/extract/target_task1/filelist'
exp_base_dir = home + '/data/VCC2020-database/extract/target_task1/exp_base'
