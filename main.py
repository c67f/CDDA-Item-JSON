import json
import csv
import pandas as pd
from pathlib import Path

files=[]

def main():
	files = get_files("./items")
	#print("test")

	merge_json_files(files, "itemsMerged.json")

	with open('itemsMerged.json', encoding='utf-8') as j:
		dataframe = pd.read_json(j)
	
	dataframe.to_csv('itemsMergedCVS.csv', encoding='utf-8', index=False)

def merge_json_files(file_paths, output_file):
	merged_data = list()
	for f in file_paths:
		with open(f, 'r', encoding="utf-8") as infile:
			print(f)
			merged_data.extend(json.load(infile))
	with open(output_file, 'w', encoding="utf-8") as outfile:
		json.dump(merged_data, outfile)

def get_files(folder_path):
	files = []
	for f in Path(folder_path).iterdir():
		#print(f.name[-5:])
		if f.suffix == ".json": #f.name[-5:]
			files.append(f)
			print(f)
		elif f.suffix == "":
			files = files + get_files(f) #recursion
	print("files: ")
	print(files)
	return files


	
if __name__ == "__main__":
	main()