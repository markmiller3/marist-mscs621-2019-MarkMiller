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
#### The first step in recreating this porject is to setup a the Database on IBM Cloud Cloudant
You can follow a guide [here](https://cloud.ibm.com/docs/tutorials?topic=solution-tutorials-serverless-api-webapp)

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
5. Insert the Code Provided Below
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

Create Sequence of Actions to Retrive the Entries
1. 
