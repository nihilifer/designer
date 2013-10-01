#!/usr/bin/env python
from utils import check_input
from utils import get_frames
from utils import reverse_complement
from utils import score_frame
from utils import score_homogeneity
from utils import two_same_strands_score
from backbone import get_all
from backbone import Backbone
from mfold import mfold
import sys

def main(input_str):
    sequence = check_input(input_str)[0] #just for now
    seq1, seq2, shift_left, shift_right = sequence
    if not seq2:
        seq2 = reverse_complement(seq1)
    all_frames = get_all()
    if 'error' in all_frames: #database error handler
        return all_frames

    frames = get_frames(seq1, seq2, shift_left, shift_right, all_frames)
    original_frames = [Backbone(**elem) for elem in all_frames]


    frames_with_score = []
    for frame_tuple, original in zip(frames, original_frames):
        score = 0
        frame, insert1, insert2 = frame_tuple
        mfold_data = mfold(frame.template(insert1, insert2))
        if 'error' in mfold_data:
            return mfold_data
        pdf, ss = mfold_data[0], mfold_data[1]
        score += score_frame(frame_tuple, ss, original)
        score += score_homogeneity(original)
        score += two_same_strands_score(seq1, original)
        frames_with_score.append((score, frame.template(insert1, insert2)))

    return frames_with_score


if __name__ == '__main__':
    print(main(" ".join(sys.argv[1:])))