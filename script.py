import os
import argparse
import shutil
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('number_of_lines_and_name_project', nargs=2)
 
    return parser

def glue_commits(ProjectName,NumbetOfLines):
	dirlist = [ item for item in os.listdir(ProjectName) if os.path.isdir(os.path.join(ProjectName, item)) ]

	print(dirlist)
	for path in dirlist:
		dirlist2 = [ item for item in os.listdir(ProjectName + '/' +path) if os.path.isdir(os.path.join(ProjectName + '/' +path, item)) ]
		print(dirlist2)

		for path2 in dirlist2:
			dirlist3 = [item for item in os.listdir(ProjectName + '/' + path+ '/' + path2) if os.path.isdir(os.path.join(ProjectName + '/' + path+ '/' + path2, item))]
			for path3 in dirlist3:
				directory_list = list()
				for root, dirs, files in os.walk(ProjectName + '/' +path + '/'+path2+ '/'+path3, topdown=False):
					for name in files:
						directory_list.append(os.path.join(root, name))
					print(directory_list)

				if len(directory_list) > 0:
					if os.path.exists(ProjectName + '/' +path + '/'+path2+ '/'+path3 + "/glued_commits.txt") == False:
						FAIL = open(ProjectName + '/' +path + '/'+path2+ '/'+path3 + "/glued_commits.txt","a+")
					else:
						break

					for name in directory_list:

						line_count = 0
						with open(name) as f:
							for line in f:
								line_count += 1

						if(line_count<NumbetOfLines):
							FAIL_2 = open(name,'r')
							for i in FAIL_2:
								FAIL.write(i.strip() + '\n')

							FAIL_2.close()
							try:
								os.remove(name)
							except PermissionError:
								pass
		 	
				FAIL.close()
def main():
	parser = createParser()
	namespace = parser.parse_args()

	glue_commits(namespace.number_of_lines_and_name_project[0], int(namespace.number_of_lines_and_name_project[1]))

if __name__ == '__main__':
	main()