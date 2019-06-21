# Personal Expenses Tracker

#### tldr: expense tracker using email notifications, Zapier, and Google Sheets

Thanks to this awesome [project](https://github.com/j-c-peters/spending-tracker) for the template & idea. Also checkout his [Medium post](https://medium.com/swlh/how-i-got-control-of-my-spending-with-a-couple-no-code-services-and-only-100-lines-of-python-code-36c8ac75f670) explaining the idea behind the project.

### Part 1: set up email notifications for your credit/debit card & Venmo

For your credit/debit card service, dive into their settings and turn on email notifications for every transactions.


For Venmo, you can either turn on email notifications for payments in the mobile app or [here](https://help.venmo.com/hc/en-us/articles/217532247-Edit-Account-Settings).


### Part 2: set up zapier & email auto forwarding
1. Set up a zap in [Zapier](https://zapier.com).
2. Use email parser for the **Trigger**. This will parse the necessary information from your email. Send it a few emails to set up the parser correctly (Mine parses only the amount and the "description" of the payment/transaction).
3. Set up auto forwarding to the email address (ex: expensetracker@robot.zapier.com) you just set up. For Gmail users, follow the instructions on Zapier.
4. Go back to your Zap to set up the **Action** part. Choose *Webhooks* and select *POST* for this.
5. Enter in the URL of your backend service of choice for the destination of the POST request. 
6. Turn on your Zap. 

Ideally, every time your email service forwards a payment notification to this Zap, it would send a single POST request to your backend service with this following format:
```
{
	"amount": "$15.00",
    "description": "food"
}
```

### Part 3: set up Google Sheets

#### Set up a sheet

Copy this [workbook](https://docs.google.com/spreadsheets/d/1o6o5-q1O2rX9Ikv6kUx4_Gr1T0PAmeFwk4DYnu7NoKE/edit#gid=0) into your Google Drive.

#### Set up Google Sheets API

Create a new project on the [Google API Console](https://console.google.developers.com). Go to the `Credentials` > `Create Credentials` > `Service account key`.

Choose 'New service account'. Name it whatever you want, and remember to select `Project` > `Edit` for the role. Create the credentials,  and save the associated JSON file with the necessary credentials/secrets to edit the workbook. Needless to say, don't put this on anything publicly accessible (repos, etc).

Finally, enable [Google Sheets API](https://console.developers.google.com/apis/api/sheets.googleapis.com) for your project.

### Part 4: write your backend API

You can use the Flask application in this repo as is, although it may not work perfectly with your bank/card's email notifications.

Another option is to write your own in the framework of your choice, since it's really easy. The heavy work is (hopefully) done by your email and Zapier. All the server needs to do is to read the request and write the amount & description as a new row in the "Expenses" sheet of the workbook.

Optionally, you can also edit the workbook to best suit your needs, maybe to include for categories for your spendings.

### Part 5: summary

Basically the workflow is like this:

Bank/Venmo email notification > Zapier > Backend API > Google Sheet.

1. I pay my friend using Venmo:

2. Venmo emails me with the notification.

![venmo](https://imgur.com/6IxFzJL.png)

3. Gmail forwards it to my Zap.
4. Zap fires off a POST request to my Flask application.

![Zap](https://imgur.com/k4ICw0D.png)

5. The application adds the new payment as a new row in the 'expenses' sheet in the workbook.

![expenses](https://imgur.com/XDgBrFH.png)

6. Tada!!!

![summary](https://imgur.com/WdMBW2y.png)