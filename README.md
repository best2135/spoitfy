# **Spotify Artist and Album Info CLI**

A simple command-line interface (CLI) tool to quickly fetch an artist's top 10 tracks and the full tracklist of a specified album using the Spotify Web API.

## **🎵 Features**

* **Artist Top Tracks:** Enter any artist's name to get a list of their top 10 most popular songs in the US.  
* **Album Tracklist:** Provide an album name to retrieve its complete tracklist.  
* **Secure:** Uses a .env file to keep your Spotify API credentials safe and out of the main script.  
* **Robust:** Includes error handling for cases where an artist or album cannot be found.

## **⚙️ Setup and Installation**

Follow these steps to get the project running on your local machine.

### **1\. Prerequisites**

* Python 3.6+  
* A Spotify Developer account to get API credentials. You can create one [here](https://developer.spotify.com/dashboard/).

### **2\. Clone the Repository**

First, clone this repository to your local machine or download the source code.

git clone \<your-repository-url\>  
cd \<your-repository-directory\>

### **3\. Create a Virtual Environment**

It is highly recommended to use a virtual environment to manage project dependencies.

\# Create the virtual environment  
python \-m venv venv

\# Activate it (Git Bash on Windows)  
source venv/bin/activate

\# Or activate it (PowerShell on Windows)  
\# .\\venv\\Scripts\\Activate.ps1

### **4\. Install Dependencies**

Install the required Python packages using the provided requirements.txt file.

pip install \-r requirements.txt

### **5\. Set Up Environment Variables**

This is the most important step for connecting to the Spotify API.

1. Create a file named .env in the root directory of your project.  
2. Open your Spotify Developer Dashboard, go to your application, and find your **Client ID** and **Client Secret**.  
3. Add your credentials to the .env file like this:

CLIENT\_ID=Your\_Spotify\_Client\_Id\_Goes\_Here  
CLIENT\_SECRET=Your\_Spotify\_Client\_Secret\_Goes\_Here

## **▶️ How to Use**

Once the setup is complete, you can run the application from your terminal.

1. Make sure your virtual environment is activated.  
2. Run the script:

python spotify\_api\_call\_app.py

3. The script will then prompt you to enter an artist's name and an album name.

### **Example Session**

$ python spotify\_api\_call\_app.py  
enter artist name: Tame Impala  
1\. The Less I Know The Better  
2\. New Person, Same Old Mistakes  
3\. Borderline  
4\. Feels Like We Only Go Backwards  
5\. Let It Happen  
6\. Yes I'm Changing  
7\. Elephant  
8\. Lost In Yesterday  
9\. Is It True  
10\. 'Cause I'm A Man

enter album name: Currents  
1\. Let It Happen  
2\. Nangs  
3\. The Moment  
4\. Yes I'm Changing  
5\. Eventually  
6\. Gossip  
7\. The Less I Know The Better  
8\. Past Life  
9\. Disciples  
10\. 'Cause I'm A Man  
11\. Reality In Motion  
12\. Love/Paranoia  
13\. New Person, Same Old Mistakes  
