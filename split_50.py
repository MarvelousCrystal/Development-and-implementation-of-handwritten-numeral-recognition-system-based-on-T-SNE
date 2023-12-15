import os
import fileinput

#将降维后的结果按照标签分成10个txt文件，每个finalall_partx.txt代表数字x的二维图片
def split_file(input_file, chunk_size):
    # Loop through the input file and split it into chunks of chunk_size lines
    with fileinput.input(files=input_file, mode='r') as f:
        for i, line in enumerate(f):
            # If we've reached the end of a chunk, create a new output file
            if i % chunk_size == 0:
                # Close the previous output file, if it exists
                try:
                    out.close()
                except NameError:
                    pass

                # Create a new output file with a numbered suffix
                output_file = os.path.splitext(input_file)[0] + f'_part{i//chunk_size}.txt'

                # Open the output file for writing
                out = open(output_file, 'w')

            # Write the current line to the output file
            out.write(line)

        # Close the final output file
        out.close()

# if __name__ == '__main__':
#     # Call the split_file function with the input file and chunk size
#     split_file('./2Dresult/all_final_backup.txt', 50)