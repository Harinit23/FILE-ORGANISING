import os
import argparse

def search_directory(directory, criteria):
    results = []

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            
            if criteria['name'] and criteria['name'] not in file_name:
                continue

          
            if criteria['extension'] and not file_name.endswith(criteria['extension']):
                continue

           
            file_size = os.path.getsize(file_path)
            if criteria['min_size'] and file_size < criteria['min_size']:
                continue
            if criteria['max_size'] and file_size > criteria['max_size']:
                continue

            results.append(file_path)

    return results

def main():
    parser = argparse.ArgumentParser(description="File and directory search tool")
    parser.add_argument("directory", help="Directory to search in")
    parser.add_argument("--name", help="Search by file name or part of a file name")
    parser.add_argument("--extension", help="Search by file extension (e.g., .txt, .jpg)")
    parser.add_argument("--min-size", type=int, help="Search for files larger than this size (in bytes)")
    parser.add_argument("--max-size", type=int, help="Search for files smaller than this size (in bytes)")
    args = parser.parse_args()

    criteria = {
        'name': args.name,
        'extension': args.extension,
        'min_size': args.min_size,
        'max_size': args.max_size
    }

    if not any(criteria.values()):
        print("Please specify at least one search criteria.")
        return

    results = search_directory(args.directory, criteria)

    if results:
        print("Matching files and directories:")
        for result in results:
            print(result)
    else:
        print("No matching files or directories found.")

if __name__== "__main_":
    main()