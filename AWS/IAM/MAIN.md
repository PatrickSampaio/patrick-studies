##IAM

IAM consists of the following
- Users
- Groups
- Roles
- Policy Documents (JSON)
`
{"Version": "2017-10-17",
 "Statement":
[
 {"Effect":"Allow",
  "Action":"*",
  "Resources":"*"
 }
]
}
`

- IAM is universal. It does not apply to regions at this time
- The "root account" is simply the account created when first setup your AWS account. It has complete Admin access
- New Users have NO permissions when first created.
- New Users are assigner an Access Key & Secret Access Keys when first created
- You only get to view these credentials once. If you lose them, you have to regenerate them.
- Always setup MFA on your root account
- You can create and customise your own password rotation policies
