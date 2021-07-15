import numpy as np
from model import  Embedding
from python.infer import Detector
import paddle
from deep_sort import NearestNeighborDistanceMetric, Detection, Tracker
import copy
__all__ = ['DeepSort']

class DeepSort(object):
    def __init__(
        self, 
        det_model_dir, 
        emb_model_dir, 
        use_gpu=False, 
        run_mode='fluid', 
        threshold=0.5,
        max_cosine_distance=0.2, 
        nn_budget=100, 
        max_iou_distance=0.9, 
        max_age=70, 
        n_init=3
    ):
        #  pred_config,
        #          model_dir,
        #          use_gpu=False,
        #          run_mode='fluid',
        #          use_dynamic_shape=False,
        #          trt_min_shape=1,
        #          trt_max_shape=1280,
        #          trt_opt_shape=640,
        #          threshold=0.5
        # if paddle.fluid.is_compiled_with_cuda():
        #     use_gpu = True
        print("deepSort里面使用GPU状态：",use_gpu)
        self.detector = Detector(det_model_dir, det_model_dir,use_gpu)#标记原本是True
        self.emb = Embedding(emb_model_dir, use_gpu)
        self.threshold = threshold
        metric = NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
        self.tracker = Tracker(metric, max_iou_distance=max_iou_distance, max_age=max_age, n_init=n_init)

    def update(self, ori_img):
        self.height, self.width = ori_img.shape[:2]
        results,one_second = self.detector.predict(ori_img, self.threshold)

        if results == 'none':
            print("本帧未识别出行人")
            return 'none',0
        else:
            np_boxes = results['boxes']
            expect_boxes = (np_boxes[:, 1] > self.threshold) & (np_boxes[:, 0] > -1)
            np_boxes = np_boxes[expect_boxes, :]
            xy_list = []
            con_list = []
            tl_list = []
            for dt in np_boxes:
                clsid, bbox, score = int(dt[0]), dt[2:], dt[1]
                xmin, ymin, xmax, ymax = bbox
                xmin, ymin, xmax, ymax  = int(xmin),int(ymin),int(xmax),int(ymax)
                w = xmax - xmin
                h = ymax - ymin
                tl_list.append([xmin,ymin,w,h])
                xy_list.append([xmin,ymin,xmax,ymax])
                con_list.append(score)
            tlwh = copy.deepcopy(tl_list) 
            xyxy = copy.deepcopy(xy_list) 
            confidences = copy.deepcopy(con_list) 
            if not confidences:
                return 'none',0
        # generate detections
        features = self.get_features(xyxy, ori_img)
        detections = [Detection(tlwh[i], conf, features[i]) for i,conf in enumerate(confidences)]

        # update tracker
        self.tracker.predict()
        self.tracker.update(detections)

        # output bbox identities
        outputs = []
        for track in self.tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue
            box = track.to_tlbr()
            x1,y1,x2,y2 = box
            track_id = track.track_id
            outputs.append(np.array([x1,y1,x2,y2,track_id], dtype=np.int))
        if len(outputs) > 0:
            outputs = np.stack(outputs,axis=0)
        return outputs,one_second

    def get_features(self, xyxy, ori_img):
        crops = []
        for bbox in xyxy:
            crop = ori_img[bbox[1]:bbox[3], bbox[0]:bbox[2], :]
            crops.append(crop)
        features = self.emb.predict(crops)
        return features

if __name__ == '__main__':

    deepsort = DeepSort('../model/detection', '../model/embedding', True)
    import cv2

    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        success, frame = cap.read()
        outputs = deepsort.update(frame)
        if outputs is not None:
            for output in outputs:
                cv2.rectangle(frame, (output[0], output[1]), (output[2], output[3]), (0,0,255), 2)
                cv2.putText(frame, str(output[-1]), (output[0], output[1]), font, 1.2, (255, 255, 255), 2)
        # print(outputs)
        cv2.imshow('test', frame)
        k = cv2.waitKey(1)
        if k==27:
            break
