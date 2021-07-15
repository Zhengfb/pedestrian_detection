import os
import cv2
import argparse
from deepsort import DeepSort
import warnings
warnings.filterwarnings("ignore")
from main import mainH
def StartPredictNow(path,threahold,usGPU,save_vedio_dir,VideoName,SelectPredictModelPath,SelectFeatureModelPath,testPredictTime):
    parser = argparse.ArgumentParser(
        usage='''you can set the video_path or camera_id to start the program, 
        and also can set the display or save_dir to display the results or save the output video.''',
        description="this is the help of this script."
    )

    parser.add_argument("--det_model_dir", type=str,
                        default=SelectPredictModelPath,
                        help="the detection model dir.")
    parser.add_argument("--emb_model_dir", type=str, default=SelectFeatureModelPath, help="the embedding model dir.")
    parser.add_argument("--run_mode", type=str, default='fluid', help="the run mode of detection model.")
    parser.add_argument("--use_gpu", action="store_true", default=False, help="do you want to use gpu.")

    parser.add_argument("--threshold", type=float, default=0.5, help="the threshold of detection model.")
    parser.add_argument("--max_cosine_distance", type=float, default=0.2, help="the max cosine distance.")
    parser.add_argument("--nn_budget", type=int, default=100, help="the nn budget.")
    parser.add_argument("--max_iou_distance", type=float, default=0.7, help="the max iou distance.")
    parser.add_argument("--max_age", type=int, default=70, help="the max age.")
    parser.add_argument("--n_init", type=int, default=3, help="the number of init.")

    parser.add_argument("--video_path", type=str, default=path,
                        help="the input video path or the camera id.")
    parser.add_argument("--camera_id", type=int, default=0, help="do you want to use the camera and set the camera id.")
    parser.add_argument("--display", action="store_true", help="do you want to display the results.")
    parser.add_argument("--save_dir", type=str, default=save_vedio_dir,
                        help="the save dir for the output video.")

    args = parser.parse_args()
    max_num,one_second = mainH(args,path,save_vedio_dir,threahold,usGPU,VideoName,SelectPredictModelPath,SelectFeatureModelPath,testPredictTime)
    return max_num,one_second