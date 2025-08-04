variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
}

variable "client_id" {
  description = "Azure Client ID (App ID)"
  type        = string
}

variable "client_secret" {
  description = "Azure Client Secret"
  type        = string
  sensitive   = true
}

variable "tenant_id" {
  description = "Azure Tenant ID"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Resource Group"
  type        = string
  default     = "rg-hybrid-sql-demo"
}

variable "location" {
  description = "Azure Region"
  type        = string
  default     = "westus2"
}

variable "sql_server_name" {
  description = "SQL Server Name"
  type        = string
  default     = "my-mssql-server-paul-240804"
}

variable "sql_database_name" {
  description = "SQL Database Name"
  type        = string
  default     = "hybriddb"
}

variable "sql_admin_user" {
  description = "SQL Server admin username"
  type        = string
  default     = "sqladminuser"
}

variable "sql_admin_password" {
  description = "SQL Server admin password"
  type        = string
  sensitive   = true
}

variable "my_ip" {
  description = "Your public IP address to whitelist for SQL access"
  type        = string
}
