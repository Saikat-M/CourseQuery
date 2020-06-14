# CourseQuery

<h2>About</h2>
<b>CourseQuery</b> is a chatbot designed to search for MOOCs or in more generalised way, we can say to search for <i>tutorials/contents</i> for a particular topic or subject over the internet. Now you can say <i>I can do that from internet also, why should I use this chatbot?</i>. Because you can interact with it from <b>Whatsapp</b>.

like we chat with our friends in Whatasapp, one will be just doing the same with the chatbot and will get hyperlinks of the pages as a reply and can visit that link directly from chatbox in his/her mobile browser. It's that simple.   

Now the the user need to do certain setup to use <b>CourseQuery</b> from Whatsapp and need to send a specific <i>Utterance</i> to trigger the chatbot. This will be explained next.

<h2>How to use it</h2>
The user needs to send this message <i><b>join place-rope</b></i> to this number: +14155238886 in <b>Whatsapp</b> to register his/her contact number in order to interact and get back replies from the chatbot. 

One may think <i>why this message?</i> or <i>why do I need to send a message to that number</i>(it's a US number)? For a longer description please refer the <b>Twilio</b> portion of the <b>How to develop it</b> section. 

But the shorter one is: It is needed to register the number(using which user will be interacting with the chatbot through Whatsapp) with the service <b>Twilio</b>, that helps to connect the user with the chatbot using Whatsapp. One can easily delist his/her number through sending <i><b>stop</b></i> to the name above mentioned number.

you can read more about Twilio from this link : https://www.twilio.com/

<h2>How to develop it</h2>

The services and components that have been used to build and use this chatbot in intended way are as follows:

<li><b>Amazon Lex</b> : This is the service offered by AWS, that has been used to build the <b>Chatbot</b></li>
<li><b>Google Custom Search API </b>: This API is offered by GCP and it has been used to search the internet using Google search engine with <i>topic</i> name provided by the user and give response accordingly</li>
<li><b>Twilio</b> : This is a third party service that has been used to integrate the <b>Amazon Lex bot</b> with <b>Whatsapp</b></li>

Now what configuration & developed need to be done for the above mentioned services to build this kind of a chatbot has been explained next.

<h3>Amazon Lex</h3>
<hr>

This is the service offered by AWS that has been used to create the chatbot.

To be able to use this service, one need to create an account in AWS Cloud portal from here: https://portal.aws.amazon.com/billing/signup#/start

After creating account, type <i>Amazon Lex</i> in the search bar upon clicking on the service name, it will be redirected to the Amazon Lex dashboard, where we will get an option to create a new bot through clicking on <i>Create</i>.

After the creation of the bot, the user will be taken to the console page, where there will be multiple tabs: <i>Editor</i>, <i>Settings</i>, <i>Channels</i>, <i>Monitoring</i>.

Our main work will be in <b>Editor</b> tab. Here we need to understand there things: 
<li>Intents: This is the purpose of an user to use a chatbot.</li> 
<li>Utterances: These are the messages needed to be sent in order to trigger the chatbot.</li> 
<li>Slots: This will be used to get the user input during the conversation with chatbot, to fulfill user's request.</li> 

For this Chatbot, the specifics are:

Intent: 'SearchMOOC'. 

Utterances:
<li>1. Find me some MOOCs </li>
<li>2. Find me some online courses </li>
<li>3. Help me to find online courses</li>
<li>4. Get me some online courses</li>
Any one of these 4 messages can be sent to the chatbot to trigger it. 

Slots: 'Topics'

This video can be referred for creating all these components: https://www.youtube.com/watch?v=KTa1T14nkbw

Now there's a section called '<b>Fulfillment</b>' in the console that give us two options to choose from, how we want to fulfill users request. For this chatbot the '<i>AWS Lambda Function</i>' has been chosen.

Please refer the 'lambda_function.py' file in the repository for the implementation of the functionality.

The above mentioned video can be referred to know how to create a lambda function and attach it to the Lex chatbot.

Now there's something in this project. As we will be making a '<b>http request</b>' we'll have to upload the '<i>requests</i>' package with the code in Lambda console and then only the '<i>import requests</i>' command will work properly. In order to do that we need to make a zip file out of the '<i><b>requests</b></i>' package and the '<i><b>lambda_function.py</b></i>' file. This we will be uploading using the <i>Upload a .zip file</i> option from the 'Actions' drop down, which we can see just above the code console.

The .zip file has been provided in the repository named as: '<b>lambda_function.zip</b>'. 

In the Lambda console there is a drop down at the beginning of the page beside the '<i>Test</i>' button, from there we can create a test payload (JSON object) through clicking on the '<b>Configure test events</b>' option to check whether the code that we have written is working as expected or not.

A .txt file named '<b>Test_Event.txt</b>' has been provided in the repository. It contains a sample JSON object to test the code.  

<h3>Google Custom Search API</h3>
<hr>

The component that is responsible for sending relevant response against user's query is Google's Custom Search API.

Refer this documentation: https://developers.google.com/custom-search/v1/using_rest

To be able to use the API, one need to do some configurations.

<b>First</b>, Enable the '<i>Custom Search API</i>' from Google Cloud Console. To do that <i>Sign Up</i> with cloud console at: https://cloud.google.com/ 

After Signing up click on '<b>Console</b>' button in top right corner. In the search bar of the console type:  <i>Custom Search API</i> and click on 'Enable API'.

<b>Second</b>, Now as the API is enabled to use, there are 3 required parameters needed to be sent with the API URL.

<i>API key</i> : This we can create from Google Cloud Console. If we click on the left hand side sandwich icon, we will see there's an option called <b>APIs & Services</b>. Upon hovering on the option another list will appear, there we need to choose <i>Credentials</i>. There we will get an option to create new API key from clicking on '+ CREATE CREDENTIALS' button.

<i>Custom search engine ID</i> : For this we need to create a custom search engine from this link: https://cse.google.com/all

Upon clicking on the '<i>Add</i>' button, we will need to provide some required info to create a custom search engine. 

After creation, in the left hand side menu there will be a collapsible option called '<i>Edit search engine</i>'. From there we need to click on the <b>Setup</b> option. There we will get the <i>Custom search engine ID</i> among many other info.

<i>Search query</i> : This is the query, that we will be sending from Lambda.

The configuration is done for this component

The API URL will be like this:

https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_CUSTOM_SEARCH_ENGINE_ID&q=YOUR_QUERY_STRING

<h3>Twilio</h3>
<hr>

Amazon Lex provides multiple options (4 to be exact) of <i>Channels</i> with which we can integrate our chatbot, so that we can access the chatbot from that channel. <b>Twilio</b> is one of them.

Now here comes the <b>Whatsapp</b> integration. Twilio provides an option to integrate our app with Whatsapp, so that we can interact with our app through Whatsapp, in our case which is the chatbot <i>CourseQuery</i>.

So to simplify the connectivity, here is the flow:

Amazon Lex chatbot can be integrated with Twilio --> Twilio lets us connect our app connect with Whatsapp --> So, we connect our Chatbot with Whatsapp through Twilio.

To connect the chatbot with Twilio, we need to provide certain credentials in the Amazon Lex console, which are: 

<li><b>Account SID</b></li>
<li><b>Authentication Token</b></li>

To get this we need to create an account in Twilio. one can do that from this link: https://www.twilio.com/try-twilio

No credit card is required to do so. After creating the account our account is credited with an amount of $15. Another thing is, we are given a contact number for free, using which we can develop things with the services(One of which is the <i><b>Whatsapp</b></i> connectivity) that Twilio offers.

We can get the above mentioned credentials from 'Dashboard' and need to provide it in the AWS console.

One need to go to the 'Channels' tab of the Amazon Lex service. There, after choosing the <i>Twilio</i> option, credentials are needed to be provided the  in the respective fields. Among other required fields, 'Alias' is one, where we need to provide the version of the chatbot that we need to integrate with. For this we will have to <b>Publish</b> the chatbot first. 

After providing also the required infos we will have to click on the '<b>Activate</b>' button to get the <i>EndPoint URL</i> which we will need to integrate the chatbot with Whatsapp.

Now back to Twilio console. In the left-hand side navigation bar, below the 'Home' icon there is another icon of 'Messaging' this option is called 'Programmable SMS' Upon clicking on it, we will get option of <b>Whatsapp</b> integration among other options or this link can be used directly: https://www.twilio.com/console/sms/whatsapp/sandbox

To check our app in development environment, Twilio provides a sandbox environment. Here we need to provide that <i>EndPoint URL</i> that we received from AWS in the '<i>WHEN A MESSAGE COMES IN</i>' filed and method will be '<i>HTTP Post</i>'.

At last to be able to interact with the chatbot from whatsapp using your number you need to go to the 'Learn' option under 'Whatsapp'(or this link can used directly: https://www.twilio.com/console/sms/whatsapp/learn)

Here instructions will be given to <b>Register</b>/<b>Subscribe</b> the Whatsapp number using which user want to interact with the chatbot.

The instruction includes the contact number and a message that needs to be sent to that contact number. In this case the contact number is: +14155238886 and the message is: 'join place-rope'.

If there's still any ambiguity to understand the steps this link can be referred: https://docs.aws.amazon.com/lex/latest/dg/twilio-bot-association.html 

After doing this we are ready to use the chatbot <b>CourseQuery</b>.

                                                              



