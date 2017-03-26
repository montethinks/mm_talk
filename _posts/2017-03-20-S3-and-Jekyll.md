---
layout: post 
title:  "Serving Jekyll static site on AWS S3"
---

This is a reference for setting up AWS S3 bucket to host static. Jekyll is being used to build the site. This will be a multi-part series that will eventually cover using Route 53 DNS Resoultion for adding a custom domain and a CloudFront content delivery network.

First steps to hosting a static website using AWS S3:

Create the following S3 Buckets:
  - example.com (domain name)
  - www.example.com (www domain name)
  - logs.example.com (for log files if logging is enabled)



Add permissions and configure main bucket with domain name (example.com)
  
  Edit bucket policy by pasting the following into the policy

    {
  "Version":"2012-10-17",
  "Statement": [{
    "Sid": "Allow Public Access to All Objects",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::example.com/*"
  }
 ]
}

  - Enable logging to the logs bucket. 



ONLY ADD THE CONTENTS OF THE ```_site``` DIRECTORY, OTHERWISE THE INDEX.HTML FILE IS NOT VISIBLE AS THE ROOT.

(Need to add final steps and clarify first steps.)