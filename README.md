 # Malafy's Meat Processing LLC Order Assistant Application
 ------------------------------------------------------------------
This application is desgined to aid a customer of Malafys Meat Processing with providing a simple and easy way to order meat. The project idea was given to me by a fellow professor who wanted an easier way ordering his meat. Handling high amounts of meat, makes the processing frustrating and tedious. 
 
 > Malafys Meat Processing has has a complex way for customers to order meat. The interactive web application was geared to simplifys the ordering process. This web app was built from stratch using Python Flask and HTML. It utilizies multiple different modules to complete the tasks.
 
 >The web application completes task such as calculating the total price, price per item, number of pounds ordered, and supply an easy to understand summary of your order. 
 
-------------------------------------------------------------------
## Dependencies
1. IBM Cloud Account
2. Google Cloud Account
3. Docker

-------------------------------------------------------------------
## Architecture Diagram


-------------------------------------------------------------------
## Prerequisites
#### Signup for Cloud Services
The two cloud services used are Google Cloud and IBM Cloud. Please sign up for the free trials on both services.
 - [Google Cloud](https://cloud.google.com/) 
 - [IBM Cloud](https://www.ibm.com/cloud)
 

#### Ensure Docker is Installed on your Device
Docker is used throught this setup, please ensure it is installed on your device.
- [Docker Installation](https://docs.docker.com/v17.09/engine/installation/)

------------------------------------------------------------------
## Configurations
### The first step in recreating this project is to setup a the Database on IBM Cloud Cloudant

***Note: This is only if you want to recreate the project, if you are downloading the provided one you can skip to the deployment section.***

You can follow a guide [here](https://cloud.ibm.com/docs/tutorials?topic=solution-tutorials-serverless-api-webapp)

>The guide above will provide a high level overiew of creating the cloudant database, creating the neccessary functions, and creating the api. Below is a quick overview of the guide.

#### IBM Cloudant and Functions Configuration
Creating the Cloudant Database:
1. Navigate to Cloudant Database (you may need to search for it)
2. Start by creating a Cloudant database
    - Give the database a name like **Meat-Items-db**
    - Select the region you would like
    - Ensure you are using the Lite plan (free tier)
    - Make sure you use **Use both legacy credentials and IAM** for Available authentication methods
3. Create the Cloudant Database

Create Service Credentials for Database:
1. Under the Database we just created, like on **Service Credentials**
2. Click **New Credential**
3. Click **Add**

Creating a Cloud Function:
1. Navigate to Cloud Functions
2. On the pane to the left, click **Actions** then **Create**
3. Create the action with a name like **Prepare-Meat-Items**
4. Select **Node.js** as the Runtime
5. Delete the given code and insert the code below 
```shell
function main(params) {
  if (!params.id || !params.item_name || params.price) {
    return Promise.reject({ error: 'No item Found'});
  }

  return {
    doc: {
      createdAt: new Date(),
       id: params.id,
       item_name: params.item_name,
       price: params.price
    }
  };
}
```
6. Click Save

Add another Action to the Sequence:
1. Click on **Enclosing Sequences** in the left pane
2. Click **Add to Sequence**
3. Enter a name for the sequence like **Meat-Items-Sequence**
4. Click **Create and Add**

Adding a Second Action to the Sequence:
1. Click on the recent action we created above (**Meat-Items-Sequence**) and click **Add**
2. Select **Use Public**,**Cloudant** and choose **create document** under **Actions**
3. Click create **New Binding**
4. Give a name like **Meat-Item-Binding**
5. For Cloud Instance choose **Input Own Credentials**
6. Fill in your credentials for database (see next section for instructions on how to get there)

Accessing Database Credentials for Second Action in the Sequence:
1. Go to **Resource List** in the left hand pane
2. Click **Service**, **Meat-Items-db**
3. Click **Service Credentials** in the left pane
4. Click **view crednetials** service-credentials-1
5. Insert the **Host, Password, and Username** from credentials into the last step above
6. Insert **Database** which is the name of the cloudant database

Create Sequence of Actions to Retrive the Entries:
1. Under **Functions** click **Create** new Node.js action under default package
2. Create a name for the action like **Meat-Items-Input**
3. Delete the given code and insert the code below
```shell
function main(params) {
  return {
    params: {
      include_docs: true
    }
  };
}
```
4. Click **Save**

Add an Action to a Sequence:
1. Click **Enclosing Sequences, Add to Sequence** then **Create New**
2. Give an **Action Name** like **Read-Meat-Items-Sequence**
3. Click **Create and Add**
4. Click on the sequence **Read-Meat-Items-Sequence**, we just created
5. Click **Add**
6. Under **My Bindings** choose **Meat-Item-Bindind** and click **Add** 
7. Click **Add** again
8. Under **Create New** enter a name like **Format-Meat-Items**, then click **Create and Add**
9. Click on the **Format-Meat-Items** and replace the code given with the code below
```shell
const md5 = require('spark-md5');

function main(params) {
  return {
    entries: params.rows.map((row) => { return {
      id: row.doc.id,
      item_name: row.doc.item_name,
      price: row.doc.price
    }})
  };
}
```
10. Click on **Save**

Invoke the Sequence:
1. Click on **Actions** then click on the sequence **Read-Meat-Items-Sequence**
2. Click on **Save** and **Invoke**

Create the API:
1. Go to **Actions**
2. Click on the sequence **Read-Meat-Items-Sequence**
3. Next to name click **Web Action**, check **Enable as Web Action** and then **Save**
4. Do the same as above for the sequence **Meat-Items-Sequence**
5. Go to **APIs** under Functions
6. Click **Create a Cloud Function API
7. Set the name such as **Meat-Items** and the base path to /Meat-Items
8. Click **Create operation**
9. Set path to **/entries** set verb to **GET**
10. Select the action **Read-Meat-Items-Sequence**
11. Click **Create operation**
12. Set path to **/entries** set verb to **PUT**
13. Select the action **Meat-Items-Sequence**
14. Save and expose the API

Click [here](https://portal.us-south.apigw.cloud.ibm.com/portal?artifactId=9e1186cf-5f8c-407e-9763-7ba1ed99fffd) for a link to post your entries to the database.

Please Note: If you create a new database you must replace the API url in the api_call.py file with the new url one you just created.

----------------------------------------------------------------------------------------
## Deployment - Local 
>This section is going to walkthrough the steps need to deploy the web application locally on your device. This section will also cover posting the container to docker hub.

1. Run a git clone of this repository to get acess to all the required files you will need.
```shell
git clone https://markmiller3/marist-mscs621-2019-MarkMiller.git
```
2. Once the git clone has finsihed change directories to directory you cloned the repository
3. From inside of the repository directory, run the following command
```shell
docker build --tag meat-order-app .
```
> This will build the docker image with the given tag meat-order-app
The output will look similar to:
![alt-key](https://github.com/markmiller3/marist-mscs621-2019-MarkMiller/Readme_Images/docker-build-local.png)

4. To run the docker image execute the following command
```shell
docker run --name meat-order-app -p 5000:5000 meat-order-app
```
>This is running the built image and will now be accessible on by entering the url http://0.0.0.0:5000/. 
> The --name is setting the name of the container and -p is setting to port of the container.

The output will look similar to this: 


5. 
