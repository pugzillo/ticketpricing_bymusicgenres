import numpy as np
import pandas as pd
import glob
import re
import multiprocessing

# reading in spotify outputs from the directory

files = glob.glob("*_SongInfo.csv")

# files = files[0:10]

def read_file(file, output): # return a temp df with the data from an individual file
    # file, results = arg[0], arg[1]
    global results
    print(str(file))
    temp = pd.read_csv(file, sep=",")
    temp['artist'] = re.sub('_SongInfo.csv', '', file)
    temp = temp.drop('Unnamed: 0', axis=1) # remove the indexes
    # print(temp)
    # results.append(temp)
    # if results.empty:
    #     print("Hi")
    #     results = temp.copy()
    # else:
    #     print("NO")
    #     results.append(temp)
    return temp

results = pd.DataFrame()

df_list = [results for i in range(len(files))]

# run the workers
with multiprocessing.Pool(50) as workers:
    res_list = workers.starmap(read_file, zip(files, df_list))

# print(res_list[0], str(type(res_list[0])))

# print(type(res_list))

# concat the list of temp df
res_df = pd.concat(res_list)
# print(res_df)

# for i in range(1, len(res_list)):
#     res_list[0].append(res_list[i], ignore_index=True)

# print(res_list)

# print(songfeat)
res_df.to_csv('TicketArtist_SpotifySongFeatures.csv')