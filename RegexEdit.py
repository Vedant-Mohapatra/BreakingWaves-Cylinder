import re
import sys
# height, period, stoke


#  for i in {1..16}; do cp -r "WB_VertCyl/" "WB_VertCyl_V${i%}_VM"; done
# run above command to copy parent folder to 16 copies each uniquely named
excel_data = """
0.39976	1.96848	5
0.45122	1.96848	5
0.50269	1.96848	5
0.55415	1.96848	5
0.60561	1.96848	5
0.65707	1.96848	5
0.70854	1.96848	5
0.76000	1.96848	5
0.39999	1.69420	5
0.45431	1.69420	5
0.50864	1.69420	5
0.56296	1.69420	5
0.39989	1.50976	5
0.41562	1.50976	5
0.43134	1.50976	5
0.44706	1.50976	5
"""

parent_directory = "C:/Users/Vedant/Downloads/WB_VertCyl/"
initials = "VM"

#sys lines
# excel_data = sys.argv[1]
# initials = sys.argv[2]
# parent_directory = sys.argv[3]

points = [row.split('\t') for row in excel_data.strip().split('\n')]

# Optional: convert string values to numbers
points = [[float(cell) for cell in row] for row in points]

print(points)
# points = [[0.40000, 2.14286, 2], [0.58571, 2.14286, 5], [0.77143, 2.14286], [0.95714, 2.14286], [1.14286, 2.14286], []]






def ganymedeswap ():
    for i in range(1,17):
        file_path = f"{parent_directory}WB_VertCyl_V{i}_{initials}/SLURM_GANYMEDE2"
        with open(file_path, "r+") as file:
            # read the file contents
            file_contents = file.read()
            new_contents = re.sub("LES_GOS", f"WB_VertCyl_V{i}_{initials}", file_contents)
            file.seek(0)
            file.truncate()
            file.write(new_contents)

def waveFuncSwap ():
    for i in range(1,17):
        file_path = f"{parent_directory}WB_VertCyl_V{i}_{initials}/constant/waveProperties"

        if points[i-1][2] == 2:
            stoke = "StokesII"
        if points[i-1][2] == 5:
            stoke = "StokesV"

        with open(file_path, "r+") as file:
            # swap height
            file_contents = file.read()
            new_contents = re.sub("0.3924", f"{points[i-1][0]}", file_contents)
            file.seek(0)
            file.truncate()
            file.write(new_contents)

        with open(file_path, "r+") as file:
            #swap period
            file_contents = file.read()
            #orig "4.0"
            new_contents = re.sub(r'\b4\.0\b', f"{points[i-1][1]}", file_contents)
            file.seek(0)
            file.truncate()
            file.write(new_contents)

        with open(file_path, "r+") as file:
            #swap stokes
            file_contents = file.read()
            new_contents = re.sub("StokesII", f"{stoke}", file_contents) 
            file.seek(0)
            file.truncate()
            file.write(new_contents)

ganymedeswap()
waveFuncSwap()