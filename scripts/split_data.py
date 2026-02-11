import json
import os

def split_json_file(input_file, output_folder, chunk_size_mb=500):
    """Splits a large JSON file into smaller chunks for S3 upload."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    chunk_size = chunk_size_mb * 1024 * 1024  # Convert MB to Bytes
    file_number = 1
    current_chunk = []
    current_size = 0

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line_size = len(line.encode('utf-8'))
            if current_size + line_size > chunk_size:
                # Save current chunk
                with open(f"{output_folder}/yelp_data_part_{file_number}.json", 'w') as out:
                    out.writelines(current_chunk)
                print(f"Created chunk {file_number}")
                file_number += 1
                current_chunk = []
                current_size = 0
            
            current_chunk.append(line)
            current_size += line_size

    # Write the remaining data
    if current_chunk:
        with open(f"{output_folder}/yelp_data_part_{file_number}.json", 'w') as out:
            out.writelines(current_chunk)

if __name__ == "__main__":
    split_json_file('yelp_academic_dataset_review.json', 'output_chunks')
