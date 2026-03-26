import os
from google.genai import types

def get_files_info(working_directory, directory="."):

    try:
        absolute_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_path = os.path.commonpath([absolute_path, target_path]) == absolute_path

        get_files = []

        if not valid_target_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'
        
        for dir in os.listdir(target_path):
            full_path = os.path.join(target_path, dir)
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)

            get_files.append(f'- {dir}: file_size={file_size} bytes, is_dir={is_dir}')

        return '\n'.join(get_files)
    except Exception as e:
        return f'Error: {e}'
    

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)