import tempfile
import os
import numpy as np

def get_tmppath(ext = 'amr'):
    temp_name = next(tempfile._get_candidate_names())+'.'+ext
    defult_tmp_dir = tempfile._get_default_tempdir()
    return os.path.join(defult_tmp_dir,temp_name)

def convert(input_dir,output_dir,ffmpegAPI='python'):
    """
    Converts normal audio data to AMRNB with varying quality
    :param input_dir: directory with input files (audio/video)
    :param output_dir: directory where to store output audio files
    """
    available_bitrate = [4750, 5150, 5900, 6700, 7400, 7950, 10200, 12200]
    for input_audio_filename in os.listdir(input_dir):
        input_file = os.path.join(input_dir,input_audio_filename)
        chosen_bitrate = np.random.choice(available_bitrate)
        params = { 'ab': chosen_bitrate,'ar': 8000, 'c:a': 'amr_nb','ac':1}
        num_recompressions = np.random.randint(0,5)
        ffmpeg_params = ' '
        for key,value in params.items():
            ffmpeg_params += f'-{key} {value} '

        tmp_out = get_tmppath()
        if ffmpegAPI == 'python':
            import ffmpeg

            ( 	ffmpeg.input( input_file)
                    .audio
                    .output(tmp_out,**params)
                    .overwrite_output()
                    .run()
             )
        else:
            ffmpeg_cmd = f'ffmpeg -i {input_file} '+'-y' + ffmpeg_params + tmp_out
            os.system(ffmpeg_cmd)



        name_params = f'-recomp{num_recompressions}'
        for key,value in params.items():
            name_params += f'-{key}{value}'

        outfile_name = os.path.basename(input_file)[:-4] +name_params + '.amr'
        output_file_path = os.path.join(output_dir,outfile_name)


        for i in range(num_recompressions):
            old_tmp_out = tmp_out
            tmp_out = get_tmppath()
            if i==num_recompressions-1:
                tmp_out=output_file_path
            if ffmpegAPI=='python':
                import ffmpeg
                (ffmpeg.input(old_tmp_out)
                    .output(tmp_out,**params)
                    .overwrite_output()
                    .run()
                )
            else:
                ffmpeg_cmd = f'ffmpeg -i {old_tmp_out} ' + '-y' + ffmpeg_params + tmp_out
                os.system(ffmpeg_cmd)



        print(params)
        print(f'Recompressions: {num_recompressions}')


if __name__=='__main__':
    input_dir = '../data/processed/AMRNB/input'
    input_dir = '../data/SpeechAccentArchiveKaggle/recordings/recordings'
    output_dir = '../data/processed/AMRNB/output'
    convert(input_dir,output_dir,ffmpegAPI='python')


   
