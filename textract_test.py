#!/usr/bin/env python3
import boto3
from os.path import join, split
from pathlib import Path
from json import dump


"""
    Send files to AWS Textract and serialize results.
    Iterates through S3 bucket and sends all appropriate files to Textract DetectDocumentText.  Serializes full output
    (bounding boxes, coordinates, etc) to a file and only extracted text to another.
    
    @author jjt
    @version May 23, 2020
"""

def get_keys(bucketname, extensions):
    """Return all keys (filepaths) in bucket"""
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket= bucketname, FetchOwner=False)
    keys = []
    for obj in response['Contents']:
        try:
            ext = obj['Key'].rsplit(sep='.', maxsplit=1)[1].lower()
            if ext in extensions:
                keys.append(obj['Key'])
            else:
                pass
        except IndexError:
            pass
    return keys


def extract_text(bucketname, filepath):
    """Return OCR data associated with filepaths"""
    textract = boto3.client('textract')
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucketname,
                'Name': filepath
            }
        })
    return response


def save_output(file, outputdir, ocr):
    """Serialize OCR data to files"""
    filename = file.rsplit(sep='/', maxsplit=1)[1]
    # write all output to file as json
    with open(join(outputdir, filename + '-all.txt'), 'w') as allocr:
        dump(ocr, allocr, indent=4, sort_keys=True)
    allocr.close()
    # write only detected text
    text = open(join(outputdir, filename + '-text.txt'), 'w')
    for item in ocr["Blocks"]:
        if item["BlockType"] == "LINE":
            text.write(item["Text"] + '\n')
    text.close()


def main(bucketname, outputdir, extensions):
    """Execute if run as script"""
    files = get_keys(bucketname, extensions)
    for file in files:
        ocr = extract_text(bucketname, file)
        save_output(file, outputdir, ocr)


# set variables
bucket = "<bucket_name>"
outputPath = "</path/to/directory"
approvedExtensions = ['jpg', 'jpeg', 'png']  # filetypes Textract accepts for synchronous operations

if __name__ == "__main__":
    main(bucket, outputPath, approvedExtensions)

