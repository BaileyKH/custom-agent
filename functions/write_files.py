import os
from google.genai import types

def write_file(working_directory, file_path, content):

    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_file_path = os.path.commonpath([absolute_path, target_file]) == absolute_path

        if not valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Error: {e}'
    
schema_write_files = types.FunctionDeclaration(
    name="write_files",
    description="Writes to files relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Writes to files, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)