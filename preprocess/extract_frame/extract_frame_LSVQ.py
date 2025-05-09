import numpy as np
import os
import pandas as pd
import cv2
from tqdm import tqdm


def extract_frame(videos_dir, video_name, save_folder):
    filename = os.path.join(videos_dir, video_name + '.mp4')
    video_capture = cv2.VideoCapture()
    video_capture.open(filename)
    cap=cv2.VideoCapture(filename)

    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_frame_rate = int(round(cap.get(cv2.CAP_PROP_FPS)))

    video_read_index = 0

    frame_idx = 0
    
    video_length_min = 8

    for i in range(video_length):
        has_frames, frame = video_capture.read()
        if has_frames:
            # key frame
            if (video_read_index < video_length) and (frame_idx % (int(video_frame_rate)) == int(video_frame_rate/2)):
                # read_frame = cv2.resize(frame, dim)
                read_frame = frame
                exit_folder(os.path.join(save_folder, video_name))
                cv2.imwrite(os.path.join(save_folder, video_name,
                                         '{:03d}'.format(video_read_index) + '.png'), read_frame)          
                video_read_index += 1
            frame_idx += 1
            
    if video_read_index < video_length_min:
        for i in range(video_read_index, video_length_min):
            cv2.imwrite(os.path.join(save_folder, video_name,
                                     '{:03d}'.format(i) + '.png'), read_frame)


    return
            
def exit_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)    
        
    return

if __name__ == '__main__':
    # train subset
    filename_path = 'your_path'

    column_names = ['name', 'p1', 'p2', 'p3', \
                    'height', 'width', 'mos_p1',\
                    'mos_p2', 'mos_p3', 'mos', \
                    'frame_number', 'fn_last_frame', 'left_p1',\
                    'right_p1', 'top_p1', 'bottom_p1', \
                    'start_p1', 'end_p1', 'left_p2', \
                    'right_p2', 'top_p2', 'bottom_p2', \
                    'start_p2', 'end_p2', 'left_p3', \
                    'right_p3', 'top_p3', 'bottom_p3', \
                    'start_p3', 'end_p3', 'top_vid', \
                    'left_vid', 'bottom_vid', 'right_vid', \
                    'start_vid', 'end_vid', 'is_test', 'is_valid']

    dataInfo = pd.read_csv(filename_path, header = 0, sep=',', names=column_names, index_col=False, encoding="utf-8-sig")


    video_names = dataInfo['name']
    n_video = len(video_names)
    videos_dir = 'your_path'

    save_folder = 'your_path'
    for i in tqdm(range(n_video),total=n_video):
        video_name = video_names.iloc[i]
        extract_frame(videos_dir, video_name, save_folder)



    filename_path = 'your_path'


    # test subset
    column_names = ['name', 'p1', 'p2', 'p3', \
                    'height', 'width', 'mos_p1',\
                    'mos_p2', 'mos_p3', 'mos', \
                    'frame_number', 'fn_last_frame', 'left_p1',\
                    'right_p1', 'top_p1', 'bottom_p1', \
                    'start_p1', 'end_p1', 'left_p2', \
                    'right_p2', 'top_p2', 'bottom_p2', \
                    'start_p2', 'end_p2', 'left_p3', \
                    'right_p3', 'top_p3', 'bottom_p3', \
                    'start_p3', 'end_p3', 'top_vid', \
                    'left_vid', 'bottom_vid', 'right_vid', \
                    'start_vid', 'end_vid', 'is_test', 'is_valid']

    dataInfo = pd.read_csv(filename_path, header = 0, sep=',', names=column_names, index_col=False, encoding="utf-8-sig")


    video_names = dataInfo['name']
    n_video = len(video_names)
    videos_dir = 'your_path'

    save_folder = 'your_path'
    for i in tqdm(range(n_video),total=n_video):
        video_name = video_names.iloc[i]
        print('start extract {}th/{}th video: {}'.format(i, n_video, video_name))
        extract_frame(videos_dir, video_name, save_folder)


    # test_1080p subset
    filename_path = 'your_path'

    column_names = ['name', 'p1', 'p2', 'p3', \
                    'height', 'width', 'mos_p1',\
                    'mos_p2', 'mos_p3', 'mos', \
                    'frame_number', 'fn_last_frame', 'left_p1',\
                    'right_p1', 'top_p1', 'bottom_p1', \
                    'start_p1', 'end_p1', 'left_p2', \
                    'right_p2', 'top_p2', 'bottom_p2', \
                    'start_p2', 'end_p2', 'left_p3', \
                    'right_p3', 'top_p3', 'bottom_p3', \
                    'start_p3', 'end_p3', 'top_vid', \
                    'left_vid', 'bottom_vid', 'right_vid', \
                    'start_vid', 'end_vid', 'is_valid']

    dataInfo = pd.read_csv(filename_path, header = 0, sep=',', names=column_names, index_col=False, encoding="utf-8-sig")


    video_names = dataInfo['name']
    n_video = len(video_names)
    videos_dir = 'your_path'

    save_folder = 'your_path'
    for i in tqdm(range(n_video),total=n_video):
        video_name = video_names.iloc[i]
        extract_frame(videos_dir, video_name, save_folder)