## Active Directory

1 - The Flow is initiated when a use browses to the ADFS samples site `https://Fully.Qualified.Domain.Name.Here/adfs/ls/ldpInitiatedSignOn.aspx` inside his domain. When you install ADFS, you get a new virtual directory named adfs for your default website, which includes this page

2 - Th sign-on page authenticates the user against AD, Depdendingon the browser that the user is using, he might be prompted for his AD username and password

3 - User's broswer recieves a SAML assertion in the form of an authentication response from ADFS

4 - User's browser posts the SAML assertion to the AWS sign-in endpoint for SAML `https://signin.aws.amazon.com/sam`. Behind the scenes sign-in uses the AssumeRoleWithSAML, api to request temporary security credentials and then constructs a sign-in URL for the AWS Mangment Console

5 - User's browser recieves the sign-in URL and is redirected to the console
