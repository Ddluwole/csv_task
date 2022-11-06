import json
import csv
import hashlib



team_dict = []
my_file_name = "HNGi9nft.json"




def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

# Function to generate hash of the json file
def generate_hash():
    with open('HNGi9nft.json', 'rb') as json_file:
        data = json_file.read()
        csv_hash = hashlib.sha256(data).hexdigest()
        json_file.close()
        
        return csv_hash



csv_dict = Convert(team_dict)
hash_generated = generate_hash()



# Function to convert a CSV file to JSON
def csv_to_json(hash_generated):
    with open ('HNGi9nft.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        print("Conversion in progress...")
        for col, row in enumerate(reader):
            team_dict = {"format": "CHIP-007",
            "Series_Number": row[1],
            "Filename": row[2],
            "Name": row[3],
            "Description": row[4],
            "Gender": row[5],
            "Attributes": row[6],
            "UUID": row[7],
            }

        # for col, row in enumerate(reader):
        #     team_dict = ["format", "CHIP-007",
        #     "Series_Number", row[1],
        #     "Filename", row[2],
        #     "Name", row[3],
        #     "Description", row[4],
        #     "Gender", row[5],
        #     "Attributes", row[6],
        #     "UUID", row[7],
        #     "sha_256", hash_generated
        #     ]
            # csv_dict = Convert(team_dict)
            # structure = json.dumps(csv_dict, indent=4)
            structure = json.dumps(team_dict, indent=4)
            print(structure)
        print("Conversion Successful!")
           
       
    with open('HNGi9nft.json', 'w') as json_file:
        json_file.write(structure)
        
        json_file.close()
        
csv_to_json(hash_generated)

def output_csv_file():
    print("Writing to file...")
    with open("HNGi9nft.json", "r+") as file:
            file_data = json.load(file)
            for row in file_data.values():
                row["sha_256"] = hash_generated
            # new_data = normalize_json(data=file_data)
            myFile = open("filename.output.csv", "w")
            
            print("Writing Successful")
            print("File saved as {name}.output.csv".format(name=my_file_name))

            writer = csv.writer(myFile)
                
output_csv_file()









            
        






