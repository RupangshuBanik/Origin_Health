import csv
import os
import shutil

# Get the paths to the source folder, destination folders, and CSV file
source_folder = r'D:\\Origin_Health_Project\\Training Images'
destination_folders = ["D:\Origin_Health_Project\Fetal abdomen",
                      "D:\Origin_Health_Project\Fetal brain",
                      "D:\Origin_Health_Project\Fetal femur",
                      "D:\Origin_Health_Project\Fetal thorax"]
csv_file = "D:\Origin_Health_Project\image_label.csv"

# Read the CSV file
with open(csv_file, "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # Get the file name and type
        file_name = row["Image_name"]
        file_type = row["Plane"]
        
        
        # Get the destination folder path
        destination_folder_path = destination_folders[int((file_type))]

        # Move the file to the destination folder
        shutil.move(os.path.join(source_folder, file_name), destination_folder_path)

