import glob
import os
import argparse
import numpy as np
from scipy.io import wavfile


def codec_sim(path, medium, out_folder):
    """
    Audio degradation using codec simulation
    @param path: Input file path
    @param medium: Communication medium
    @param out_folder: Output folder
    @return: Sample rate and audio data in numpy array
    """
    if medium == 'random':
        mediums = ['cellular', 'landline', 'voip', 'satellite']
        medium = np.random.choice(mediums)
    seed = str(np.random.randint(1, 100))
    with open("path.txt", "w") as outfile:
        outfile.write(path)
    os.system('rm -r ' + out_folder + '/*')
    os.system('python degrade-audio-list-safe-random__.py -s ' + seed + ' ' + medium + ' path.txt ' + out_folder)
    converted_file = glob.glob(os.path.join(out_folder, medium)+'/*')[0]
    sample_rate, data = wavfile.read(converted_file)
    os.system('rm path.txt')
    return sample_rate, data


def parser():
    """
    Argument parser function to use from terminal
    @return: Parser object
    """
    parse = argparse.ArgumentParser()
    parse.add_argument("path", nargs="?", help="Path to input file")
    parse.add_argument("-m", dest="medium", default="random", help="Transmission medium selection (random,cellular,"
                                                                   "landline,voip,satellite,interview,playback) - "
                                                                   "Default=random")
    parse.add_argument("-o", dest="out_folder", default="out", help="Converted file directory, Default=out")
    ops = parse.parse_args()
    return ops


def main():
    ops = parser()
    sample_rate, data = codec_sim(ops.path, ops.medium, ops.out_folder)


if __name__ == '__main__':
    main()
