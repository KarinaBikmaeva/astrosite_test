import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

def find_count_area(df, dataset_type, types_images_events="events"):
    df_type = df[df['status'] == types_images_events]
    regions_count = []

    for index, row in df_type.iterrows():

        image_path = row['file_path']
        image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
        image_array = np.array(image)
        _, thresh = cv2.threshold(image_array, 175, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        regions_count.append(len(contours))

    df_areas = pd.DataFrame({
        
        'video': dataset_type,
        'image_index': df_type['frame_id'],
        'area': regions_count
    })
    
    return df_areas
