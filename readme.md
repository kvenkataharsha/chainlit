This app is build uisng Chainlit + OpenAI  which takes csv file as input and perform data analysis based on the User Input. 

Please replace your OPENAI_API_KEY to you own OpenAI Key. (Please refer to this for platform.openai.com/account/api-keys for creating or updating your keys)

After replacing build your docker image (docker build -it YourImageName:ImageTag)

To Run the container : docker run -p 8000:8000 YourImageName
