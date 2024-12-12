from pathlib import Path
from rembg import remove, new_session

session = new_session()

for file in Path(r'C:\Users\sarfa\Documents\PythonProject\image-background'
                 r'-removal-api-end-to-end-pipeline\data').glob('*'):
    input_path = str(file)
    output_path = str(file.parent / (file.stem + ".out.png"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, session=session)
            o.write(output)
