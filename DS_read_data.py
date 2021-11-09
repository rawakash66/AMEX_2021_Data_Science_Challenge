import json,csv, pandas as pd
from os import listdir
from os.path import isfile, join

#replace this with your local directory path
local_path = """local_dir/train/"""

filenames = (sorted([f for f in listdir(local_path+"input") if isfile(join(local_path+"input", f))], key = lambda x: int(x[6:10])  ), \
             sorted([f for f in listdir(local_path+"output") if isfile(join(local_path+"output", f))], key = lambda x: int(x[6:10])))
paths = (local_path+"input/",local_path+"output/")

##column headers
fields = ['image_id', 'textAnnotation_id', 'x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'description', 'label']

## Function to convert Input and Output JSON to arrays
def train_data_extractor(filenames,fields_merge):
    #read input json, extract text ids, vertices and description and store in an array. Convert array to dataframe.
    input_array = []
    for filename in filenames[0]:
        input_file = open(paths[0]+filename,"r")
        input_json = json.loads(input_file.read())
        for i in input_json["textAnnotations"] :
            temp_array = []
            temp_array.append(filename[:-5])
            temp_array.append(input_json["textAnnotations"].index(i))
            for j in i["boundingPoly"]["vertices"] :
                temp_array.append(j["x"])
                temp_array.append(j["y"])
            temp_array.append(i["description"])
            input_array.append(temp_array)
    input_df = pd.DataFrame(input_array, columns = fields[:11])
    
    #read output json, extract text ids and label and store in an array. Convert array to dataframe.
    output_array = []
    for filename in filenames[1]:              
        output_file = open(paths[1]+filename,"r")
        output_json = json.loads(output_file.read())
        for j in output_json :
            temp_array = []
            temp_array.append(filename[:10])
            temp_array.append(j["id"])
            temp_array.append(j["label"]) 
            output_array.append(temp_array)
    output_df = pd.DataFrame(output_array, columns = [fields[i] for i in [0,1,11]])
    
    #return inner join of the two dataframes based on the fields passed as a parameter to the function. 
    #inner join is also used to remove any rows with NaN
    
    return  pd.merge(input_df, output_df, on= [fields[i] for i in fields_merge], how="inner")



train_df = train_data_extractor(filenames,[0,1]) #merge dfs based on image id, text id and description

#print our df
train_df.head()


