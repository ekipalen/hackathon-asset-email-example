# Example: Use Storage Asset and send emails

This template leverages the new Python open-source structure [robo](https://github.com/robocorp/robo), the [libraries](https://github.com/robocorp/robo#libraries) from to same project as well.
The full power of [rpaframework](https://github.com/robocorp/rpaframework) is also available for you on Python as a backup while we implement new Python libraries.

This example: 
- Reads csv formatted list of fictional customers/leads and a email template from the Robocorp Control Room's Storage Assets 
- Sends each of the customer an email using Mailgun if testing mode is not enabled
- If testing mode is enabled the email is only sent for one recipient. 

For more information, do not forget to check out the following:
* [Robocorp Documentation -site](https://robocorp.com/docs)
* [Portal for more examples](https://robocorp.com/portal)
* [robo repo](https://github.com/robocorp/robo) as this will developed a lot...