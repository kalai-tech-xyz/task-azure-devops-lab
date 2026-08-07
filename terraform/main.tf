terraform {
     required_providers {
       azurerm = {
         source  = "hashicorp/azurerm"
         version = "~> 4.0"
       }
     }
   }
   
   provider "azurerm" {
     features {}
   }
   
   resource "random_id" "storage_suffix" {
     byte_length = 4
   }
   
   resource "azurerm_resource_group" "lab_rg" {
     name     = "rg-devops-task7-kalai"
     location = "eastus"
   }
   
   resource "azurerm_storage_account" "lab_storage" {
     name                     = "stdevopslab-task7${random_id.storage_suffix.hex}"
     resource_group_name      = azurerm_resource_group.lab_rg.name
     location                 = azurerm_resource_group.lab_rg.location
     account_tier             = "Standard"
     account_replication_type = "LRS"
   }
   
   resource "azurerm_storage_container" "lab_container" {
     name                  = "free-blob-container"
     storage_account_id    = azurerm_storage_account.lab_storage.id
     container_access_type = "private"
   }
