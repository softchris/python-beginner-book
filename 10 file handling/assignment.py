import os
import zipfile as zip

def print_stats(dir):
    # is valid directory
    if os.path.isdir(dir):
        # get stats
        stats = os.stat(dir)
        print(f'Name: {dir}')
        print(f'Owner: {stats.st_uid}')
        print(f'Permissions: {stats.st_mode}')
        print(f'Files: {os.listdir(dir)}')
        print(f'File count: {len(os.listdir(dir))}')
        print(f'Size: {stats.st_size}')
        print(f'Last modified: {stats.st_mtime}')
        print(f'Last accessed: {stats.st_atime}')
        print(f'Created: {stats.st_ctime}')
    else:
        print('Invalid directory')

def print_list(dir):
    # is valid directory
    if os.path.isdir(dir):
        # get stats
        stats = os.stat(dir)
        print(f'Files: {os.listdir(dir)}')
    else:
        print('Invalid directory')

def compress(dir):
    # is valid directory
    if os.path.isdir(dir):
        # get stats
        stats = os.stat(dir)
        # create zip file
        with zip.ZipFile('backup.zip', 'w') as zip_file:
            # write files to zip file
            for file in os.listdir(dir):
                # only write file if it's a non .zip file
                if not file.endswith('.zip'):
                    zip_file.write(os.path.join(dir, file))
    else:
        print('Invalid directory')

switch = {
    'stats': lambda: print_stats(dir),
    'list': lambda: print_list(dir),
    'compress': lambda: compress(dir),
    'help': lambda: print('Available commands: stats, list, compress, help, exit')
} 

# ask for directory
dir = input('Enter a directory: ')

while True:
    # ask for command
    command = input('Enter a command: ')

    if command in switch:
        print('Executing command...')
        switch[command]()
    elif command == 'exit':
        print('Exiting...')
        break
    else:
        print('Invalid command')
        switch['help']()