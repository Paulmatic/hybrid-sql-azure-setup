terraform {
  backend "azurerm" {
    resource_group_name   = "rg-terraform-state"
    storage_account_name  = "terraformstatepaul123456"  # updated
    container_name        = "tfstate"
    key                   = "terraform.tfstate"
  }
}
