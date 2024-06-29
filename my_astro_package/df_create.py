
import cv2
import pandas as pd
from tqdm import tqdm
from pathlib2 import Path
import glob 
def create_df_for_dataset_type(data_path,dataset_type):

    events_mask =  str(data_path / dataset_type / '**' / '*.png')
    file_names = glob.glob(events_mask)
   
    data = []
    for file_path in tqdm(file_names):
        file_path = Path(file_path)
        # print(file_path)
        name = file_path.stem
        name_parts, frame_id = name.split('_t')
        image_name = str(file_path.relative_to(data_path))
        status = file_path.parents[0].stem
        image = cv2.imread(str(file_path))
        data_size= image.shape
        data.append([image_name, name, dataset_type, data_size, str(file_path), status, int(frame_id)])

    # if data:
    columns = ['image_name', 'name', 'dataset_type', 'data_size', 'file_path', 'status', 'frame_id']
    df = pd.DataFrame(data, columns=columns)
    return df.sort_values(by = 'frame_id')