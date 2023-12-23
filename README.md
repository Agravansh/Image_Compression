---

# Image Compression and AWS S3 Upload Script

## Overview

This Python script helps you compress images in a specified folder and upload them to an AWS S3 bucket. It's handy for reducing image sizes while maintaining quality.

## Prerequisites

Make sure you have Python 3 installed on your machine.

```bash
pip install boto3 Pillow
```

## Usage

1. **Run the Script:**

   Open your terminal or command prompt and navigate to the script's directory. Run the following command:

   ```bash
   python image_compress_script.py
   ```

2. **Enter AWS Credentials:**

   When prompted, enter your AWS Access Key, AWS Secret Key, target S3 bucket name, and the directory path containing your images.

3. **Set Compression Quality:**

   You'll be asked to set the compression quality (0-100). The default is 95, and you can adjust it based on your needs.

4. **Wait for Completion:**

   The script will do its magic—compressing and uploading images. Once done, it will display a success message.

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)

## Important Notes

- Compressed images are temporarily saved locally with a ".compressed" extension and removed after successful S3 upload.
- The script simplifies the image compression process, making it easy to use for basic tasks.

## Troubleshooting

- If any issues occur during the compression or upload process, the script will display an error message. Ensure you've provided accurate AWS credentials and that your S3 bucket is accessible.

## Feedback and Contribution

This script is a basic tool that can be enhanced over time. If you have feedback or want to contribute, feel free to reach out!

---
