variable "credentials" {
  description = "GCP credentials for zoomcamp24"
  default     = ".secrets/sa-eze.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}


variable "project" {
  description = "GCP project id"
  default     = "eze-zoomcamp24"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "US"
}

variable "bq_dataset_name" {
  description = "Sandbox for homework and deadlines in Zoomcamp24"
  #Update the below to what you want your dataset to be called
  default     = "SBOX"
}

variable "gcs_bucket_name" {
  description = "Bucket name at GCS (data-lake)"
  #Update the below to a unique bucket name
  default     = "zoomcamp24"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
