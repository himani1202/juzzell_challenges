vpc.tf provisions a VPC, subnets and availability zones using the AWS VPC Module
security-groups.tf provisions the security groups used by the EKS cluster.
eks-cluster.tf provisions all the resources (AutoScaling Groups, etc...) required to set up an EKS cluster in the private subnets and bastion servers to access the cluster using the AWS EKS Module.


Steps to create EKS cluster

-> Run 'terraform init' to initialize the terraform workspace that downloads and configures provider (aws in this case)
-> Run 'terraform apply' to provision the eks cluster

Configure kubectl using below commands:

aws eks --region us-east-2 update-kubeconfig --name test-kpmg