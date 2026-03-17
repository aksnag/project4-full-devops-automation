variable "resource_group_name"{
    default = "devops-project4-rg"
  
}

variable "location" {
    default = "eastus"
  
}

variable "cluster_name" {
    default = "devops-project4-aks"
  
}

variable "node_count" {
    default = 1
  
}

variable "vm_size" {
  default = "standard_d2s_v3"
}
