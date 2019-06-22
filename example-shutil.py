# import os
#
# resource_dir = "/Users/i0413/python-session/PythonAdvance-1/resources/"
#
# for index in range(10):
#     text = "hello world"
#     filename = "test-file-{index}.txt".format(index=index)
#     filepath = os.path.join(resource_dir, filename)
#     with open(filepath, 'w') as f:
#         f.write(text)
#         f.close()

# import shutil
# import os
# resource_dir = "/Users/i0413/python-session/PythonAdvance-1/resources/"
# destination_dir = "/Users/i0413/python-session/PythonAdvance-1/destination/"
#
# with open(os.path.join(resource_dir, "test-file-1.txt"), "r") as input_file:
#     with open(os.path.join(destination_dir, "test-file-1.txt"), "w") as output_file:
#         shutil.copyfileobj(input_file, output_file)


# import shutil
# import os
# resource_dir = "/Users/i0413/python-session/PythonAdvance-1/resources/"
# destination_dir = "/Users/i0413/python-session/PythonAdvance-1/destination/"
#
# shutil.copyfile(os.path.join(resource_dir, "test-file-1.txt"), os.path.join(destination_dir, "test-output.txt"))


# import shutil
# import os
# resource_dir = "/Users/i0413/python-session/PythonAdvance-1/resources/"
# destination_dir = "/Users/i0413/python-session/PythonAdvance-1/destination/"
# shutil.copy(os.path.join(resource_dir, "test-file-1.txt"), destination_dir)


import shutil
import os
resource_dir = "/Users/i0413/python-session/PythonAdvance-1/resources/"
destination_dir = "/Users/i0413/python-session/PythonAdvance-1/destination/"
shutil.copytree(resource_dir, destination_dir)

