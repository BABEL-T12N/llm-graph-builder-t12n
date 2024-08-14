from langchain_community.document_loaders import S3DirectoryLoader, ObsidianLoader
import logging
import boto3
import os
from urllib.parse import urlparse

def get_s3_files_info(s3_url,aws_access_key_id=None,aws_secret_access_key=None):
  try:
      # Extract bucket name and directory from the S3 URL
      parsed_url = urlparse(s3_url)
      bucket_name = parsed_url.netloc
      directory = parsed_url.path.lstrip('/')
      try:
        # Connect to S3
        s3 = boto3.client('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)

        # List objects in the specified directory
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory)
      except Exception as e:
         raise Exception("Invalid AWS credentials")
      
      files_info = []

      # Check each object for file size and type
      for obj in response.get('Contents', []):
          file_key = obj['Key']
          file_name = os.path.basename(file_key)
          logging.info(f'file_name : {file_name}  and file key : {file_key}')
          file_size = obj['Size']

          # Check if file is a PDF
          if file_name.endswith('.pdf'):
            files_info.append({'file_key': file_key, 'file_size_bytes': file_size})
          
      return files_info
  except Exception as e:
    error_message = str(e)
    logging.error(f"Error while reading files from s3: {error_message}")
    raise Exception(error_message)

def get_s3_directory_info(s3_url, aws_access_key_id=None, aws_secret_access_key=None):
    try:
      # Extract bucket name and directory from the S3 URL
        parsed_url = urlparse(s3_url)
        bucket_name = parsed_url.netloc
        directory = parsed_url.path.lstrip('/')
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory)

        # Check each object for file size and type
        for obj in response.get('Contents', []):
            file_key = obj['Key']
            file_name = os.path.basename(file_key)
            file_size = obj['Size']
            logging.info(f'file_name : {file_name}  and file key : {file_key}')
            # Check if file is a PDF
            
            #files_info.append({'file_key': file_key, 'file_size_bytes': file_size})

        return directory
    except Exception as e:
        error_message = str(e)
        logging.error(f"Error while reading files from s3: {error_message}")
        raise Exception(error_message)

def get_s3_pdf_content(s3_url,aws_access_key_id=None,aws_secret_access_key=None):
    try:
      # Extract bucket name and directory from the S3 URL
        parsed_url = urlparse(s3_url)
        bucket_name = parsed_url.netloc
        logging.info(f'bucket name : {bucket_name}')
        directory = parsed_url.path.lstrip('/')
        if directory.endswith('.pdf'):
          loader=S3DirectoryLoader(bucket_name, prefix=directory,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
          pages = loader.load_and_split()
          return pages
        else:
          return None
    
    except Exception as e:
        logging.error(f"getting error while reading content from s3 files:{e}")
        raise Exception(e)
      
def get_obsidian_file_content(directory_path:str):
    try:
      loader=ObsidianLoader(directory_path)
      pages = loader.load()
      logging.debug(f"pages length : {len(pages)}")
      return pages
    
    except Exception as e:
        logging.error(f"getting error while reading content from obsidian files:{e}")
        raise Exception(e)


def get_documents_from_s3(s3_url, aws_access_key_id, aws_secret_access_key):
    try:
      parsed_url = urlparse(s3_url)
      bucket = parsed_url.netloc
      file_key = parsed_url.path.lstrip('/')
      file_name=file_key.split('/')[-1]
      s3=boto3.client('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
      response=s3.head_object(Bucket=bucket,Key=file_key)
      file_size=response['ContentLength']
      
      logging.info(f'bucket : {bucket},file_name:{file_name},  file key : {file_key},  file size : {file_size}')
      pages=get_s3_pdf_content(s3_url,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
      return file_name,pages
    except Exception as e:
      error_message = str(e)
      logging.exception(f'Exception in reading content from S3:{error_message}')
      raise Exception(error_message)
    
def get_documents_from_s3_to_system_path(s3_url, aws_access_key_id, aws_secret_access_key, local_directory):
    try:
        # Extract bucket name and directory from the S3 URL
        parsed_url = urlparse(s3_url)
        bucket_name = parsed_url.netloc
        directory = parsed_url.path.lstrip('/')
        
        # Connect to S3
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        
        # List objects in the specified directory
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory)
        
        if 'Contents' not in response:
            logging.info("No files found in the specified S3 directory.")
            return
        
        # Ensure the local directory exists
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)
        
        # Download each file and save it to the local system
        for obj in response.get('Contents', []):
            file_key = obj['Key']
            
            # Skip directories
            if file_key.endswith('/'):
                continue
            
            local_file_path = os.path.join(local_directory, file_key)
            
            # Create local directories if they don't exist
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            
            # Download the file
            s3.download_file(bucket_name, file_key, local_file_path)
            logging.info(f"Downloaded {file_key} to {local_file_path}")
          
        # get last folder from s3_url
        logging.info(f's3_url : {s3_url}') 
        last_folder = s3_url.split('/')[-2]
        logging.info(f'last folder : {last_folder}')   
        obsidian_path = os.path.join(local_directory,last_folder)
        logging.info(f'the obsidian path: {obsidian_path}')
        pages = get_obsidian_file_content(obsidian_path)
        logging.info("All files have been downloaded successfully.")  
        return f"{last_folder}/", pages
        
        
        
    except Exception as e:
        error_message = str(e)
        logging.error(f"Error while reading files from S3: {error_message}")
        raise Exception(error_message)
    
    
def get_s3_files_info(s3_url,aws_access_key_id=None,aws_secret_access_key=None):
  try:
      # Extract bucket name and directory from the S3 URL
      parsed_url = urlparse(s3_url)
      bucket_name = parsed_url.netloc
      directory = parsed_url.path.lstrip('/')
      try:
        # Connect to S3
        s3 = boto3.client('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)

        # List objects in the specified directory
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory)
      except Exception as e:
         raise Exception("Invalid AWS credentials")
      
      files_info = []

      # Check each object for file size and type
      for obj in response.get('Contents', []):
          file_key = obj['Key']
          file_name = os.path.basename(file_key)
          logging.info(f'file_name : {file_name}  and file key : {file_key}')
          file_size = obj['Size']

          # Check if file is a PDF
          if file_name.endswith('.pdf'):
            files_info.append({'file_key': file_key, 'file_size_bytes': file_size})
          
      return files_info
  except Exception as e:
    error_message = str(e)
    logging.error(f"Error while reading files from s3: {error_message}")
    raise Exception(error_message)