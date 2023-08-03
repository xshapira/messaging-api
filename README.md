# Messaging API

Messaging API that allows to manage messages between users.

## Features

### User Authentication

* **Signup** - Create a new user account by providing username and password.
* **Login** - Authenticate existing users with username and password.

### Messaging

* **Write Message** - Authenticated users can send messages to others with subject and body.
* **Get User Messages** - Get all messages sent to or from an authenticated user.
* **Get Unread User Messages** - Get all unread messages for an authenticated user.
* **Read Message** - Get a specific message by ID and mark as read if accessed by receiver.
* **Delete Message** - Allow sender or receiver to delete a specific message.

### Security

* **Token Authentication** - Only authenticated users can access endpoints. Users get a token on signup/login that must be included in the Authorization header.

<div style="margin-top: 70px; ">

# Endpoints

## Users

### Signup

Create a new user account.

**POST** `/api/users/signup/`

Request body:

```json
{
  "username": "new_user",
  "password": "secret"
}
```

Returns auth token on success.

After signing up a new user, copy the returned auth `token` , your `username` , and `password` , then update the following variables in the Postman collection:

`token` - Set this to the auth token received after signup

`current_user` - Set this to your username

`password` - Set this to your password

This will allow you to make authenticated requests to the API after registering a new user account.

### Login

Authenticate an existing user.

**POST** `/api/users/login/`

Request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Returns auth token on success.

## Messages

### Get current user's messages

Get a list of messages for the authenticated user.

**GET** `/api/messages/`

### Compose message

Create a new message.

**POST** `/api/messages/create/`

Request body:

```json
{
  "from_user": "jane_doe",
  "to_user": "your_username",
  "subject": "Meeting invite",
  "body": "Let's meet at 2pm tomorrow."
}
```

### Get unread messages

Get a list of unread messages for the authenticated user.

**GET** `/api/messages/unread/`

### Read message

Get a specific message.

**GET** `/api/messages/{message_id}/`

### Update message

Update an existing message.

**PUT** `/api/messages/{message_id}/`

Request body same as compose message.

### Delete message

Delete a message.

**DELETE** `/api/messages/{message_id}/`
