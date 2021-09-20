import shutil
from glob import glob
from pathlib import Path

""" 
Next Steps: Exceptions to be handled
Case folders already exist in the printing and trimming folder: Abort moving and display the warning
 """

src_root = "D:/Test/1........  Ready for Automation (ZIP)/Exported"
dest_root = "D:/Test/2........  Waiting for Automation"
printing_root = "D:/Test/3. Patients for Printing/0. To be Printed"
trimming_root = "D:/Test/2. Patients for Trim/1........................PATIENTS FOR PROGRAMMING/1. Create MCAM File"

# Count the stl files in the directory
# Input: dir - path to the directory
# Output: the number of stl files in the input directory as a string
def get_stl_count(dir):
	return len(glob(f"{dir}/*.stl"))


# Get the full case name from the case number
# Input: case_number, target_dir - path to the directory containing the case folder with the full case name
# Output: the full case name as a string or an empty string if the case is not found
def get_case_name(case_number, target_dir):
	for case in glob(f"{target_dir}/*"):
		case_name = Path(case).stem
		if case_name.startswith(case_number):
			return case_name
	return ""

success = 0
failure = 0

for case in glob(f"{src_root}/*"):
	case_number = Path(case).stem
	case_full_name = get_case_name(case_number, dest_root)

	if case_full_name == "":
		print(f"Case {case_number} is not found!")
		failure = failure + 1
		continue
	#check if files match
	dest_dir = f"{dest_root}/{case_full_name}/Treatment/3D Printing Files"
	if get_stl_count(case) != get_stl_count(dest_dir):
		print(f"Case {case_number} failed: Files do not match")
		failure = failure + 1
		continue
	for stl_file in glob(f"{case}/*.stl"):
		stl_name = Path(stl_file).name
		shutil.copy(stl_file, dest_dir)
    
	# delete source folder
	shutil.rmtree(case)
	# copy to printing folder
	shutil.copytree(f"{dest_root}/{case_full_name}",f"{printing_root}/{case_full_name}")
	# copy to trimming folder
	shutil.move(f"{dest_root}/{case_full_name}",f"{trimming_root}/{case_full_name}")
	
	
	# delete target folder
	#shutil.rmtree(f"{dest_root}/{case_full_name}")

	print(f"Case {case_number} is moved successfully")
	success = success + 1

print(f"{success} cases are moved successfully.")
print(f"{failure} cases failed.")