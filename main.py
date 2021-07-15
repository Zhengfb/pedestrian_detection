import os
import cv2
import argparse
from deepsort import DeepSort
import warnings
warnings.filterwarnings("ignore")

def mainH(args,path,save_vedio_dir,threahold,usGPU,VideoName,SelectPredictModelPath,SelectFeatureModelPath,testPredictTime):
    deepsort = DeepSort(
        det_model_dir=SelectPredictModelPath,
        emb_model_dir=SelectFeatureModelPath,
        use_gpu=usGPU,
        run_mode='fluid', 
        threshold=threahold,
        max_cosine_distance=0.2,
        nn_budget=100,
        max_iou_distance=0.7,
        max_age=70,
        n_init=3
    )
    cap = cv2.VideoCapture(path)
    print('在main函数, usGPU: ',usGPU)
    # if args.video_path:
    #     cap = cv2.VideoCapture(args.video_path)
    # else:
    #     cap = cv2.VideoCapture(args.camera_id)

    font = cv2.FONT_HERSHEY_SIMPLEX

    if save_vedio_dir:
        if not os.path.exists(save_vedio_dir):
            print(save_vedio_dir)
            os.mkdir(save_vedio_dir)
        fps = cap.get(cv2.CAP_PROP_FPS)
        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(fps, w, h)
        if testPredictTime!=0:
            save_video_path = os.path.join(save_vedio_dir, VideoName)
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            writer = cv2.VideoWriter(save_video_path, fourcc, fps, (int(w), int(h)))
    fff = -1
    max_num=0
    while True:
        
        # < frame >,< id >,< bb_left >,< bb_top >,< bb_width >,< bb_height >,< conf >,< x >,< y >, < z>
        success, frame = cap.read()
        string = ""
        l = 0
        string = string+str(fff)+","
        if not success:
            break
        outputs,one_second = deepsort.update(frame)
        if testPredictTime==0:
            break
        if outputs == "none":
            print("空了空了")

        if outputs is not 'none':
            l = len(outputs)
            for output in outputs:
                temp_s = string
                cv2.rectangle(frame, (int(output[0]), int(output[1])), (int(output[2]), int(output[3])), (0,0,255), 2)
                cv2.putText(frame, str(output[-1]), (int(output[0]), int(output[1])), font, 1.2, (255, 255, 255), 2)
                w = output[2]-output[0]
                h = output[3]-output[1]
                if output[-1]>max_num:
                    max_num = output[-1]
                # print(temp_s)
        # print(outputs)
        # print("l长度",l)
        cv2.putText(frame, "Number of people: "+str(l), (10,30), font, 1.2, (0, 0, 255), 4)
        cv2.putText(frame, "The number of people who showed up: "+str(max_num), (10,60), font, 1.2, (0, 0, 255), 4)
        if save_vedio_dir:
            writer.write(frame)
        if args.display:
            cv2.imshow(' ', frame)
            k = cv2.waitKey(1)
            if k==27:
                cap.release()
                break
        fff+=1
        if testPredictTime==0:
            break
    print("max_num = ",max_num)
    if save_vedio_dir and testPredictTime!=0:
        writer.release()
    return max_num,one_second
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='''you can set the video_path or camera_id to start the program, 
        and also can set the display or save_dir to display the results or save the output video.''', 
        description="this is the help of this script."
    )

    parser.add_argument("--det_model_dir", type=str, default='model\\detection\\pedestrian_yolov3_darknet', help="the detection model dir.")
    parser.add_argument("--emb_model_dir", type=str, default='model/embedding', help="the embedding model dir.")
    parser.add_argument("--run_mode", type=str, default='fluid', help="the run mode of detection model.")
    parser.add_argument("--use_gpu", action="store_true",default=False, help="do you want to use gpu.")

    parser.add_argument("--threshold", type=float, default=0.5, help="the threshold of detection model.")
    parser.add_argument("--max_cosine_distance", type=float, default=0.2, help="the max cosine distance.")
    parser.add_argument("--nn_budget", type=int, default=100, help="the nn budget.")
    parser.add_argument("--max_iou_distance", type=float, default=0.7, help="the max iou distance.")
    parser.add_argument("--max_age", type=int, default=70, help="the max age.")
    parser.add_argument("--n_init", type=int, default=3, help="the number of init.")

    parser.add_argument("--video_path", type=str, default='', help="the input video path or the camera id.")
    parser.add_argument("--camera_id", type=int, default=0, help="do you want to use the camera and set the camera id.")
    parser.add_argument("--display", action="store_true", help="do you want to display the results.")
    parser.add_argument("--save_dir", type=str, default='', help="the save dir for the output video.")
 
    args = parser.parse_args()
    mainH(args)
