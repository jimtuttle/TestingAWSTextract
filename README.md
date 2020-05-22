# TestingAWSTextract
Test OCR capabilities of [AWS Textract](https://aws.amazon.com/textract/) by iterating through a S3 bucket, sending all appropriate formats to [DetectDocumentText](https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html), and serializing content, both for all output (bounding boxes, coordinates, etc) and only extracted text.
