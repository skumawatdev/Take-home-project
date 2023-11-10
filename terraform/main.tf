# terraform/main.tf

provider "aws" {
  region = "your-aws-region"
}

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
}

resource "aws_subnet" "my_subnet" {
  vpc_id = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_instance" "my_instance" {
  ami           = "your-ami-id"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.my_subnet.id

  tags = {
    Name = "my-instance"
  }
}

resource "aws_security_group" "my_security_group" {
  vpc_id = aws_vpc.my_vpc.id

  # Add necessary security group rules
}

# Additional Terraform resources as needed
