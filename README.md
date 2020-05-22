# TestingAWSTextract

Test OCR capabilities of [AWS Textract](https://aws.amazon.com/textract/) by iterating through an S3 bucket, sending all appropriate formats to [DetectDocumentText](https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html), and serializing content, both for all output (bounding boxes, coordinates, etc) and only extracted text.


## Getting Started

Upload input files to an S3 bucket and enable DetectDocumentText policies on bucket.  Ensure input files are PNG or JPEG for [synchronous operations](https://docs.aws.amazon.com/textract/latest/dg/sync-calling.html).

### Prerequisites

* [boto3](https://pypi.org/project/boto3/)
* [awscli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
* [AWS Configuration and credential file](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

