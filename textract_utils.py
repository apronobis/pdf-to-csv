import boto3

textract = boto3.client('textract')

def get_response(file_path):
    with open(file_path, 'rb') as document:  
        image_bytes = document.read()
        
    response = textract.analyze_document(  
        Document={'Bytes': image_bytes},  
        FeatureTypes=['TABLES']  
    )  
    
    return response

def get_rows(table, blocks_map):
    rows = {}

    for relationship in table['Relationships']:  
        if relationship['Type'] == 'CHILD':  
            for child_id in relationship['Ids']:  
                cell = blocks_map[child_id]  
                if cell['BlockType'] == 'CELL':  
                    row_index = cell['RowIndex']  
                    col_index = cell['ColumnIndex']  
                    
                    if row_index not in rows:  
                        rows[row_index] = {}  

                    rows[row_index][col_index] = get_text(cell, blocks_map)
    return rows

def get_text(result, blocks_map):
    text = ''  
    for relationship in result.get('Relationships', []):  
        if relationship['Type'] == 'CHILD':  
            for child_id in relationship['Ids']:  
                word = blocks_map[child_id]
                if word['BlockType'] == 'WORD':  
                    text += word['Text'] + ' '  
    return text.strip()

def get_indices(image_path):
    response = get_response(image_path)
    blocks = response['Blocks']  
    blocks_map = {block['Id']: block for block in blocks}  
    tables = [block for block in blocks if block['BlockType'] == 'TABLE']
    rows = get_rows(tables[0], blocks_map)
    return [i for i, v in enumerate(list(rows[2].values())[1:]) if len(v) > 3]