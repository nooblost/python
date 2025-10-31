"""
file_object = open('filename', 'mode')


config_file = open('config.txt', 'r')
# Or simply, since 'r' is the default:
# config_file = open('config.txt')

Modes:

r - read mode
w - write mode - will overwrite existing file, will create file if filename doesnt exist
a - append mode - will not overwrite existing file, will create file if filename doesnt exist

log_file = open('log.txt', 'a')

output_file = open('output.txt', 'w')

# Open the file for writing
output_file = open('output.txt', 'w')

# Perform write operations (covered in the next sections)
output_file.write('This is the first line.\n')
output_file.write('This is the second line.\n')

# Explicitly close the file
output_file.close()

"""