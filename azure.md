Azure Notes
===========


func init FunctionAppProj --python
func new --name HttpExampleAb --template "HTTP trigger" --authlevel "anonymous"

az group create --name dpro3-deleteme-rg --location canadaeast
az storage account create --name dpro3storage --location canadaeast --resource-group dpro3-deleteme-rg --sku Standard_LRS
az functionapp create --resource-group dpro3-deleteme-rg --os-type Linux --consumption-plan-location $LOC --runtime python --runtime-version 3.8 --functions-version 3 --name dpro3function --storage-account dpro3storage

*func azure functionapp publish dpro3function

az group delete --name dpro3-deleteme-rg
az group delete --name dpro3-deleteme-rg


https://docs.microsoft.com/en-us/azure/container-registry/container-registry-tutorial-quick-task

*azure shell

# resource names

$RES_GRP="proj33-resource-grp-deleteme"

$LOC="eastus"
$RES_GRP="dpro3-resource-grp" 
$CONTAINER_REGISTRY="dpro3registrycontainer"
$APP_SERVICE_PLAN="dpro3appserviceplan"
$WEB_APP="dpro3-web-app"
$STORAGE_ACCOUNT="dpro3storage"
$FUNCTION_APP="dpro3-function-app"
$PREMIUM_PLAN="dpro3-premium-plan"
$KEYVAULT_NAME="dpro3-kv"

# Create resource & storage
az group create --resource-group $RES_GRP --location $LOC
az storage account create --name $STORAGE_ACCOUNT --location $LOC --kind StorageV2 --resource-group $RES_GRP --sku Standard_LRS 

# function app fpr linux python container - use PREMIUM_PLAN
az functionapp plan create --resource-group $RES_GRP --name $PREMIUM_PLAN --location $LOC --number-of-workers 1 --sku EP1 --is-linux
az functionapp create --resource-group $RES_GRP --runtime python --runtime-version 3.8 --functions-version 3 --name $FUNCTION_APP --storage-account $STORAGE_ACCOUNT --os-type Linux  --plan $PREMIUM_PLAN --disable-app-insights true

#create container registry
az acr create -n $CONTAINER_REGISTRY -g $RES_GRP --sku Standard --admin-enabled true

* create function app manually
#create function
func init LocalFunctionsProject --worker-runtime python --docker
cd LocalFunctionsProject
func new --name HttpExample --template "HTTP trigger"

* or clone from git
git clone https://github.com/arbalisi12/project2067.git

* goto azure portal and configure function app with container

# build container-registry/container-registry


#function app blob storage
az functionapp create --name $FUNCTION_APP --storage-account $STORAGE_ACCOUNT --consumption-plan-location $LOC --resource-group $RES_GRP --functions-version 3





#https-only
az storage account create --name $STORAGE_ACCOUNT --location $LOC --kind StorageV2 --resource-group $RES_GRP --sku Standard_LRS --https-only true

az functionapp delete --name $FUNCTION_APP --resource-group $RES_GRP
az keyvault create --name $KEYVAULT_NAME --resource-group $RES_GRP --location $LOC

  





# build container-registry/container-registry-tutorial-quick-task

az acr build --registry $CONTAINER_REGISTRY --image sample/kv:latest .

*git clone https://github.com/arbalisi12/project3

az acr build --registry $CONTAINER_REGISTRY --image functionapp/kv:v4 .

az acr build --registry $CONTAINER_REGISTRY --file Dockerfile --image sample/hello-world:v1 .
  
echo FROM mcr.microsoft.com/hello-world > Dockerfile

az acr build --registry $CONTAINER_REGISTRY --image hello:v1 .

az group delete --name $RES_GRP


# managed identity
az group create --name myResourceGroup --location westus
az appservice plan create --name myPlan --resource-group myResourceGroup --sku S1
az webapp create --name myApp --resource-group myResourceGroup --plan myPlan

az webapp identity assign --name myApp --resource-group myResourceGroup

$resourceURI = "https://<AAD-resource-URI-for-resource-to-obtain-token>"
$tokenAuthURI = $env:IDENTITY_ENDPOINT + "?resource=$resourceURI&api-version=2019-08-01"
$tokenResponse = Invoke-RestMethod -Method Get -Headers @{"X-IDENTITY-HEADER"="$env:IDENTITY_HEADER"} -Uri $tokenAuthURI
$accessToken = $tokenResponse.access_token



# Stop Azure VM
az vm stop --name {vm name} --g {resource group name}
# Deallocate Azure VM
az vm deallocate --name {vm name} -g {resource group name}


py -3.7 -m venv .venv

sql server
dpro3sqladmin
xx2121pw13!

vm
arnel
BP12

#!/bin/bash
location="East US"
randomIdentifier=random123

resource="resource-$randomIdentifier"
server="server-$randomIdentifier"
database="database-$randomIdentifier"

login="sampleLogin"
password="samplePassword123!"

startIP=0.0.0.0
endIP=0.0.0.0

echo "Creating $resource..."
az group create --name $resource --location "$LOC"

echo "Creating $server in $LOC..."
az sql server create --name $server --resource-group $resource --location "$LOC" --admin-user $login --admin-password $password

echo "Configuring firewall..."
az sql server firewall-rule create --resource-group $resource --server $server -n AllowYourIp --start-ip-address $startIP --end-ip-address $endIP

echo "Creating $database on $server..."
az sql db create --resource-group $resource --server $server --name $database --sample-name AdventureWorksLT --edition GeneralPurpose --family Gen4 --capacity 1 --zone-redundant false # zone redundancy is only supported on premium and business critical service tiers


https://dpro3storage.queue.core.windows.net/dpro3-test-queue/messages?sv=2019-12-12&ss=bfqt&srt=sco&sp=rwdlacupx&se=2021-11-18T00:17:33Z&st=2020-11-17T16:17:33Z&spr=https&sig=KEMpgKOm2uX2ipYCQ6TSrz2IJxRKB4ehiQ7jWKxGfx0%3D
	
https://dpro3storage.queue.core.windows.net/dpro3-test-queue


pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org azure.functions

pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org requirements.txt

azure.functions


c:\python\python38\python.exe -m pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org --upgrade pip


powershell.exe -noprofile -executionpolicy bypass -file .\storage.ps1

# bash
# Function app and storage account names must be unique.
storageName=mystorageaccount$RANDOM
functionAppName=myserverlessfunc$RANDOM
region=westeurope
pythonVersion=3.6 #3.7 also supported

# Create a resource group.
az group create --name myResourceGroup --location $region

# Create an Azure storage account in the resource group.
az storage account create \
  --name $storageName \
  --location $region \
  --resource-group myResourceGroup \
  --sku Standard_LRS

# Create a serverless function app in the resource group.
az functionapp create \
  --name $functionAppName \
  --storage-account $storageName \
  --consumption-plan-location $region \
  --resource-group myResourceGroup \
  --os-type Linux \
  --runtime python \
  --runtime-version $pythonVersion \
  --functions-version 3

# python blob container
https://www.datacareer.ch/blog/using-azure-functions-with-python/


